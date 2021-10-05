from random import randint

from retrying import retry

import apysc as ap
from apysc._display.skew_y_interface import SkewYInterface
from apysc._expression import var_names
from apysc._type.variable_name_interface import VariableNameInterface
from tests.testing_helper import assert_attrs, assert_raises


class TestAnimationSkewY:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target_1: SkewYInterface = SkewYInterface()
        target_1.variable_name = 'test_animation_skew_y'
        animation_skew_y: ap.AnimationSkewY = ap.AnimationSkewY(
            target=target_1,
            skew_y=50,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert animation_skew_y.variable_name.startswith(
            f'{var_names.ANIMATION_SKEW_Y}_')
        assert_attrs(
            expected_attrs={
                '_target': target_1,
                '_skew_y': 50,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_skew_y)

        target_2: VariableNameInterface = VariableNameInterface()
        target_2.variable_name = 'test_animation_skew_y'
        assert_raises(
            expected_error_class=TypeError,
            func_or_method=ap.AnimationSkewY,
            kwargs={
                'target': target_2,
                'skew_y': 50,
            },
            match='Specified `target` argument is not a SkewYInterface',
        )
