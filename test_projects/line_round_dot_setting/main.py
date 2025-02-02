"""Test project for line_round_dot_setting.

Command examples:
$ python test_projects/line_round_dot_setting/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module), "test_output/"
)


def main() -> None:
    """
    Entry point of this test project.
    """
    ap.Stage(background_color="#333", stage_width=1000, stage_height=500)

    sprite: ap.Sprite = ap.Sprite()
    sprite.graphics.line_style(
        color="#0af",
        round_dot_setting=ap.LineRoundDotSetting(round_size=10, space_size=10),
    )
    sprite.graphics.move_to(x=50, y=30)
    sprite.graphics.line_to(x=450, y=30)

    sprite.graphics.line_style(
        color="#0af",
        round_dot_setting=ap.LineRoundDotSetting(round_size=10, space_size=20),
    )
    sprite.graphics.move_to(x=50, y=60)
    sprite.graphics.line_to(x=450, y=60)

    sprite.graphics.line_style(
        color="#0af",
        round_dot_setting=ap.LineRoundDotSetting(round_size=20, space_size=2),
    )
    sprite.graphics.move_to(x=50, y=90)
    sprite.graphics.line_to(x=450, y=90)

    sprite.graphics.line_style(color="#0af", thickness=3)
    sprite.graphics.move_to(x=40, y=120)
    sprite.graphics.line_to(x=460, y=120)

    sprite.graphics.line_style(
        color="#0af",
        round_dot_setting=ap.LineRoundDotSetting(round_size=10, space_size=10),
    )
    polyline: ap.Polyline = sprite.graphics.move_to(x=50, y=150)
    sprite.graphics.line_to(x=450, y=150)
    sprite.graphics.line_to(x=700, y=250)
    sprite.graphics.line_to(x=700, y=150)
    polyline.click(on_polyline_click)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_polyline_click(e: ap.MouseEvent[ap.Polyline], options: dict) -> None:
    """
    Handler that called when polyline is clicked.

    Parameters
    ----------
    e : MouseEvent
        Created MouseEvent instance.
    options : dict
        Optional parameters.
    """
    polyline: ap.Polyline = e.this
    polyline.delete_line_round_dot_setting()


if __name__ == "__main__":
    main()
