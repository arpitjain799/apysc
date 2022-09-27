from random import randint
from typing import Any
from typing import Dict

from retrying import retry

import apysc as ap
from apysc._event.click_interface import ClickInterface
from apysc._event.handler import get_handler_name
from apysc._expression import expression_data_util
from apysc._testing import testing_helper
from apysc._type.variable_name_interface import VariableNameInterface


class _TestClickInterface(ClickInterface, VariableNameInterface):
    def __init__(self) -> None:
        """
        Test class for ClickInterface.
        """
        self.variable_name = "test_click_interface_1"


class TestClickInterface:
    def on_click_1(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Click handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_click_2(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Click handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_click(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestClickInterface = _TestClickInterface()
        name: str = interface_1.click(handler=self.on_click_1)
        assert (
            interface_1._click_handlers[name].handler == self.on_click_1
        )
        assert interface_1._click_handlers[name].options == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{interface_1.variable_name}.click({name});"
        assert expected in expression

        interface_2: _TestClickInterface = _TestClickInterface()
        name = interface_2.click(handler=self.on_click_1, options={"a": 10})
        assert interface_2._click_handlers[name].options == {"a": 10}

        interface_3: ClickInterface = ClickInterface()
        testing_helper.assert_raises(
            expected_error_class=TypeError,
            callable_=interface_3.click,
            handler=self.on_click_1,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_click_handlers_if_not_initialized(self) -> None:
        interface_1: ClickInterface = ClickInterface()
        interface_1._initialize_click_handlers_if_not_initialized()
        assert interface_1._click_handlers == {}
        interface_1._initialize_click_handlers_if_not_initialized()
        assert interface_1._click_handlers == {}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_unbind_click(self) -> None:
        expression_data_util.empty_expression()
        interface_1: ClickInterface = ClickInterface()
        testing_helper.assert_raises(
            expected_error_class=TypeError,
            callable_=interface_1.unbind_click,
            handler=self.on_click_1,
        )

        interface_2: _TestClickInterface = _TestClickInterface()
        interface_2.click(handler=self.on_click_1)
        interface_2.unbind_click(handler=self.on_click_1)
        assert not interface_2._click_handlers
        handler_name: str = get_handler_name(
            handler=self.on_click_1, instance=interface_2
        )
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{interface_2.variable_name}.off("
            f'"{ap.MouseEventType.CLICK.value}", {handler_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_unbind_click_all(self) -> None:
        expression_data_util.empty_expression
        interface_1: ClickInterface = ClickInterface()
        testing_helper.assert_raises(
            expected_error_class=TypeError, callable_=interface_1.unbind_click_all
        )

        interface_2: _TestClickInterface = _TestClickInterface()
        interface_2.click(handler=self.on_click_1)
        interface_2.click(handler=self.on_click_2)
        interface_2.unbind_click_all()
        assert interface_2._click_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{interface_2.variable_name}.off(" f'"{ap.MouseEventType.CLICK.value}");'
        )
        assert expected in expression
