# pyright: reportUnusedExpression=false

from random import randint
from typing import List
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display.graphics import Graphics
from apysc._display.graphics import Rectangle
from apysc._expression import expression_data_util
from apysc._testing import testing_helper


class TestGraphics:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        graphics: Graphics = Graphics(parent=sprite)
        testing_helper.assert_attrs(
            expected_attrs={
                'parent_sprite': sprite,
            },
            any_obj=graphics)
        assert isinstance(graphics.variable_name, str)
        assert graphics.variable_name != ''

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_begin_fill(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        graphics: Graphics = Graphics(parent=sprite)
        testing_helper.assert_raises(
            expected_error_class=ValueError,
            callable_=graphics.begin_fill,
            color='red')

        graphics.begin_fill(color='#0af')
        testing_helper.assert_attrs(
            expected_attrs={
                '_fill_color': '#00aaff',
            },
            any_obj=graphics)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_draw_rect(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        graphics: Graphics = Graphics(parent=sprite)
        rectangle: Rectangle = graphics.draw_rect(
            x=100, y=200, width=300, height=400)
        assert graphics.num_children == 1
        testing_helper.assert_attrs(
            expected_attrs={
                '_x': 100,
                '_y': 200,
                'width': 300,
                'height': 400,
            },
            any_obj=graphics.get_child_at(index=0))
        assert isinstance(graphics.get_child_at(index=0), Rectangle)
        assert rectangle == graphics.get_child_at(index=0)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_clear(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.begin_fill(color='#333')
        sprite.graphics.draw_rect(x=50, y=50, width=100, height=100)
        assert sprite.graphics.num_children == 1
        sprite.graphics.clear()
        assert sprite.graphics.num_children == 0

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'var {sprite.graphics.variable_name} = '
            f'{stage.variable_name}.nested();'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        repr_str: str = repr(sprite.graphics)
        assert repr_str == f"Graphics('{sprite.graphics.variable_name}')"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_to(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        polyline: ap.Polyline = sprite.graphics.line_to(x=100, y=200)
        assert polyline.points == ap.Array(
            [ap.Point2D(0, 0), ap.Point2D(100, 200)])
        assert polyline.x == 0
        assert polyline.y == 0
        pre_var_name: str = polyline.variable_name

        polyline = sprite.graphics.line_to(x=-50, y=-100)
        assert polyline.points == ap.Array(
            [ap.Point2D(0, 0), ap.Point2D(100, 200), ap.Point2D(-50, -100)])
        assert polyline.variable_name == pre_var_name
        assert polyline.x == -50
        assert polyline.y == -100

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_move_to(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        polyline: ap.Polyline = sprite.graphics.move_to(x=100, y=200)
        assert polyline.points == ap.Array([ap.Point2D(100, 200)])
        pre_var_name: str = polyline.variable_name

        sprite.graphics.line_to(x=0, y=0)
        polyline = sprite.graphics.move_to(x=300, y=400)
        assert polyline.points == ap.Array([ap.Point2D(300, 400)])
        assert polyline.variable_name != pre_var_name

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__reset_each_line_settings(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics._line_dot_setting = ap.LineDotSetting(dot_size=10)
        sprite.graphics._line_dash_setting = ap.LineDashSetting(
            dash_size=10, space_size=5)
        sprite.graphics._line_round_dot_setting = ap.LineRoundDotSetting(
            round_size=10, space_size=5)
        sprite.graphics._line_dash_dot_setting = ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=5)
        sprite.graphics._reset_each_line_settings()
        assert sprite.graphics._line_dot_setting is None
        assert sprite.graphics._line_dash_setting is None
        assert sprite.graphics._line_round_dot_setting is None
        assert sprite.graphics._line_dash_dot_setting is None

    def _assert_line_points(
            self,
            line: ap.Line,
            expected_x_start: int = 50,
            expected_y_start: int = 100,
            expected_x_end: int = 150,
            expected_y_end: int = 200) -> None:
        """
        Assert line points are expected values or not.

        Parameters
        ----------
        line : Line
            Target line instance to check.
        expected_x_start : int, default 50
            Expected line x start coordinate.
        expected_y_start : int, default 100
            Expected line y start coordinate.
        expected_x_end : int, default 150
            Expected line x end coordinate.
        expected_y_end : int, default 200
            Expected line y end coordinate.

        Raises
        ------
        AssertionError
            If unexpected coordinate(s) is set.
        """
        assert line._start_point == ap.Point2D(
            x=expected_x_start, y=expected_y_start)
        assert line._end_point == ap.Point2D(
            x=expected_x_end, y=expected_y_end)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_draw_line(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.line_style(
            color='#333', thickness=3,
            dot_setting=ap.LineDotSetting(dot_size=10))
        line: ap.Line = sprite.graphics.draw_line(
            x_start=50, y_start=100, x_end=150, y_end=200)
        assert line.line_color == '#333333'
        assert line.line_thickness == 3
        assert line.line_dot_setting is None
        self._assert_line_points(line=line)
        assert isinstance(sprite.graphics.line_dot_setting, ap.LineDotSetting)
        sprite.graphics._children == [line]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_draw_dashed_line(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.line_style(
            color='#333', thickness=3,
            dot_setting=ap.LineDotSetting(dot_size=5))
        line: ap.Line = sprite.graphics.draw_dashed_line(
            x_start=50, y_start=100, x_end=150, y_end=200,
            dash_size=10, space_size=5)
        assert line.line_color == '#333333'
        assert line.line_thickness == 3
        line_dash_setting: Optional[ap.LineDashSetting] = \
            line.line_dash_setting
        assert isinstance(line_dash_setting, ap.LineDashSetting)
        assert line_dash_setting.dash_size == 10
        assert line_dash_setting.space_size == 5
        self._assert_line_points(line=line)
        assert isinstance(sprite.graphics.line_dot_setting, ap.LineDotSetting)
        sprite.graphics._children == [line]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_draw_dotted_line(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.line_style(
            color='#333',
            dash_setting=ap.LineDashSetting(dash_size=10, space_size=5))
        line: ap.Line = sprite.graphics.draw_dotted_line(
            x_start=50, y_start=100, x_end=150, y_end=200, dot_size=5)
        assert isinstance(line.line_dot_setting, ap.LineDotSetting)
        assert line.line_color == '#333333'
        self._assert_line_points(line=line)
        assert isinstance(
            sprite.graphics.line_dash_setting, ap.LineDashSetting)
        sprite.graphics._children == [line]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_draw_round_dotted_line(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.line_style(
            color='#333',
            dash_setting=ap.LineDashSetting(dash_size=10, space_size=5))
        line: ap.Line = sprite.graphics.draw_round_dotted_line(
            x_start=50, y_start=100, x_end=150, y_end=200,
            round_size=10, space_size=5)
        assert isinstance(line.line_round_dot_setting, ap.LineRoundDotSetting)
        assert line.line_color == '#333333'
        self._assert_line_points(line=line)
        assert isinstance(
            sprite.graphics.line_dash_setting, ap.LineDashSetting)
        sprite.graphics._children == [line]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_draw_dash_dotted_line(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.line_style(
            color='#333',
            dash_setting=ap.LineDashSetting(dash_size=10, space_size=5))
        line: ap.Line = sprite.graphics.draw_dash_dotted_line(
            x_start=50, y_start=100, x_end=150, y_end=200,
            dot_size=3, dash_size=10, space_size=5)
        assert isinstance(line.line_dash_dot_setting, ap.LineDashDotSetting)
        assert line.line_color == '#333333'
        self._assert_line_points(line=line)
        assert isinstance(
            sprite.graphics.line_dash_setting, ap.LineDashSetting)
        sprite.graphics._children == [line]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_draw_polygon(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.begin_fill(color='#333')
        polygon: ap.Polygon = sprite.graphics.draw_polygon(
            points=[
                ap.Point2D(50, 50), ap.Point2D(150, 50),
                ap.Point2D(100, 100)])
        assert polygon.points == ap.Array(
            [ap.Point2D(50, 50), ap.Point2D(150, 50), ap.Point2D(100, 100)])
        assert polygon.fill_color == '#333333'
        assert sprite.graphics._children == [polygon]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_draw_round_rect(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        rectangle: Rectangle = sprite.graphics.draw_round_rect(
            x=50, y=100, width=150, height=200, ellipse_width=20,
            ellipse_height=30)
        assert rectangle.x == 50
        assert rectangle.y == 100
        assert rectangle.width == 150
        assert rectangle.height == 200
        assert rectangle.ellipse_width == ap.Int(20)
        assert rectangle.ellipse_height == ap.Int(30)
        assert sprite.graphics._children == [rectangle]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_draw_circle(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        circle: ap.Circle = sprite.graphics.draw_circle(
            x=50, y=100, radius=30)
        assert circle.x == 50
        assert circle.y == 100
        assert circle.radius == 30
        assert sprite.graphics._children == [circle]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_draw_ellipse(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
            x=50, y=100, width=150, height=200)
        assert ellipse.x == 50
        assert ellipse.y == 100
        assert ellipse.width == 150
        assert ellipse.height == 200
        assert sprite.graphics._children == [ellipse]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_draw_path(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        path_data_list: List[ap.PathDataBase] = [
            ap.PathMoveTo(x=50, y=50),
        ]
        path: ap.Path = sprite.graphics.draw_path(
            path_data_list=path_data_list)
        assert isinstance(path, ap.Path)
        assert path._path_data_list == path_data_list
