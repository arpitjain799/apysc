"""The test project for the `Sprite` class.

Command examples:
$ python test_projects/Sprite/main.py
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
    _: ap.Stage = ap.Stage(
        background_color="#333",
        stage_width=1200,
        stage_height=900,
    )

    sprite: ap.Sprite = ap.Sprite()
    sprite.graphics.begin_fill(color="#0af")
    sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
    sprite.graphics.draw_rect(
        x=150,
        y=50,
        width=50,
        height=50,
    )
    sprite.x = ap.Number(50)

    bounding_box: ap.RectangleGeom = sprite.get_bounds()
    ap.Rectangle(
        x=bounding_box.left_x,
        y=bounding_box.top_y,
        width=bounding_box.width,
        height=bounding_box.height,
        line_color="#fff",
        line_thickness=1,
    )

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
