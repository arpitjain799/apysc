from random import randint
from typing import Any
from typing import Dict

from retrying import retry

from apysc._event.click_mixin import ClickMixIn
from apysc._expression import expression_data_util
from apysc._type.variable_name_mixin import VariableNameMixIn
import apysc as ap


class _TestClickMixIn(ClickMixIn, VariableNameMixIn):
    def __init__(self) -> None:
        """MixIn for testing."""
        self.variable_name = "test_click_mixin"


class TestMouseEventBindingExpressionMixin:
    def on_click_1(self, e: ap.MouseEvent, options: Dict[str, Any]) -> None:
        """
        Test handler method.

        Parameters
        ----------
        e : MouseEvent
            Event instance.
        options : dict
            Optional arguments dictionary.
        """

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_mouse_event_binding_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestClickMixIn = _TestClickMixIn()
        name: str = mixin_1.click(handler=self.on_click_1)
        mixin_1._append_mouse_event_binding_expression(
            name=name, mouse_event_type=ap.MouseEventType.CLICK
        )
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin_1.variable_name}." f"{ap.MouseEventType.CLICK.value}({name});"
        )
        assert expected in expression
