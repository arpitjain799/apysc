"""Test project for line_cap setting.

Command examples:
$ python test_projects/line_cap/main.py
$ python line_cap/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apysc import LineCaps
from apysc import Sprite
from apysc import Stage
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
    sprite.graphics.line_style(color='#0af', thickness=10)
    sprite.graphics.move_to(x=50, y=30)
    sprite.graphics.line_to(x=150, y=30)

    sprite.graphics.line_style(
        color='#0af', thickness=10, cap=LineCaps.ROUND)
    sprite.graphics.move_to(x=50, y=60)
    sprite.graphics.line_to(x=150, y=60)

    sprite.graphics.line_style(
        color='#0af', thickness=10, cap=LineCaps.SQUARE)
    sprite.graphics.move_to(x=50, y=90)
    sprite.graphics.line_to(x=150, y=90)

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == '__main__':
    main()
