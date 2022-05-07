from random import randint

from retrying import retry

import apysc as ap
from apysc._display.scale_x_from_center_interface import \
    ScaleXFromCenterInterface
from apysc._expression import var_names
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._testing.testing_helper import assert_attrs
from apysc._testing.testing_helper import assert_raises


class TestAnimationScaleXFromCenter:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target_1: ScaleXFromCenterInterface = ScaleXFromCenterInterface()
        target_1.variable_name = 'test_animation_scale_x_from_center'
        animation: ap.AnimationScaleXFromCenter = \
            ap.AnimationScaleXFromCenter(
                target=target_1,
                scale_x_from_center=2.0,
                duration=1000,
                delay=500,
                easing=ap.Easing.EASE_OUT_QUINT)
        assert animation.variable_name.startswith(
            f'{var_names.ANIMATION_SCALE_X_FROM_CENTER}_'
        )
        assert_attrs(
            expected_attrs={
                '_target': target_1,
                '_scale_x_from_center': 2.0,
                '_before_scale_x_from_center': 1.0,
                '_scale_x_from_center_diff_ratio': 2.0,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation)

        target_2: VariableNameInterface = VariableNameInterface()
        target_2.variable_name = 'test_animation_scale_x_from_center'
        assert_raises(
            expected_error_class=TypeError,
            func_or_method=ap.AnimationScaleXFromCenter,
            kwargs={
                'target': target_2,
                'scale_x_from_center': 2.0,
            },
            match='Specified `target` argument is not a '
                  'ScaleXFromCenterInterface')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: ScaleXFromCenterInterface = ScaleXFromCenterInterface()
        target.variable_name = 'test_animation_scale_x_from_center'
        animation: ap.AnimationScaleXFromCenter = \
            ap.AnimationScaleXFromCenter(
                target=target, scale_x_from_center=2.0)
        expression: str = animation._get_animation_func_expression()
        variable_name: str = \
            animation._scale_x_from_center_diff_ratio.variable_name
        assert expression == (
            f'\n  .scale({variable_name}, 1);'
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: ScaleXFromCenterInterface = ScaleXFromCenterInterface()
        target.variable_name = 'test_animation_scale_x_from_center'
        animation: ap.AnimationScaleXFromCenter = \
            ap.AnimationScaleXFromCenter(
                target=target, scale_x_from_center=2.0)
        expression: str = animation.\
            _get_complete_event_in_handler_head_expression()
        assert expression == (
            f'{target._scale_x_from_center.variable_name} = '
            f'{animation._scale_x_from_center.variable_name};'
        )
