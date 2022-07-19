from random import randint

from retrying import retry

import apysc as ap
from apysc._display.append_line_point_interface import AppendLinePointInterface
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import assert_raises


class TestAppendLinePointInterface:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_append_line_point(self) -> None:
        expression_data_util.empty_expression()
        interface: AppendLinePointInterface = AppendLinePointInterface()
        interface.variable_name = "test_append_line_point_interface"
        interface._variable_name_suffix = "test_interface"
        x: ap.Int = ap.Int(50)
        y: ap.Int = ap.Int(100)
        assert_raises(
            expected_error_class=AttributeError,
            callable_=interface.append_line_point,
            match=r"_points_var_name attribute is not set.",
            x=x,
            y=y,
        )

        interface._points_var_name = "test_points"
        interface.append_line_point(x=x, y=y)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"test_points.push([{x.variable_name}, {y.variable_name}]);"
            f"\n{interface.variable_name}.plot(test_points);"
        )
        assert expected in expression
        assert "test_interface" in interface.points[0]._variable_name_suffix
