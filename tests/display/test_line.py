from random import randint

from retrying import retry

from apysc import Stage, Sprite, LineDotSetting, Point2D
from apysc.expression import var_names
from apysc import Line


class TestLine:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        line_dot_setting: LineDotSetting = LineDotSetting(dot_size=10)
        sprite.graphics.line_style(
            color='#0af', dot_setting=line_dot_setting)
        line: Line = Line(
            parent=sprite.graphics,
            start_point=Point2D(x=10, y=20),
            end_point=Point2D(x=30, y=40))
        assert line.variable_name.startswith(f'{var_names.LINE}_')
        assert line._start_point == Point2D(x=10, y=20)
        assert line._end_point == Point2D(x=30, y=40)
        assert line.line_color == '#00aaff'
        assert line.line_dot_setting == line_dot_setting
