from random import randint
from typing import Any, Callable

from retrying import retry

from apysc._testing.testing_helper import assert_raises
from apysc._validation import arg_validation_decos
import apysc as ap


@arg_validation_decos.not_empty_string(
    arg_position_index=0, arg_name='a')
def _test_func_1(a: str) -> None:
    ...


class _TestClass1:

    @arg_validation_decos.not_empty_string(
        arg_position_index=2, arg_name='a')
    def _test_method_1(self, *, a: str) -> None:
        ...

    @arg_validation_decos.not_empty_string(
        arg_position_index=1, arg_name='a')
    def _test_method_2(self, a: str) -> None:
        ...


@arg_validation_decos.handler_args_num(
    arg_position_index=0, arg_name='handler')
def _test_func_2(*, handler: Callable) -> None:
    ...


@arg_validation_decos.handler_args_num(
    arg_position_index=0, arg_name='handler')
def _test_func_3() -> None:
    ...


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_not_empty_string() -> None:
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=_test_func_1,
        kwargs={'a': ''},
        match='An argument\'s string value must not be empty.')
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=_test_func_1,
        kwargs={'a': 10})

    _test_func_1('Hello')
    _test_func_1(a='Hello')

    test_instance: _TestClass1 = _TestClass1()
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=test_instance._test_method_1,
        kwargs={'a': ''},
        match='An argument\'s string value must not be empty.')
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=test_instance._test_method_2,
        kwargs={'a': ''},
        match='An argument\'s string value must not be empty.')

    test_instance._test_method_1(a='Hello')
    test_instance._test_method_2(a='Hello')
    test_instance._test_method_2('Hello')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__extract_arg_value() -> None:
    value: Any = arg_validation_decos._extract_arg_value(
        args=[],
        kwargs={'a': 'Test message 1'},
        arg_position_index=0,
        arg_name='a')
    assert value == 'Test message 1'

    value = arg_validation_decos._extract_arg_value(
        args=['Test message 2'],
        kwargs={},
        arg_position_index=0,
        arg_name='a')
    assert value == 'Test message 2'

    value = arg_validation_decos._extract_arg_value(
        args=[],
        kwargs={},
        arg_position_index=0,
        arg_name='a')
    assert value is None


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_handler_args_num() -> None:

    def _test_handler_1(e: ap.Event) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        func_or_method=_test_func_2,
        kwargs={'handler': _test_handler_1},
        match='Target Callable name: _test_func_2',
    )

    _test_func_3()

    def _test_handler_2(e: ap.Event, options: dict) -> None:
        ...

    _test_func_2(handler=_test_handler_2)
