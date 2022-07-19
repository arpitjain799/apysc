from random import randint

from retrying import retry

import apysc as ap
from apysc._animation.animation_width_for_ellipse_interface import (
    AnimationWidthForEllipseInterface,
)
from apysc._testing.testing_helper import assert_attrs


class TestAnimationWidthForEllipseInterface:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_width(self) -> None:
        interface: AnimationWidthForEllipseInterface = (
            AnimationWidthForEllipseInterface()
        )
        interface.variable_name = "test_animation_width_for_ellipse_interface"
        animation_width_for_ellipse: ap.AnimationWidthForEllipse = (
            interface.animation_width(
                width=100, duration=1000, delay=500, easing=ap.Easing.EASE_OUT_QUINT
            )
        )
        assert_attrs(
            expected_attrs={
                "_target": interface,
                "_width": 100,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_width_for_ellipse,
        )
