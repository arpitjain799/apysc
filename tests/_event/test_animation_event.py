from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from apysc._type.variable_name_interface import VariableNameInterface


class TestAnimationEvent:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = "test_animation_event"
        animation_move: ap.AnimationMove = ap.AnimationMove(
            target=target, x=50, y=100, duration=1000
        )
        animation_event: ap.AnimationEvent = ap.AnimationEvent(this=animation_move)
        assert animation_event._this == animation_move
        assert animation_event.variable_name.startswith(f"{var_names.ANIMATION_EVENT}_")

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_this(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = "test_animation_event"
        animation_move: ap.AnimationMove = ap.AnimationMove(
            target=target, x=50, y=100, duration=1000
        )
        animation_event: ap.AnimationEvent = ap.AnimationEvent(this=animation_move)
        assert animation_event.this == animation_move
