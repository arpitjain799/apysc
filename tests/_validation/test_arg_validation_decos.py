from random import randint
from typing import Any
from typing import Callable
from typing import Union

from retrying import retry

import apysc as ap
from apysc._testing.testing_helper import assert_raises
from apysc._validation import arg_validation_decos


class _TestClass1:

    @arg_validation_decos.not_empty_string(arg_position_index=1)
    def _test_method_1(self, *, a: str) -> None:
        ...

    @arg_validation_decos.not_empty_string(arg_position_index=1)
    def _test_method_2(self, a: str) -> None:
        ...


@arg_validation_decos.handler_args_num(arg_position_index=0)
def _test_func_2(*, handler: Callable) -> None:
    ...


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_not_empty_string() -> None:

    @arg_validation_decos.not_empty_string(arg_position_index=0)
    def _test_func(a: str) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        func_or_method=_test_func,
        kwargs={'a': ''},
        match='An argument\'s string value must not be empty.')
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=_test_func,
        kwargs={'a': 10})

    _test_func('Hello')
    _test_func(a='Hello')

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
        arg_name='a',
        default_val=None)
    assert value == 'Test message 1'

    value = arg_validation_decos._extract_arg_value(
        args=['Test message 2'],
        kwargs={},
        arg_position_index=0,
        arg_name='a',
        default_val=None)
    assert value == 'Test message 2'

    value = arg_validation_decos._extract_arg_value(
        args=[],
        kwargs={},
        arg_position_index=0,
        arg_name='a',
        default_val=None)
    assert value is None

    value = arg_validation_decos._extract_arg_value(
        args=[],
        kwargs={},
        arg_position_index=0,
        arg_name='a',
        default_val='Hello!')
    assert value == 'Hello!'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_handler_args_num() -> None:

    def _test_handler_1(e: ap.Event) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        func_or_method=_test_func_2,
        kwargs={'handler': _test_handler_1},
        match='Target callable name: _test_func_2',
    )

    def _test_handler_2(e: ap.Event, options: dict) -> None:
        ...

    _test_func_2(handler=_test_handler_2)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_handler_options_type() -> None:

    @arg_validation_decos.handler_options_type(arg_position_index=0)
    def _test_func(*, options: dict) -> None:
        ...

    assert_raises(
        expected_error_class=TypeError,
        func_or_method=_test_func,
        kwargs={'options': 10})

    _test_func(options={'msg': 'Hello!'})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_arg_name_by_index() -> None:

    def _test_func(*, a: int, b: str) -> None:
        ...

    arg_name: str = arg_validation_decos._get_arg_name_by_index(
        callable_=_test_func, arg_position_index=0)
    assert arg_name == 'a'
    arg_name = arg_validation_decos._get_arg_name_by_index(
        callable_=_test_func, arg_position_index=1)
    assert arg_name == 'b'

    def _test_func_2(a: int, b: str) -> None:
        ...

    arg_name = arg_validation_decos._get_arg_name_by_index(
        callable_=_test_func_2, arg_position_index=0)
    assert arg_name == 'a'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_callable_and_arg_names_msg() -> None:

    def _test_func(a: int) -> None:
        ...

    callable_and_arg_names_msg: str = arg_validation_decos.\
        _get_callable_and_arg_names_msg(
            callable_=_test_func, arg_name='a')
    assert callable_and_arg_names_msg == (
        'Target callable name: _test_func'
        '\nTarget argument name: a'
    )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_integer() -> None:

    @arg_validation_decos.is_integer(arg_position_index=1)
    def _test_func(*, a: str, b: Union[int, ap.Int]) -> None:
        ...

    assert_raises(
        expected_error_class=ValueError,
        func_or_method=_test_func,
        kwargs={'a': 'Hello!', 'b': 'World!'})

    _test_func(a='Hello!', b=10)
    _test_func(a='Hello!', b=ap.Int(10))


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_num_is_gt_zero() -> None:

    @arg_validation_decos.num_is_gt_zero(arg_position_index=0)
    def _test_func(*, a: Union[int, ap.Int]) -> None:
        ...

    _test_func(a=1)
    _test_func(a=ap.Int(1))
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=_test_func,
        kwargs={'a': 0})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_easing() -> None:

    @arg_validation_decos.is_easing(arg_position_index=0)
    def _test_func(*, easing: ap.Easing) -> None:
        ...

    _test_func(easing=ap.Easing.EASE_IN_SINE)
    _test_func(easing=ap.Easing.EASE_OUT_QUAD)
    assert_raises(
        expected_error_class=TypeError,
        func_or_method=_test_func,
        kwargs={'easing': 10},
        match=r"A specified easing argument\'s type is not the ap\.Easing\: ")


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_default_val_by_arg_name() -> None:

    def _test_func(*, a: int, b: str = 'Hello!') -> None:
        ...

    default_val: Any = arg_validation_decos._get_default_val_by_arg_name(
        callable_=_test_func, arg_name='a')
    assert default_val is None

    default_val = arg_validation_decos._get_default_val_by_arg_name(
        callable_=_test_func, arg_name='b')
    assert default_val == 'Hello!'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_num() -> None:

    @arg_validation_decos.is_num(arg_position_index=0)
    def _test_func_1(
            *, a: Union[int, float, ap.Int, ap.Number]) -> None:
        ...

    _test_func_1(a=1.5)
    _test_func_1(a=1)
    _test_func_1(a=ap.Int(1))
    _test_func_1(a=ap.Number(1.5))

    assert_raises(
        expected_error_class=ValueError,
        func_or_method=_test_func_1,
        kwargs={'a': 'Hello!'})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_hex_color_code_format() -> None:

    @arg_validation_decos.is_hex_color_code_format(arg_position_index=0)
    def _test_func(*, a: str) -> None:
        ...

    _test_func(a='#a')
    _test_func(a='0af')
    _test_func(a='#0af')
    _test_func(a='#00aaff')

    assert_raises(
        expected_error_class=ValueError,
        func_or_method=_test_func,
        kwargs={
            'a': 'Hello!',
        })


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_num_is_gte_zero() -> None:

    @arg_validation_decos.num_is_gte_zero(arg_position_index=0)
    def _test_func(*, a: int) -> None:
        ...

    _test_func(a=0)
    _test_func(a=1)
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=_test_func,
        kwargs={'a': -1})
