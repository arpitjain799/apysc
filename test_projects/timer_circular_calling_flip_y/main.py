"""The test project for the timer event circular calling and
updating flip-y interface value.

Command examples:
$ python test_projects/timer_circular_calling_flip_y/main.py
$ python timer_circular_calling_flip_y/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType
from typing import Any
from typing import Dict

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """
    Entry point of this test project.
    """
    stage: ap.Stage = ap.Stage(
        background_color='#333',
        stage_width=1000, stage_height=500, stage_elem_id='stage')
    sprite: ap.Sprite = ap.Sprite(stage=stage)
    sprite.y = ap.Int(100)
    sprite.graphics.begin_fill(color='#00aaff')

    rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        x=50, y=0, width=50, height=50)
    timer_1: ap.Timer = ap.Timer(
        on_timer_1, delay=1000, repeat_count=1,
        options={'rectangle': rectangle})
    timer_1.timer_complete(
        on_timer_complete_1, options={'rectangle': rectangle})
    timer_1.start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_timer_1(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler will be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.flip_y = rectangle.flip_y.not_


def on_timer_complete_1(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler will be called when a timer has completed.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    timer_2: ap.Timer = ap.Timer(
        on_timer_2, delay=1000, repeat_count=1,
        options={'rectangle': rectangle})
    timer_2.timer_complete(
        on_timer_complete_2,
        options={'rectangle': rectangle})
    timer_2.start()


def on_timer_2(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler will be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    rectangle.flip_y = rectangle.flip_y.not_


def on_timer_complete_2(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler will be called when a timer has completed.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    timer_3: ap.Timer = ap.Timer(
        on_timer_1, delay=1000, repeat_count=1,
        options={'rectangle': rectangle})
    timer_3.timer_complete(
        on_timer_complete_1, options={'rectangle': rectangle})
    timer_3.start()


if __name__ == '__main__':
    main()
