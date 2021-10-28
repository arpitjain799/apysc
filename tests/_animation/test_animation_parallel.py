from random import randint
from typing import List

from retrying import retry

import apysc as ap
from apysc._animation.animation_parallel import AnimationParallel
from apysc._expression import var_names
from tests.testing_helper import assert_attrs


class TestAnimationParallel:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        rectangle: ap.Rectangle = sprite.graphics.draw_rect(
            x=50, y=50, width=50, height=50)
        animations: List[ap.AnimationBase] = [
            rectangle.animation_x(x=100),
            rectangle.animation_y(y=100),
        ]
        animation_parallel: ap.AnimationParallel = rectangle.\
            animation_parallel(
                animations=animations,
                duration=1000,
                delay=500,
                easing=ap.Easing.EASE_OUT_QUINT)
        assert_attrs(
            expected_attrs={
                '_target': rectangle,
                '_animations': animations,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_parallel)
        assert animation_parallel.variable_name.startswith(
            f'{var_names.ANIMATION_PARALLEL}_')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        rectangle: ap.Rectangle = sprite.graphics.draw_rect(
            x=50, y=50, width=50, height=50)
        animation_x: ap.AnimationX = rectangle.animation_x(x=100)
        animation_y: ap.AnimationY = rectangle.animation_y(y=100)
        animations: List[ap.AnimationBase] = [
            animation_x,
            animation_y,
        ]
        animation_parallel: ap.AnimationParallel = rectangle.\
            animation_parallel(animations=animations)
        expression: str = animation_parallel._get_animation_func_expression()
        expected: str = (
            f'\n  .x({animation_x._x.variable_name})'
            f'\n  .y({animation_y._y.variable_name});'
        )
        assert expression == expected

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        rectangle: ap.Rectangle = sprite.graphics.draw_rect(
            x=50, y=50, width=50, height=50)
        animations: List[ap.AnimationBase] = [
            rectangle.animation_x(x=100),
            rectangle.animation_y(y=100),
        ]
        animation_parallel: ap.AnimationParallel = rectangle.\
            animation_parallel(animations=animations)
        expression: str = animation_parallel.\
            _get_complete_event_in_handler_head_expression()
        expected_strs: List[str] = [
            f'{rectangle._x.variable_name} = ',
            f'{rectangle._y.variable_name} = ',
        ]
        for expected in expected_strs:
            assert expected in expression
