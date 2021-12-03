from random import randint

from retrying import retry

import apysc as ap
from tests.testing_helper import assert_attrs


class TestPathBezier2D:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        path_bezier_2d: ap.PathBezier2D = ap.PathBezier2D(
            control_x=10, control_y=20, dest_x=30, dest_y=40)
        assert_attrs(
            expected_attrs={
                '_control_x': 10,
                '_control_y': 20,
                '_dest_x': 30,
                '_dest_y': 40,
            },
            any_obj=path_bezier_2d,
        )
        assert isinstance(path_bezier_2d._control_x, ap.Int)
        assert isinstance(path_bezier_2d._control_y, ap.Int)
        assert isinstance(path_bezier_2d._dest_x, ap.Int)
        assert isinstance(path_bezier_2d._dest_y, ap.Int)
