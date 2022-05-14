import os
from random import randint
from typing import List

from retrying import retry
from apysc._file import file_util

from scripts import run_test_projects_e2e_testing
from apysc._testing.testing_helper import assert_raises


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_target_test_project_main_module_paths() -> None:
    main_module_paths: List[str] = run_test_projects_e2e_testing.\
        _get_target_test_project_main_module_paths(
            alphabets_group=['a', 'b'])
    expected_paths: List[str] = [
        './test_projects/AnimationXInterface/main.py',
        './test_projects/Boolean/main.py',
    ]
    for expected_path in expected_paths:
        assert expected_path in main_module_paths

    unexpected_paths: List[str] = [
        './test_projects/ClickInterface/main.py',
    ]
    for unexpected_path in unexpected_paths:
        assert unexpected_path not in main_module_paths


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__run_test_project_command() -> None:
    run_test_projects_e2e_testing._run_test_project_command(
        main_module_path='./test_projects/AnimationXInterface/main.py')

    os.makedirs('./tmp/', exist_ok=True)
    file_util.save_plain_txt(
        txt='',
        file_path='./tmp/__init__')
    tmp_module_path: str = './tmp/test_run_test_projects_e2e_testing.py'
    file_util.save_plain_txt(
        txt="raise Exception('Test error!')",
        file_path=tmp_module_path)
    assert_raises(
        expected_error_class=Exception,
        func_or_method=run_test_projects_e2e_testing.
        _run_test_project_command,
        kwargs={'main_module_path': tmp_module_path})

    file_util.delete_file_if_exists(file_path=tmp_module_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_index_file_path() -> None:
    index_file_path: str = run_test_projects_e2e_testing._get_index_file_path(
        main_module_path='./test_projects/AnimationXInterface/'
        'main.py')
    assert index_file_path == \
        './test_projects/AnimationXInterface/test_output/index.html'
