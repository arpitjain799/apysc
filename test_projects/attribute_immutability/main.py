"""The test project to test the immutability of the attribute.

Command examples:
$ python test_projects/attribute_immutability/main.py
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
    sprite.graphics.begin_fill(color="#0af")
    rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
    rectangle.x += 50
    ap.assert_equal(rectangle.x, 100)
    rectangle.x += 50
    ap.assert_equal(rectangle.x, 150)

    x: ap.Number = rectangle.x
    x += 50
    ap.assert_equal(x, 200)
    ap.assert_not_equal(x, rectangle.x)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
