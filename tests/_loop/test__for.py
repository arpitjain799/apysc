import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import indent_num
from apysc._expression import last_scope
from apysc._expression.indent_num import Indent
from apysc._expression.last_scope import LastScope
from apysc._loop import loop_count
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings


class TestFor:
    @apply_test_settings()
    def test___init__(self) -> None:
        arr: ap.Array = ap.Array([1, 2, 3])
        for_: ap.For = ap.For(
            arr_or_dict=arr, locals_={"value_1": 1}, globals_={"value_2": 2}
        )
        testing_helper.assert_attrs(
            expected_attrs={
                "_arr_or_dict": arr,
                "_locals": {"value_1": 1},
                "_globals": {"value_2": 2},
            },
            any_obj=for_,
        )
        assert isinstance(for_._indent, Indent)

        for_ = ap.For(arr)
        testing_helper.assert_attrs(
            expected_attrs={
                "_locals": {},
                "_globals": {},
            },
            any_obj=for_,
        )

    @apply_test_settings()
    def test__append_arr_enter_expression(self) -> None:
        expression_data_util.empty_expression()
        arr: ap.Array = ap.Array([1, 2, 3])
        with ap.For(arr, locals_=locals(), globals_=globals()) as i:
            pass
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"var length = {arr.variable_name}.length;"
        assert expected in expression
        i_name: str = i.variable_name
        expected = f"for ({i_name} = 0; {i_name} < length; {i_name}++) {{"
        assert expected in expression

    @apply_test_settings()
    def test___enter__(self) -> None:
        indent_num.reset()
        arr: ap.Array = ap.Array([1, 2, 3])
        with ap.For(arr, locals_=locals(), globals_=globals()) as i:
            current_indent_num: int = indent_num.get_current_indent_num()
            assert current_indent_num == 1
            current_loop_count: int = loop_count.get_current_loop_count()
            assert current_loop_count == 1
        assert isinstance(i, ap.Int)

        dict_val: ap.Dictionary = ap.Dictionary({"a": 10})
        with ap.For(dict_val) as key:
            pass
        assert isinstance(key, ap.String)
        assert key == "a"

        dict_val = ap.Dictionary({})
        with ap.For(dict_val) as key:
            pass
        assert isinstance(key, ap.String)
        assert key == ""

    @apply_test_settings()
    def test___exit__(self) -> None:
        expression_data_util.empty_expression()
        indent_num.reset()
        int_1: ap.Int = ap.Int(10)
        arr: ap.Array = ap.Array([1, 2, 3])
        with ap.For(arr, locals_=locals(), globals_=globals()) as i:
            int_1.value = 20
        assert int_1.value == 10
        current_indent_num: int = indent_num.get_current_indent_num()
        assert current_indent_num == 0
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"  {int_1.variable_name} = 20;" "\n}"
        assert expected in expression
        assert last_scope.get_last_scope() == LastScope.FOR
        current_loop_count: int = loop_count.get_current_loop_count()
        assert current_loop_count == 0

    @apply_test_settings()
    def test__append_dict_enter_expression(self) -> None:
        expression_data_util.empty_expression()
        dict_1: ap.Dictionary = ap.Dictionary({"a": 10})
        with ap.For[ap.String](dict_1) as key:
            pass
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"for (var {key.variable_name} in {dict_1.variable_name}) {{"
        assert expected in expression

    @apply_test_settings()
    def test__validate_arr_or_dict_val_type(self) -> None:
        ap.For(ap.Array([0]))
        ap.For(ap.Dictionary({"a": 10}))
        testing_helper.assert_raises(
            expected_error_class=TypeError,
            callable_=ap.For,
            match="Specified value type is neither Array nor Dictionary: ",
            arr_or_dict="Hello!",
        )
