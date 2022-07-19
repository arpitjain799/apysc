from random import randint

from retrying import retry

import apysc as ap
from apysc._display.skew_y_interface import SkewYInterface
from apysc._testing.testing_helper import assert_attrs


class TestAnimationSkewYInterface:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_skew_y(self) -> None:
        interface: SkewYInterface = SkewYInterface()
        animation_skew_y: ap.AnimationSkewY = interface._animation_skew_y(
            skew_y=50,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert_attrs(
            expected_attrs={
                "_target": interface,
                "_skew_y": 50,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_skew_y,
        )
