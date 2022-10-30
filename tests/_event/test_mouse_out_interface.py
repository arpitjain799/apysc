from random import randint
from typing import Any
from typing import Dict

from retrying import retry

import apysc as ap
from apysc._event.mouse_out_interface import MouseOutInterface
from apysc._expression import expression_data_util
from apysc._type.variable_name_mixin import VariableNameMixIn


class _TestMouseOut(MouseOutInterface, VariableNameMixIn):
    def __init__(self) -> None:
        """Test class for MouseOutInterface."""
        self.variable_name = "test_mouse_out"


class TestMouseOutInterface:
    def on_mouse_out_1(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Mouse out handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_mouse_out_2(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Mouse out handler method for testing.

        Parameters
        ----------
        e : MouseEvent
            Created event instance.
        options : dict
            Optional arguments dictionary.
        """

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_mouse_out_handlers_if_not_initialized(self) -> None:
        interface_1: MouseOutInterface = MouseOutInterface()
        interface_1._initialize_mouse_out_handlers_if_not_initialized()
        assert interface_1._mouse_out_handlers == {}

        interface_1._initialize_mouse_out_handlers_if_not_initialized()
        assert interface_1._mouse_out_handlers == {}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_mouseout(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestMouseOut = _TestMouseOut()
        name: str = interface_1.mouseout(
            handler=self.on_mouse_out_1, options={"msg": "Hello!"}
        )
        assert name in interface_1._mouse_out_handlers
        assert interface_1._mouse_out_handlers[name].options == {"msg": "Hello!"}
        expression: str = (
            expression_data_util.get_current_event_handler_scope_expression()
        )
        expected: str = f"function {name}("
        assert expected in expression

        expression = expression_data_util.get_current_expression()
        expected = f"{interface_1.variable_name}.mouseout({name});"
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_unbind_mouseout(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestMouseOut = _TestMouseOut()
        name: str = interface_1.mouseout(handler=self.on_mouse_out_1)
        interface_1.unbind_mouseout(handler=self.on_mouse_out_1)
        assert interface_1._mouse_out_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{interface_1.variable_name}.off"
            f'("{ap.MouseEventType.MOUSEOUT.value}", {name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_unbind_mouseout_all(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestMouseOut = _TestMouseOut()
        interface_1.mouseout(handler=self.on_mouse_out_1)
        interface_1.mouseout(handler=self.on_mouse_out_2)
        interface_1.unbind_mouseout_all()
        assert interface_1._mouse_out_handlers == {}
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{interface_1.variable_name}.off("
            f'"{ap.MouseEventType.MOUSEOUT.value}");'
        )
        assert expected in expression
