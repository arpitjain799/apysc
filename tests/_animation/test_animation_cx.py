from random import randint

from retrying import retry

import apysc as ap
from apysc._display.cx_interface import CxInterface
from apysc._expression import var_names
from apysc._testing.testing_helper import assert_attrs
from apysc._type.variable_name_interface import VariableNameInterface


class TestAnimationCx:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = "test_animation_cx"
        animation_cx: ap.AnimationCx = ap.AnimationCx(
            target=target,
            x=100,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert animation_cx.variable_name.startswith(f"{var_names.ANIMATION_CX}_")
        assert_attrs(
            expected_attrs={
                "_target": target,
                "_cx": 100,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_cx,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = "test_animation_cx"
        animation_cx: ap.AnimationCx = ap.AnimationCx(
            target=target,
            x=100,
        )
        expression: str = animation_cx._get_animation_func_expression()
        assert expression == f"\n  .cx({animation_cx._cx.variable_name});"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: CxInterface = CxInterface()
        target.variable_name = "test_animation_cx"
        animation_cx: ap.AnimationCx = ap.AnimationCx(target=target, x=100)
        expression: str = animation_cx._get_complete_event_in_handler_head_expression()
        expected: str = (
            f"{target._x.variable_name} = " f"{animation_cx._cx.variable_name};"
        )
        assert expression == expected
