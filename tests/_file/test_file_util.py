import os
import shutil
from random import randint
from typing import List

from retrying import retry

from apysc._file import file_util
from apysc._testing import testing_helper


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_empty_directory() -> None:
    tmp_dir_path: str = '../.tmp_apysc/'
    os.makedirs(tmp_dir_path, exist_ok=True)
    test_file_path: str = os.path.join(tmp_dir_path, 'test.txt')
    testing_helper.make_blank_file(file_path=test_file_path)
    file_util.empty_directory(directory_path=tmp_dir_path)
    assert os.path.isdir(tmp_dir_path)
    assert len(os.listdir(tmp_dir_path)) == 0

    shutil.rmtree(tmp_dir_path, ignore_errors=True)
    file_util.empty_directory(directory_path=tmp_dir_path)
    assert os.path.isdir(tmp_dir_path)

    shutil.rmtree(tmp_dir_path, ignore_errors=True)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_read_txt() -> None:
    tmp_file_path: str = '../tmp_apysc_test_file_util.txt'
    with open(tmp_file_path, 'w') as f:
        f.write('To be, or not to be, that is the question.')
    txt: str = file_util.read_txt(file_path=tmp_file_path)
    assert txt == 'To be, or not to be, that is the question.'
    os.remove(tmp_file_path)

    with open(tmp_file_path, 'w', encoding='cp932') as f:
        f.write('猫')
    testing_helper.assert_raises(
        expected_error_class=Exception,
        callable_=file_util.read_txt,
        file_path=tmp_file_path)
    os.remove(tmp_file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_save_plain_txt() -> None:
    tmp_file_path: str = '../tmp_apysc_test_file_util.txt'
    file_util.save_plain_txt(
        txt='To be, or not to be, that is the question.',
        file_path=tmp_file_path)
    txt: str = file_util.read_txt(file_path=tmp_file_path)
    assert txt == 'To be, or not to be, that is the question.'
    os.remove(tmp_file_path)

    tmp_dir_path: str = '../tmp_apysc_test_file_util/'
    tmp_file_path = os.path.join(tmp_dir_path, 'test.txt')
    shutil.rmtree(tmp_dir_path, ignore_errors=True)
    file_util.save_plain_txt(
        txt='To be, or not to be, that is the question.',
        file_path=tmp_file_path)
    assert os.path.isfile(tmp_file_path)
    shutil.rmtree(tmp_dir_path, ignore_errors=True)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_remove_file_if_exists() -> None:
    tmp_file_path: str = '../tmp_apysc_test_file_util.txt'
    file_util.save_plain_txt(
        txt='To be, or not to be, that is the question.',
        file_path=tmp_file_path)
    file_util.remove_file_if_exists(file_path=tmp_file_path)
    assert not os.path.exists(tmp_file_path)

    file_util.remove_file_if_exists(file_path=tmp_file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_abs_module_dir_path() -> None:
    abs_module_dir_path: str = file_util.get_abs_module_dir_path(
        module=file_util)
    assert abs_module_dir_path.endswith('/apysc/_file/')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_abs_directory_path_from_file_path() -> None:
    dir_path: str = file_util.get_abs_directory_path_from_file_path(
        file_path='any/dir/path.txt')
    assert dir_path == 'any/dir/'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_append_plain_txt() -> None:
    tmp_file_path: str = '../tmp_test_file_util.txt'
    file_util.remove_file_if_exists(file_path=tmp_file_path)
    file_util.append_plain_txt(txt='Hello ', file_path=tmp_file_path)
    file_util.append_plain_txt(txt='World!', file_path=tmp_file_path)
    txt: str = file_util.read_txt(file_path=tmp_file_path)
    assert txt == 'Hello World!'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_specified_ext_file_paths_recursively() -> None:
    file_paths: List[str] = file_util.get_specified_ext_file_paths_recursively(
        extension='md', dir_path='./docs_src/')
    assert './docs_src/source/index.md' in file_paths
    assert './docs_src/source/quick_start.md' in file_paths
    assert './docs_src/source/conf.py' not in file_paths


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_count_files_recursively() -> None:
    tmp_dir_path: str = 'tmp/tmp_test_file_util/'
    shutil.rmtree(tmp_dir_path, ignore_errors=True)
    count: int = file_util.count_files_recursively(dir_path=tmp_dir_path)
    assert count == 0
    os.makedirs(tmp_dir_path, exist_ok=True)

    tmp_subdir_path: str = os.path.join(tmp_dir_path, 'subdir/')
    os.makedirs(tmp_subdir_path, exist_ok=True)
    tmp_file_path_1: str = os.path.join(tmp_dir_path, 'test_1.txt')
    tmp_file_path_2: str = os.path.join(tmp_dir_path, 'test_2.txt')
    tmp_file_path_3: str = os.path.join(tmp_subdir_path, 'test_1.txt')
    for tmp_file_path in (tmp_file_path_1, tmp_file_path_2, tmp_file_path_3):
        with open(tmp_file_path, 'w') as f:
            f.write('')
    count = file_util.count_files_recursively(dir_path=tmp_dir_path)
    assert count == 3
    shutil.rmtree(tmp_dir_path, ignore_errors=True)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_delete_file_if_exists() -> None:
    os.makedirs('./tmp/', exist_ok=True)
    test_file_path: str = './tmp/test_file.txt'

    is_deleted: bool = file_util.delete_file_if_exists(
        file_path=test_file_path)
    assert not is_deleted

    file_util.save_plain_txt(txt='', file_path=test_file_path)
    is_deleted = file_util.delete_file_if_exists(
        file_path=test_file_path)
    assert is_deleted
    assert not os.path.exists(test_file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__has_excluding_prefix() -> None:
    result: bool = file_util._has_excluding_prefix(
        file_name='jp_sprite.md',
        excluding_file_names_prefix_list=None)
    assert not result

    result = file_util._has_excluding_prefix(
        file_name='jp_sprite.md',
        excluding_file_names_prefix_list=['test_prefix', 'jp_'])
    assert result

    result = file_util._has_excluding_prefix(
        file_name='jp_sprite.md',
        excluding_file_names_prefix_list=['test_prefix'])
    assert not result
