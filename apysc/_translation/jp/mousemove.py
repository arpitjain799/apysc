"""This module is for the translation mapping data of the
following document:

Document file: mousemove.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Mousemove interface':
    '',

    'This page explains the `mousemove` interface.':
    '',

    '## What interface is this?':
    '',

    'The `mousemove` interface binds the mouse moving event handler to any `DisplayObject` instance. If you move the mouse cursor on that instance, the interface calls the registered handler.':  # noqa
    '',

    '## See also':
    '',

    'The following page describes the basic mouse event interfaces.\n\n- [Basic mouse event interfaces](mouse_event_basic.md)':  # noqa
    '',

    '## Basic usage':
    '',

    'Each `DisplayObject` instance has the `mousemove` method, and you can bind handlers by that.\n\nThe following example binds the mouse move event handler to the circle. So if you move a mouse cursor on that, the circle follows the cursor position.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mousemove(\n        e: ap.MouseEvent[ap.Circle], options: dict) -> None:\n    """\n    The handler that the circle calls when mousemove.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle: ap.Circle = e.this\n    circle.x = e.stage_x\n    circle.y = e.stage_y\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=200,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\ncircle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)\ncircle.mousemove(on_mousemove)\n\nap.save_overall_html(\n    dest_dir_path=\'mousemove_basic_usage/\')\n```':  # noqa
    '',

    '<iframe src="static/mousemove_basic_usage/index.html" width="200" height="200"></iframe>':  # noqa
    '',

    '## Unbind interfaces':
    '',

    '`unbind_mousemove` interface can remove the binding of the mouse move event from the `DisplayObject`\\.\n\nIn the following example, the interface removes the mouse move event handler if you click the circle.':  # noqa
    '',

    '```py\n# runnable\nimport apysc as ap\n\n\ndef on_mousemove(\n        e: ap.MouseEvent[ap.Circle], options: dict) -> None:\n    """\n    The handler that the circle calls when mousemove.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle: ap.Circle = e.this\n    circle.x = e.stage_x\n    circle.y = e.stage_y\n\n\ndef on_click(e: ap.MouseEvent[ap.Circle], options: dict) -> None:\n    """\n    The handler that the circle calls when clicked.\n\n    Parameters\n    ----------\n    e : MouseEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    circle: ap.Circle = e.this\n    circle.unbind_mousemove(handler=on_mousemove)\n\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=200,\n    stage_elem_id=\'stage\')\n\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\'#0af\')\ncircle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)\ncircle.mousemove(on_mousemove)\ncircle.click(on_click)\n\nap.save_overall_html(\n    dest_dir_path=\'mousemove_unbind_interface/\')\n```':  # noqa
    '',

    '<iframe src="static/mousemove_unbind_interface/index.html" width="200" height="200"></iframe>\n\nThere are also existing the `unbind_mousemove_all` interface. This interface unbinds all the handlers from the target `DisplayObject` instance.':  # noqa
    '',

    '## mousemove API':
    '',

    '<!-- Docstring: apysc._event.mouse_move_interface.MouseMoveInterface.mousemove -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `mousemove(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType], *, options:Union[~_O, NoneType]=None) -> str`<hr>\n\n**[Interface summary]** Add mouse move event listener setting.<hr>\n\n**[Parameters]**\n\n- `handler`: _Handler\n  - Callable that would be called when mousemove on this instance.\n- `options`: dict or None, default None\n  - Optional arguments dictionary to be passed to a handler.\n\n<hr>\n\n**[Returns]**\n\n- `name`: str\n  - Handler\'s name.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mousemove(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     stage_x: ap.Int = e.stage_x\n...     ap.trace(\'stage_x:\', stage_x)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousemove(on_mousemove)\n```':  # noqa
    '',

    '<hr>\n\n**[References]**\n\n- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)':  # noqa
    '',

    '## unbind_mousemove API':
    '',

    '<!-- Docstring: apysc._event.mouse_move_interface.MouseMoveInterface.unbind_mousemove -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `unbind_mousemove(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType]) -> None`<hr>\n\n**[Interface summary]** Unbind a specified handler\'s mouse move event.<hr>\n\n**[Parameters]**\n\n- `handler`: _Handler\n  - Unbinding target Callable.\n\n<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mousemove(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     stage_x: ap.Int = e.stage_x\n...     ap.trace(\'stage_x:\', stage_x)\n>>> def on_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.unbind_mousemove(on_mousemove)\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousemove(on_mousemove)\n>>> _ = rectangle.click(on_click)\n```':  # noqa
    '',

    '':
    '',

    '## unbind_mousemove_all API':
    '',

    '<!-- Docstring: apysc._event.mouse_move_interface.MouseMoveInterface.unbind_mousemove_all -->\n\n<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>\n\n**[Interface signature]** `unbind_mousemove_all(self) -> None`<hr>\n\n**[Interface summary]** Unbind all mouse move events.<hr>\n\n**[Examples]**':  # noqa
    '',

    '```py\n>>> import apysc as ap\n>>> def on_mousemove(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     stage_x: ap.Int = e.stage_x\n...     ap.trace(\'stage_x:\', stage_x)\n>>> def on_click(\n...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:\n...     rectangle: ap.Rectangle = e.this\n...     rectangle.unbind_mousemove_all()\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.mousemove(on_mousemove)\n>>> _ = rectangle.click(on_click)\n```':  # noqa
    '',

}
