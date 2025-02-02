"""Test project for draw_dotted_line interface.

Command examples:
$ python test_projects/draw_dotted_line/main.py
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
        thickness=5,
        dash_setting=ap.LineDashSetting(dash_size=10, space_size=5),
    )
    _: ap.Line = sprite.graphics.draw_dotted_line(
        x_start=50, y_start=50, x_end=350, y_end=50, dot_size=5
    )

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == "__main__":
    main()
