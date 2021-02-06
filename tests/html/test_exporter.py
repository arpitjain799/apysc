from apyscript.file import file_util
import os
import shutil
from typing import List

from retrying import retry

from apyscript.html import exporter, html_util
from apyscript.display.stage import Stage
from apyscript.display import stage


@retry(stop_max_attempt_number=5, wait_fixed=300)
def test__export_js_libs() -> None:
    tmp_dir_path: str = '../.tmp_action_py_script_test_exporter/'
    shutil.rmtree(tmp_dir_path, ignore_errors=True)

    saved_js_file_paths: List[str] = exporter._export_js_libs(
        dest_dir_path=tmp_dir_path)
    for saved_js_file_path in saved_js_file_paths:
        assert os.path.isfile(saved_js_file_path)

    expected_file_path: str = os.path.join(
        tmp_dir_path, 'jquery.min.js')
    assert expected_file_path in saved_js_file_paths

    shutil.rmtree(tmp_dir_path, ignore_errors=True)


def test__append_head_to_html_str() -> None:
    html_str: str = '<html>'
    html_str = exporter._append_head_to_html_str(html_str=html_str)

    expected_str: str = '<html>\n<head>\n'
    assert html_str.startswith(expected_str)

    expected_str = '  <meta charset="utf-8">'
    assert expected_str in html_str

    expected_str = \
        '  <script type="text/javascript" src="./jquery.min.js"></script>'
    assert expected_str in html_str

    expected_str = '</head>'
    assert html_str.endswith(expected_str)


@retry(stop_max_attempt_number=5, wait_fixed=300)
def test__append_each_expression_to_html_str() -> None:
    html_str: str = '<html>\n<body>'
    stage: Stage = Stage()
    html_str = exporter._append_each_expression_to_html_str(
        html_str=html_str)
    expected_expresion: str = stage._make_constructor_expression()
    expected_expresion = html_util.append_indent_to_each_line(
        html=expected_expresion, indent_num=1)
    assert expected_expresion in html_str


@retry(stop_max_attempt_number=5, wait_fixed=300)
def test_save_expressions_overall_html() -> None:
    tmp_dir_path: str = '../.tmp_action_py_script_test_exporter/'
    shutil.rmtree(tmp_dir_path, ignore_errors=True)
    stage: Stage = Stage()
    exporter.save_expressions_overall_html(dest_dir_path=tmp_dir_path)
    expected_index_file_path: str = os.path.join(tmp_dir_path, 'index.html')
    assert os.path.isfile(expected_index_file_path)
    html_str: str = file_util.read_txt(file_path=expected_index_file_path)
    assert html_str.startswith('<html>\n<head>')
    assert html_str.endswith('</body>\n</html>')
    expected_expresion: str = stage._make_constructor_expression()
    expected_expresion = html_util.append_indent_to_each_line(
        html=expected_expresion, indent_num=1)
    assert expected_expresion in html_str

    shutil.rmtree(tmp_dir_path, ignore_errors=True)
