"""The implementation of manipulating HTL and js expression files.

Mainly following interfaces are defined:

- empty_expression_dir : Remove expression directory
    (EXPRESSION_ROOT_DIR) to initialize.
- append_js_expression : Append js expression to file.
- wrap_by_script_tag_and_append_expression : Wrap an expression
    string by script tags and append it's expression to file.
- get_current_expression : Get current expression string.
- remove_expression_file : Remove expression file.
"""

import os
from typing import List

EXPRESSION_ROOT_DIR: str = '../.apysc_expression/'
EXPRESSION_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'expression.txt')
INDENT_NUM_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'indent_num.txt')
LAST_SCOPE_FILE_PATH: str = os.path.join(
    EXPRESSION_ROOT_DIR, 'last_scope.txt')


def empty_expression_dir() -> None:
    """
    Remove expression directory (EXPRESSION_ROOT_DIR) to initialize.
    """
    from apysc.file import file_util
    file_util.empty_directory(directory_path=EXPRESSION_ROOT_DIR)


def append_js_expression(expression: str) -> None:
    """
    Append js expression to file.

    Parameters
    ----------
    expression : str
        JavaScript Expression string.
    """
    from apysc.expression import indent_num
    from apysc.expression import last_scope
    from apysc.file import file_util
    from apysc.string import indent_util
    current_indent_num: int = indent_num.get_current_indent_num()
    expression = indent_util.append_spaces_to_expression(
        expression=expression, indent_num=current_indent_num)
    dir_path: str = file_util.get_abs_directory_path_from_file_path(
        file_path=EXPRESSION_FILE_PATH)
    os.makedirs(dir_path, exist_ok=True)
    file_util.append_plain_txt(
        txt=f'{expression}\n', file_path=EXPRESSION_FILE_PATH)
    last_scope.set_last_scope(value=last_scope.LastScope.NORMAL)


def wrap_by_script_tag_and_append_expression(expression: str) -> None:
    """
    Wrap an expression string by script tags and append it's
    expression to file (helper function of `append_js_expression`).

    Parameters
    ----------
    expression : str
        HTML and js Expression string.
    """
    from apysc.html import html_util
    expression = html_util.wrap_expression_by_script_tag(
        expression=expression)
    append_js_expression(expression=expression)


def get_current_expression() -> str:
    """
    Get current expression's string from file.

    Returns
    -------
    current_expression : str
        Current expression's string.
    """
    from apysc.file import file_util
    if not os.path.isfile(EXPRESSION_FILE_PATH):
        return ''
    current_expression: str = file_util.read_txt(
        file_path=EXPRESSION_FILE_PATH)
    current_expression = current_expression.strip()
    return current_expression


def remove_expression_file() -> None:
    """
    Remove expression file.
    """
    from apysc.file import file_util
    file_util.remove_file_if_exists(file_path=EXPRESSION_FILE_PATH)
