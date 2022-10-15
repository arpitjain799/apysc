import re
from random import randint
from typing import Any
from typing import Match
from typing import Optional
from typing import Tuple

import pytest
from retrying import retry

import apysc as ap
from apysc._display.x_mixin import XMixIn
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing import testing_helper
from apysc._type import number_value_interface
from apysc._type.number_value_interface import NumberValueInterface
from apysc._validation import arg_validation_decos


class _TestNumberClass(NumberValueInterface):
    def __init__(
        self,
        *,
        value: number_value_interface._NumType,
        type_name: str,
        variable_name_suffix: str = "",
    ) -> None:
        """
        Test class for number value interface.

        Parameters
        ----------
        value : NumberValueInterface or int or float
            Initial number value.
        type_name : str
            This instance expression's type name (e.g., int, number).
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript's debugging.
        """
        super(_TestNumberClass, self).__init__(
            value=value, type_name=type_name, variable_name_suffix=variable_name_suffix
        )

    @arg_validation_decos.is_num(arg_position_index=1)
    def _set_value_and_skip_expression_appending(
        self, *, value: number_value_interface._NumType
    ) -> None:
        """
        Update value attribute and skip expression appending.

        Parameters
        ----------
        value : NumberValueInterface or int or float
            Any number value to set.
        """
        if isinstance(value, NumberValueInterface):
            value_: Any = value._value
        else:
            value_ = value  # type: ignore
        self._value = value_


