"""Test project for line_to interface.

Command examples:
$ python test_projects/line_to/main.py
$ python line_to/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apysc import Int
from apysc import Number
from apysc import Rectangle
from apysc import Sprite
from apysc import Stage
from apysc import String
from apysc import assert_not_equal
from apysc.file import file_util
from apysc.html import exporter

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """
    Entry point of this test project.
    """
    stage: Stage = Stage(
        background_color='#111',
        stage_width=1000, stage_height=500)

    sprite: Sprite = Sprite(stage=stage)
    sprite.graphics.begin_fill(color='#0af', alpha=0.5)
    sprite.graphics.line_style(color='#eee', thickness=4, alpha=0.75)
    sprite.graphics.line_to(x=100, y=0)
    sprite.graphics.line_to(x=100, y=100)
    sprite.graphics.line_to(x=0, y=0)

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == '__main__':
    main()
