import os
from random import randint
from typing import Any, List

from retrying import retry

from apysc._string import docstring_util
from apysc._file import file_util
from apysc._display.sprite import Sprite
from apysc._display import sprite


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_docstring_path_comment_matches() -> None:
    matches: List[str] = docstring_util._get_docstring_path_comment_matches(
        md_txt=(
            '# Test title'
            '\n<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->'
            '\n## Sub heading'
            '\n<!-- Docstring:apysc._display.sprite.Sprite.add_child-->'
        ))
    assert matches == [
        '<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->',
        '<!-- Docstring:apysc._display.sprite.Sprite.add_child-->',
    ]


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__extract_docstring_path_specification_comment_from_line() -> None:
    docstring_path_specification_comment: str = docstring_util.\
        _extract_docstring_path_specification_comment_from_line(
            line='<!-- Docstring: apysc._display.sprite.Sprite.add_child -->',
            matches=[
                '<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->',
                '<!-- Docstring: apysc._display.sprite.Sprite.add_child -->',
            ])
    assert (
        docstring_path_specification_comment ==
        '<!-- Docstring: apysc._display.sprite.Sprite.add_child -->')

    docstring_path_specification_comment = docstring_util.\
        _extract_docstring_path_specification_comment_from_line(
            line='## Test sub heading',
            matches=[
                '<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->',
                '<!-- Docstring: apysc._display.sprite.Sprite.add_child -->',
            ])
    assert docstring_path_specification_comment == ''


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__remove_replaced_docstring_section_from_md_txt() -> None:
    md_txt: str = (
        '# Test title'
        '\n\nLorem ipsum dolor sit amet.'
        '\n\n## Sub heading 1'
        '\n\n<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->'
        '\n\n**Parameters**'
        '\n\n- a: str'
        '\n\n## Sub heading 2'
        '\n\nLorem ipsum dolor sit amet.'
        '\n\n## Sub heading 3'
        '\n\n<!-- Docstring: apysc._display.sprite.Sprite.add_child -->'
        '\n\n**Parameters**'
        '\n\n- b: str'
        '\n\n## Sub heading 4'
        '\n\nLorem ipsum dolor sit amet.'
    )
    md_txt = docstring_util._remove_replaced_docstring_section_from_md_txt(
        md_txt=md_txt,
        matches=[
            '<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->',
            '<!-- Docstring: apysc._display.sprite.Sprite.add_child -->',
        ])
    expected: str = (
        '# Test title'
        '\n\nLorem ipsum dolor sit amet.'
        '\n\n## Sub heading 1'
        '\n\n<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->'
        '\n\n## Sub heading 2'
        '\n\nLorem ipsum dolor sit amet.'
        '\n\n## Sub heading 3'
        '\n\n<!-- Docstring: apysc._display.sprite.Sprite.add_child -->'
        '\n\n## Sub heading 4'
        '\n\nLorem ipsum dolor sit amet.'
    )
    assert md_txt == expected


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_reset_replaced_docstring_section() -> None:
    tmp_md_file_path: str = './tmp/test_docstring_util_1.md'
    os.makedirs('./tmp/', exist_ok=True)
    file_util.remove_file_if_exists(file_path=tmp_md_file_path)

    with open(tmp_md_file_path, 'w') as f:
        f.write(
            '# Test title'
            '\n\nLorem ipsum dolor sit amet.'
        )
    is_executed = docstring_util.reset_replaced_docstring_section(
        md_file_path=tmp_md_file_path)
    assert not is_executed

    with open(tmp_md_file_path, 'w') as f:
        f.write(
            '# Test title'
            '\n\nLorem ipsum dolor sit amet.'
            '\n\n## Sub heading 1'
            '\n\n<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->'
            '\n\n**Parameters**'
            '\n\n- a: str'
            '\n\n## Sub heading 2'
            '\n\nLorem ipsum dolor sit amet.'
            '\n\n## Sub heading 3'
            '\n\n<!-- Docstring: apysc._display.sprite.Sprite.add_child -->'
            '\n\n**Parameters**'
            '\n\n- b: str'
            '\n\n## Sub heading 4'
            '\n\nLorem ipsum dolor sit amet.'
        )
    is_executed = docstring_util.reset_replaced_docstring_section(
        md_file_path=tmp_md_file_path)
    assert is_executed
    saved_md_txt: str = file_util.read_txt(file_path=tmp_md_file_path)
    expected: str = (
        '# Test title'
        '\n\nLorem ipsum dolor sit amet.'
        '\n\n## Sub heading 1'
        '\n\n<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->'
        '\n\n## Sub heading 2'
        '\n\nLorem ipsum dolor sit amet.'
        '\n\n## Sub heading 3'
        '\n\n<!-- Docstring: apysc._display.sprite.Sprite.add_child -->'
        '\n\n## Sub heading 4'
        '\n\nLorem ipsum dolor sit amet.'
    )
    assert saved_md_txt == expected

    file_util.remove_file_if_exists(file_path=tmp_md_file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__extract_path_from_docstring_comment() -> None:
    path: str = docstring_util._extract_path_from_docstring_comment(
        docstring_path_comment='# Test title')
    assert path == ''

    path = docstring_util._extract_path_from_docstring_comment(
        docstring_path_comment=(
            '<!-- Docstring: apysc._display.sprite.Sprite.add_child -->'))
    assert path == 'apysc._display.sprite.Sprite.add_child'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__extract_package_path_and_callable_name_from_path() -> None:
    module_or_class_package_path: str
    callable_name: str
    module_or_class_package_path, callable_name = \
        docstring_util._extract_package_path_and_callable_name_from_path(
            docstring_path_comment='# Test title')
    assert module_or_class_package_path == ''
    assert callable_name == ''

    module_or_class_package_path, callable_name = \
        docstring_util._extract_package_path_and_callable_name_from_path(
            docstring_path_comment=(
                '<!-- Docstring: apysc._display.sprite.Sprite.add_child -->'))
    assert module_or_class_package_path == 'apysc._display.sprite.Sprite'
    assert callable_name == 'add_child'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__is_section_line() -> None:
    result: bool = docstring_util._is_section_line(
        line='    Parameters')
    assert result

    result = docstring_util._is_section_line(
        line='        Parameters')
    assert result

    result = docstring_util._is_section_line(
        line='    Returns')
    assert result

    result = docstring_util._is_section_line(
        line='Test function.')
    assert not result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__extract_summary_from_docstring() -> None:
    docstring: str = (
        '    Lorem ipsum dolor sit amet, consectetur adipiscing'
        '\n    elit, sed do eiusmod tempor incididunt ut.'
        '\n    Parameters'
        '\n    ----------'
        '\n    a : int'
    )
    summary: str = docstring_util._extract_summary_from_docstring(
        docstring=docstring)
    assert summary == (
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
        'sed do eiusmod tempor incididunt ut.'
    )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__is_parameters_section_pattern_line() -> None:
    result: bool = docstring_util._is_parameters_section_pattern_line(
        line='    Parameters')
    assert result

    result = docstring_util._is_parameters_section_pattern_line(
        line='    a : str')
    assert not result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__is_hyphens_line() -> None:
    line: str = '    Parameters'
    result: bool = docstring_util._is_hyphens_line(line=line)
    assert not result

    line = '    ----------'
    result = docstring_util._is_hyphens_line(line=line)
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_value_name_and_type_from_line() -> None:
    value_name: str
    type_name: str
    value_name, type_name = docstring_util._get_value_name_and_type_from_line(
        line='    Lorem ipsum dolor sit')
    assert value_name == ''
    assert type_name == ''

    value_name, type_name = docstring_util._get_value_name_and_type_from_line(
        line='    any_value : int')
    assert value_name == 'any_value'
    assert type_name == 'int'