class TestNumberValueInterface:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=100, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_1"
        testing_helper.assert_attrs(
            expected_attrs={
                "_initial_value": 100,
                "_value": 100,
                "_type_name": "test_interface",
            },
            any_obj=interface_1,
        )

        interface_2: _TestNumberClass = _TestNumberClass(
            value=interface_1, type_name="test_interface"
        )
        interface_2.variable_name = "test_interface_2"
        testing_helper.assert_attrs(
            expected_attrs={
                "_initial_value": interface_1,
                "_value": 100,
            },
            any_obj=interface_2,
        )

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            callable_=_TestNumberClass,
            value="Hello!",
            type_name="test_interface",
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_value(self) -> None:
        expression_data_util.empty_expression()
        interface: _TestNumberClass = _TestNumberClass(
            value=100, type_name="test_interface"
        )
        interface.variable_name = "test_number_value_interface"
        interface.value = 200
        assert interface.value == 200

        with pytest.raises(ValueError):  # type: ignore
            interface.value = "Hello!"  # type: ignore

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_append_constructor_expression(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestNumberClass = _TestNumberClass(
            value=100, type_name="test_interface"
        )
        interface_1.variable_name = "test_number_value_interface_1"
        interface_1._append_constructor_expression()
        expression: str = expression_data_util.get_current_expression()
        expected: str = "var test_number_value_interface_1 = 100;"
        assert expected in expression

        interface_2: _TestNumberClass = _TestNumberClass(
            value=interface_1, type_name="test_interface"
        )
        interface_2.variable_name = "test_number_value_interface_2"
        interface_2._append_constructor_expression()
        expression = expression_data_util.get_current_expression()
        expected = (
            "var test_number_value_interface_2 = " "test_number_value_interface_1"
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_value_setter_expression(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestNumberClass = _TestNumberClass(
            value=100, type_name="test_interface"
        )
        interface_1.variable_name = "test_number_value_interface_1"
        interface_1.value = 200
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{interface_1.variable_name} = 200;"
        assert expected in expression

        interface_2: _TestNumberClass = _TestNumberClass(
            value=100, type_name="test_interface"
        )
        interface_2.variable_name = "test_number_value_interface_2"
        interface_2.value = interface_1
        expression = expression_data_util.get_current_expression()
        expected = f"{interface_2.variable_name} = {interface_1.variable_name};"
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_type_name(self) -> None:
        interface: _TestNumberClass = _TestNumberClass(
            value=100, type_name="test_interface"
        )
        assert interface.type_name == "test_interface"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___add__(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_1"
        interface_2: NumberValueInterface = interface_1 + 20
        assert interface_2.value == 30
        assert interface_1.variable_name != interface_2.variable_name

        interface_3: NumberValueInterface = interface_1 + interface_2
        assert interface_3.value == 40
        assert interface_3.variable_name != interface_2.variable_name

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__copy(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_0"
        interface_2: NumberValueInterface = interface_1._copy()
        assert interface_1.value == interface_2.value
        assert interface_1.variable_name != interface_2.variable_name
        assert interface_2.variable_name.startswith("test_interface")

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_addition_expression(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_0"
        interface_2: NumberValueInterface = interface_1 + 10
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"var {interface_2.variable_name} = " f"{interface_1.variable_name} + 10;"
        )
        assert expected in expression

        interface_3: NumberValueInterface = interface_1 + interface_2
        expression = expression_data_util.get_current_expression()
        expected = (
            f"var {interface_3.variable_name} = "
            f"{interface_1.variable_name} + {interface_2.variable_name};"
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___sub__(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=20, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_0"
        interface_2: NumberValueInterface = interface_1 - 15
        assert interface_2.value == 5

        interface_3: NumberValueInterface = interface_1 - interface_2
        assert interface_3.value == 15

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_subtraction_expression(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestNumberClass = _TestNumberClass(
            value=20, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_0"
        interface_2: NumberValueInterface = interface_1 - 15
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{interface_2.variable_name} = {interface_1.variable_name} - 15;"
        )
        assert expected in expression

        interface_3: NumberValueInterface = interface_1 - interface_2
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{interface_3.variable_name} = {interface_1.variable_name} "
            f"- {interface_2.variable_name};"
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___mul__(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=20, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_0"
        interface_2: NumberValueInterface = interface_1 * 3
        assert interface_2.value == 60

        interface_3: NumberValueInterface = interface_1 * interface_2
        assert interface_3.value == 1200

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_multiplication_expression(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestNumberClass = _TestNumberClass(
            value=20, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_0"
        interface_2: NumberValueInterface = interface_1 * 3
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{interface_2.variable_name} = {interface_1.variable_name} * 3;"
        )
        assert expected in expression

        interface_3: NumberValueInterface = interface_1 * interface_2
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{interface_3.variable_name} = {interface_1.variable_name}"
            f" * {interface_2.variable_name};"
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___truediv__(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_0"
        interface_2: NumberValueInterface = interface_1 / 4
        assert interface_2.value == 2.5
        assert isinstance(interface_2, ap.Number)

        interface_3: NumberValueInterface = interface_2 / interface_1
        assert interface_3.value == 0.25

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_true_division_expression(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_0"
        interface_2: NumberValueInterface = interface_1 / 4
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{interface_2.variable_name} = {interface_1.variable_name};"
            f"\n{interface_2.variable_name} = {interface_1.variable_name}"
            " / 4;"
        )
        assert expected in expression

        interface_3: NumberValueInterface = interface_2 / interface_1
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{interface_3.variable_name} = {interface_2.variable_name};"
            f"\n{interface_3.variable_name} = {interface_2.variable_name}"
            f" / {interface_1.variable_name};"
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___floordiv__(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_0"
        interface_2: NumberValueInterface = interface_1 // 4
        assert interface_2.value == 2
        assert isinstance(interface_2, ap.Int)

        interface_3: _TestNumberClass = _TestNumberClass(
            value=6, type_name="test_interface"
        )
        interface_3.variable_name = "test_interface_2"
        interface_4: NumberValueInterface = interface_1 // interface_3
        assert interface_4.value == 1

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_floor_division_expression(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_0"
        interface_2: NumberValueInterface = interface_1 // 4
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{interface_2.variable_name} = "
            f"Math.trunc({interface_1.variable_name} / 4);"
        )
        assert expected in expression

        interface_3: NumberValueInterface = interface_1 // interface_2
        expression = expression_data_util.get_current_expression()
        expected = f"{interface_3.variable_name} = {interface_1.variable_name};"
        assert expected in expression
        expected = (
            f"{interface_3.variable_name} = Math.trunc("
            f"{interface_1.variable_name} / {interface_2.variable_name});"
        )
        assert expected in expression

    def _make_x_mixin_instance(self) -> Tuple[XMixIn, str]:
        """
        Make the x interface instance and it's x value variable name.

        Returns
        -------
        x_mixin : XMixIn
            Created x interface instance.
        x_variable_name : str
            Variable name of the x_mixin x attribute.
        """
        x_mixin: XMixIn = XMixIn()
        x_mixin.variable_name = "test_x_mixin"
        x_mixin.x = ap.Int(10)
        x_variable_name: str = x_mixin._x.variable_name
        return x_mixin, x_variable_name

    def _assert_substitution_expression_to_prev_var_exists(
        self, x_mixin: XMixIn, previous_x_variable_name: str
    ) -> None:
        """
        Assert the substitution expression to the previous x
        variable name exists.

        Parameters
        ----------
        x_mixin : XMixIn
            Targe x interface instance.
        previous_x_variable_name : str
            Variable name before a calculation.

        Raises
        ------
        AssertionError
            If the substitution expression does not exist.
        """
        expression = expression_data_util.get_current_expression()
        expected: str = f"{previous_x_variable_name} = {x_mixin._x.variable_name};"
        assert expected in expression

    def _assert_substitution_expression_to_prev_var_not_exist(
        self, x_mixin: XMixIn, previous_x_variable_name: str
    ) -> None:
        """
        Assert the substitution expression to the previous x
        variable name does not exist.

        Parameters
        ----------
        x_mixin : XMixIn
            Targe x interface instance.
        previous_x_variable_name : str
            Variable name before a calculation.

        Raises
        ------
        AssertionError
            If the substitution expression exists.
        """
        expression = expression_data_util.get_current_expression()
        expected: str = f"{previous_x_variable_name} = {x_mixin._x.variable_name};"
        assert expected not in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___iadd__(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_0"
        int_1: ap.Int = ap.Int(5)
        interface_1 += int_1
        assert interface_1.value == 15
        assert interface_1.variable_name == "test_interface_0"

        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                r"test_interface_[0-9]+ = test_interface_0 \+ "
                rf"{int_1.variable_name};"
                r"\ntest_interface_0 = test_interface_[0-9]+;"
            ),
            string=expression,
            flags=re.MULTILINE | re.DOTALL,
        )
        assert match is not None

        expression_data_util.empty_expression()
        x_mixin, previous_variable_name = self._make_x_mixin_instance()
        x_mixin.x += 20
        self._assert_substitution_expression_to_prev_var_exists(
            x_mixin=x_mixin, previous_x_variable_name=previous_variable_name
        )

        expression_data_util.empty_expression()
        x_mixin, previous_variable_name = self._make_x_mixin_instance()
        x: ap.Int = x_mixin.x
        x += 20
        self._assert_substitution_expression_to_prev_var_not_exist(
            x_mixin=x_mixin, previous_x_variable_name=previous_variable_name
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___isub__(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_0"
        interface_1 -= 3
        assert interface_1.value == 7
        assert interface_1.variable_name == "test_interface_0"

        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                r"test_interface_[0-9]+ = test_interface_0 - 3;"
                r"\ntest_interface_0 = test_interface_[0-9]+;"
            ),
            string=expression,
            flags=re.MULTILINE | re.DOTALL,
        )
        assert match is not None

        expression_data_util.empty_expression()
        x_mixin, previous_variable_name = self._make_x_mixin_instance()
        x_mixin.x -= 5
        self._assert_substitution_expression_to_prev_var_exists(
            x_mixin=x_mixin, previous_x_variable_name=previous_variable_name
        )

        expression_data_util.empty_expression()
        x_mixin, previous_variable_name = self._make_x_mixin_instance()
        x: ap.Int = x_mixin.x
        x -= 20
        self._assert_substitution_expression_to_prev_var_not_exist(
            x_mixin=x_mixin, previous_x_variable_name=previous_variable_name
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___imul__(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_0"
        interface_1 *= 3
        assert interface_1.value == 30
        assert interface_1.variable_name == "test_interface_0"

        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                r"test_interface_[0-9]+ = test_interface_0 \* 3;"
                r"\ntest_interface_0 = test_interface_[0-9]+;"
            ),
            string=expression,
            flags=re.MULTILINE | re.DOTALL,
        )
        assert match is not None

        expression_data_util.empty_expression()
        x_mixin, previous_variable_name = self._make_x_mixin_instance()
        x_mixin.x *= 2
        self._assert_substitution_expression_to_prev_var_exists(
            x_mixin=x_mixin, previous_x_variable_name=previous_variable_name
        )

        expression_data_util.empty_expression()
        x_mixin, previous_variable_name = self._make_x_mixin_instance()
        x: ap.Int = x_mixin.x
        x *= 2
        self._assert_substitution_expression_to_prev_var_not_exist(
            x_mixin=x_mixin, previous_x_variable_name=previous_variable_name
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___itruediv__(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_0"
        interface_1 /= 4
        assert interface_1.value == 2.5
        assert interface_1.variable_name == "test_interface_0"

        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                r"var n_[0-9]+ = test_interface_0;"
                r"\nn_[0-9]+ = test_interface_0 / 4;"
            ),
            string=expression,
            flags=re.MULTILINE | re.DOTALL,
        )
        assert match is not None

        expression_data_util.empty_expression()
        x_mixin, previous_variable_name = self._make_x_mixin_instance()
        x_mixin.x /= 2
        self._assert_substitution_expression_to_prev_var_exists(
            x_mixin=x_mixin, previous_x_variable_name=previous_variable_name
        )

        expression_data_util.empty_expression()
        x_mixin, previous_variable_name = self._make_x_mixin_instance()
        x: ap.Int = x_mixin.x
        x /= 2
        self._assert_substitution_expression_to_prev_var_not_exist(
            x_mixin=x_mixin, previous_x_variable_name=previous_variable_name
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___str__(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        assert str(interface_1) == "10"

        del interface_1._value
        assert str(interface_1) == "0"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___eq__(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_0"
        interface_2: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_2.variable_name = "test_interface_1"
        interface_3: _TestNumberClass = _TestNumberClass(
            value=11, type_name="test_interface"
        )
        interface_3.variable_name = "test_interface_3"

        assert interface_1 == 10
        assert interface_1 == interface_2
        assert not interface_1 == 11
        assert not interface_1 == interface_3

        assert isinstance(interface_1 == 10, ap.Boolean)
        assert isinstance(interface_1 == interface_2, ap.Boolean)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___ne__(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_1"
        interface_2: _TestNumberClass = _TestNumberClass(
            value=11, type_name="test_interface"
        )
        interface_2.variable_name = "test_interface_2"
        assert interface_1 != 11
        assert interface_1 != interface_2

        assert isinstance(interface_1 != 11, ap.Boolean)
        assert isinstance(interface_1 != interface_2, ap.Boolean)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___lt__(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_1"
        interface_2: _TestNumberClass = _TestNumberClass(
            value=11, type_name="test_interface"
        )
        interface_2.variable_name = "test_interface_2"
        interface_3: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_3.variable_name = "test_interface_3"

        assert interface_1 < 11
        assert interface_1 < interface_2
        assert not interface_1 < 10
        assert not interface_1 < interface_3
        assert isinstance(interface_1 < 11, ap.Boolean)
        assert isinstance(interface_1 < interface_2, ap.Boolean)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___le__(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_1"
        interface_2: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_2.variable_name = "test_interface_2"
        interface_3: _TestNumberClass = _TestNumberClass(
            value=11, type_name="test_interface"
        )
        interface_3.variable_name = "test_interface_3"
        interface_4: _TestNumberClass = _TestNumberClass(
            value=9, type_name="test_interface"
        )
        interface_4.variable_name = "test_interface_4"

        assert interface_1 <= 10
        assert interface_1 <= 11
        assert interface_1 <= interface_2
        assert interface_1 <= interface_3
        assert not interface_1 <= 9
        assert not interface_1 <= interface_4

        assert isinstance(interface_1 <= 10, ap.Boolean)
        assert isinstance(interface_1 <= interface_2, ap.Boolean)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___gt__(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_1"
        interface_2: _TestNumberClass = _TestNumberClass(
            value=9, type_name="test_interface"
        )
        interface_2.variable_name = "test_interface_2"
        interface_3: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_3.variable_name = "test_interface_3"

        assert interface_1 > 9
        assert interface_1 > interface_2
        assert not interface_1 > 10
        assert not interface_1 > interface_3

        assert isinstance(interface_1 > 9, ap.Boolean)
        assert isinstance(interface_1 > interface_2, ap.Boolean)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___ge__(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_1"
        interface_2: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_2.variable_name = "test_interface_2"
        interface_3: _TestNumberClass = _TestNumberClass(
            value=9, type_name="test_interface"
        )
        interface_3.variable_name = "test_interface_3"
        interface_4: _TestNumberClass = _TestNumberClass(
            value=11, type_name="test_interface"
        )
        interface_4.variable_name = "test_interface_4"

        assert interface_1 >= 10
        assert interface_1 >= 9
        assert interface_1 >= interface_2
        assert interface_1 >= interface_3
        assert not interface_1 >= 11
        assert not interface_1 >= interface_4

        assert isinstance(interface_1 >= 10, ap.Boolean)
        assert isinstance(interface_1 >= interface_2, ap.Boolean)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___int__(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_1"
        integer: int = int(interface_1)
        assert interface_1 == 10
        assert isinstance(integer, int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___float__(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10.5, type_name="test_interface"
        )
        float_val: float = float(interface_1)
        assert float_val == 10.5
        assert isinstance(float_val, float)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10.5, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_1"
        snapshot_name: str = "snapshot_1"
        interface_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface_1._value_snapshots[snapshot_name] == 10.5

        interface_1.value = 20
        interface_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface_1._value_snapshots[snapshot_name] == 10.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10.5, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_1"
        snapshot_name: str = "snapshot_1"
        interface_1._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface_1.value = 20
        interface_1._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface_1.value == 10.5

        interface_1.value = 20
        interface_1._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface_1.value == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_eq_expression(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_1"
        interface_2: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_2.variable_name = "test_interface_2"
        result: ap.Boolean = interface_1 == interface_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{interface_1.variable_name} === {interface_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = interface_1 == 10
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{interface_1.variable_name} === "
                rf"{var_names.INT}\_.+?\;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_ne_expression(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_1"
        interface_2: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_2.variable_name = "test_interface_2"
        result: ap.Boolean = interface_1 != interface_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{interface_1.variable_name} !== "
            f"{interface_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = interface_1 != 20
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{interface_1.variable_name} !== "
                rf"{var_names.INT}\_.+?;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_lt_expression(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_1"
        interface_2: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_2.variable_name = "test_interface_2"
        result: ap.Boolean = interface_1 < interface_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{interface_1.variable_name} < {interface_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = interface_1 < 10
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{interface_1.variable_name} \< "
                rf"{var_names.INT}\_.+;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_le_expression(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_1"
        interface_2: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_2.variable_name = "test_interface_2"
        result: ap.Boolean = interface_1 <= interface_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{interface_1.variable_name} <= {interface_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = interface_1 <= 10
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{interface_1.variable_name} <= "
                rf"{var_names.INT}\_.+;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_gt_expression(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_1"
        interface_2: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_2.variable_name = "test_interface_2"
        result: ap.Boolean = interface_1 > interface_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{interface_1.variable_name} > {interface_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = interface_1 > 10
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{interface_1.variable_name} > "
                rf"{var_names.INT}\_.+;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_ge_expression(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_1"
        interface_2: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_2.variable_name = "test_interface_2"
        result: ap.Boolean = interface_1 >= interface_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = "
            f"{interface_1.variable_name} >= {interface_2.variable_name};"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        result = interface_1 >= 10
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{result.variable_name} = "
                rf"{interface_1.variable_name} >= "
                rf"{var_names.INT}\_.+?;"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__convert_other_val_to_int_or_number(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        converted_val: Any = interface_1._convert_other_val_to_int_or_number(other=10)
        assert isinstance(converted_val, ap.Int)
        assert converted_val == 10

        converted_val = interface_1._convert_other_val_to_int_or_number(other=10.5)
        assert isinstance(converted_val, ap.Number)
        assert converted_val == 10.5

        converted_val = interface_1._convert_other_val_to_int_or_number(other="Hello")
        assert converted_val == "Hello"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_incremental_calc_substitution_expression(self) -> None:
        expression_data_util.empty_expression()
        x_mixin, previous_variable_name = self._make_x_mixin_instance()
        x_mixin.x += 10
        self._assert_substitution_expression_to_prev_var_exists(
            x_mixin=x_mixin, previous_x_variable_name=previous_variable_name
        )
        assert x_mixin._x._incremental_calc_prev_name == ""

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_modulo_expression(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_1"
        interface_2: NumberValueInterface = interface_1 % 10
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{interface_2.variable_name} = " f"{interface_1.variable_name} % 10;"
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___mod__(self) -> None:
        interface_1: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        interface_1.variable_name = "test_interface_1"
        interface_2: NumberValueInterface = interface_1 % 3
        assert interface_2 == 1

        interface_1 = _TestNumberClass(value=10.5, type_name="test_interface")
        interface_1.variable_name = "test_interface_1"
        interface_3: NumberValueInterface = interface_1 % ap.Int(3)
        assert interface_3 == 1.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__create_substitution_expression(self) -> None:
        interface: _TestNumberClass = _TestNumberClass(
            value=10, type_name="test_interface"
        )
        expression: str = interface._create_initial_substitution_expression()
        assert expression == f"{interface.variable_name} = 10;"

        int_val: ap.Int = ap.Int(10)
        interface = _TestNumberClass(value=int_val, type_name="test_interface")
        expression = interface._create_initial_substitution_expression()
        assert expression == f"{interface.variable_name} = {int_val.variable_name};"
