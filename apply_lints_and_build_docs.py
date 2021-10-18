"""Apply each lint to all modules and build documentation.

Command example:
$ python apply_lints_and_build_docs.py
$ python apply_lints_and_build_docs.py --skip_overall_docs_build
"""

import os
import re
import shutil
import subprocess as sp
from argparse import ArgumentParser
from argparse import Namespace
from logging import Logger
from typing import List
from typing import Match
from typing import Optional
import multiprocessing as mp

from typing_extensions import Final
from typing_extensions import TypedDict

from apysc._console import loggers
from apysc._lint import lint_hash_util
from apysc._file import module_util

logger: Logger = loggers.get_info_logger()


class LintCommand(TypedDict):
    command: str
    lint_name: str


FLAKE8_NO_PATH_COMMAND: Final[str] = (
    'flake8 --ignore E402,W503'
)

FLAKE8_COMMAND: Final[str] = (
    f'{FLAKE8_NO_PATH_COMMAND} ./'
)

NUMDOCLINT_COMMAND: Final[str] = (
    'numdoclint -p ./ -r -f test,sample,_test,_sample'
)

MYPY_NO_PATH_COMMAND: Final[str] = (
    'mypy --ignore-missing-imports --follow-imports skip '
    '--disallow-untyped-calls --disallow-untyped-defs '
    '--strict-optional --strict-equality'
)

MYPY_COMMAND: Final[str] = (
    f'{MYPY_NO_PATH_COMMAND} ./apysc/ '
    './tests/ ./test_projects/'
)


def _get_module_paths() -> List[str]:
    """
    Get the Python module paths in the project.

    Returns
    -------
    module_paths : list of str
        Python module paths in the project.
    """
    logger.info('Getting module paths...')
    dir_paths: List[str] = [
        './apysc/',
        './docs_src/',
        './tests/',
        './test_projects/',
    ]
    with mp.Pool(processes=len(dir_paths)) as p:
        module_paths_list: List[List[str]] = p.map(
            func=module_util.get_module_paths_recursively,
            iterable=dir_paths)
    module_paths: List[str] = []
    for module_paths_ in module_paths_list:
        module_paths.extend(module_paths_)

    root_module_paths: List[str] = _get_root_dir_module_paths()
    module_paths.extend(root_module_paths)
    return module_paths


def _get_root_dir_module_paths() -> List[str]:
    """
    Get root directory module paths.

    Returns
    -------
    module_paths : list of str
        Root directory module paths.
    """
    filr_or_dir_names: List[str] = os.listdir('./')
    module_paths: List[str] = []
    for file_or_dir_name in filr_or_dir_names:
        if not os.path.isfile(file_or_dir_name):
            continue
        if not file_or_dir_name.endswith('.py'):
            continue
        if file_or_dir_name.startswith('__init__'):
            continue
        module_paths.append(f'./{file_or_dir_name}')
    return module_paths


lint_commands: List[LintCommand] = [
    {
        'command':
        'autoflake --in-place --remove-unused-variables '
        '--remove-all-unused-imports -r .',
        'lint_name': 'autoflake',
    }, {
        'command': 'isort --force-single-line-imports .',
        'lint_name': 'isort',
    }, {
        'command':
        'autopep8 --in-place --aggressive --aggressive -r --ignore=E402 .',
        'lint_name': 'autopep8',
    }, {
        'command': FLAKE8_COMMAND,
        'lint_name': 'flake8',
    }, {
        'command': NUMDOCLINT_COMMAND,
        'lint_name': 'numdoclint',
    }, {
        'command': MYPY_COMMAND,
        'lint_name': 'mypy',
    },
]


class _CommandOptions(TypedDict):
    skip_overall_docs_build: bool


def _main() -> None:
    """Entry point of this command.
    """
    from build_docs import HASHED_VALS_DIR_PATH
    options: _CommandOptions = _get_command_options()
    shutil.rmtree('./build/', ignore_errors=True)
    if not options['skip_overall_docs_build']:
        shutil.rmtree(HASHED_VALS_DIR_PATH, ignore_errors=True)
    _remove_tmp_py_module()
    logger.info(msg='Documentation build started.')
    process: sp.Popen = sp.Popen(
        ['python', 'build_docs.py'], stdout=sp.PIPE, stderr=sp.PIPE)
    for lint_command in lint_commands:
        run_lint_command(lint_command=lint_command)
    stdout: bytes
    stderr: bytes
    logger.info(msg='Waiting documentation build completion...')
    stdout, stderr = process.communicate()
    stdout_str: str = stdout.decode()
    stderr_str: str = stderr.decode()
    for string in (stdout_str, stderr_str):
        if 'Traceback' not in string:
            continue
        print(string)
    logger.info(msg='Ended.')


def _get_command_options() -> _CommandOptions:
    """
    Get a command-line options.

    Returns
    -------
    options : _CommandOptions
        Command argument values and options.
    """
    parser: ArgumentParser = ArgumentParser(
        description='Apply each lint to all modules and build documentation.')

    parser.add_argument(
        '-s',
        '--skip_overall_docs_build',
        action='store_true',
        help='If specified, build the overall documentation. If not '
        'specified, only updated document will be built.',
    )
    args: Namespace = parser.parse_args()
    options: _CommandOptions = {
        'skip_overall_docs_build': args.skip_overall_docs_build,
    }
    return options


def _remove_tmp_py_module() -> None:
    """
    Remove temporary Python modules (`tmp_<any_string>.py` file
    will become deletion target).
    """
    file_names: List[str] = os.listdir('./')
    for file_name in file_names:
        if not os.path.isfile(file_name):
            continue
        match: Optional[Match] = re.search(
            pattern=r'tmp_.+\.py$',
            string=file_name)
        if match is None:
            continue
        os.remove(file_name)


def run_command(command: str) -> str:
    """
    Run a specified command.

    Parameters
    ----------
    command : str
        Target command string.

    Returns
    -------
    stdout : str
        Command result stdout.
    """
    complete_process: sp.CompletedProcess = sp.run(
        command, shell=True,
        stdout=sp.PIPE, stderr=sp.STDOUT)
    stdout: str = complete_process.stdout.decode('utf-8')
    return stdout


def run_lint_command(lint_command: LintCommand) -> str:
    """
    Run single lint command.

    Parameters
    ----------
    lint_command : str
        Target lint command settng.

    Returns
    -------
    stdout : str
        Command result stdout.
    """
    print('-' * 20)
    logger.info(msg=f'{lint_command["lint_name"]} command started.')
    stdout: str = run_command(command=lint_command['command'])
    print(stdout)
    return stdout


if __name__ == '__main__':
    _main()
