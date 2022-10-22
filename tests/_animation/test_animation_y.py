from random import randint

from retrying import retry

import apysc as ap
from apysc._display.y_mixin import YMixIn
from apysc._testing.testing_helper import assert_attrs
from apysc._type.variable_name_interface import VariableNameInterface


class TestAnimationY:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = "test_animation_y"
        animation_y: ap.AnimationY = ap.AnimationY(
            target=target,
            y=100,
            duration=2000,
            delay=1000,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert_attrs(
            expected_attrs={
                "_target": target,
                "_y": 100,
                "_duration": 2000,
                "_delay": 1000,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_y,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = "test_animation_y"
        animation_y: ap.AnimationY = ap.AnimationY(target=target, y=100)
        expression: str = animation_y._get_animation_func_expression()
        assert expression == f"\n  .y({animation_y._y.variable_name});"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: YMixIn = YMixIn()
        target.variable_name = "test_y_interface"
        animation_y: ap.AnimationY = ap.AnimationY(target=target, y=100)
        expression: str = animation_y._get_complete_event_in_handler_head_expression()
        assert expression == (
            f"{target._y.variable_name} = " f"{animation_y._y.variable_name};"
        )
