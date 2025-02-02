# PathMoveTo class

This page explains the `PathMoveTo` class.

## What class is this?

The `PathMoveTo` class is the class to set a new position on a path.

This setting only sets coordinates and does not append any vector graphics.

Mainly, the `Path` class constructor or `draw_path` interfaces use this setting.

## Basic usage

The `PathMoveTo` class constructor requires the `x` and `y` arguments.

The `Path` class constructor or `draw_path` interfaces' `path_data_list` argument requires its instance.

The following example sets the x=50 and y=50 coordinates with the `PathMoveTo` instance and then draws the line to x=150 and y=50:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=100, stage_elem_id="stage"
)
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=150, y=50),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_move_to_basic_usage/")
```

<iframe src="static/path_move_to_basic_usage/index.html" width="200" height="100"></iframe>

## Relative position setting

The constructor's `relative` optional argument changes its behavior.

For example, if you set True to its argument, coordinates become relative.

The default setting is False, and it becomes absolute.

The following example sets the relative setting and moves to the 50px under position from the current position:

```py
# runnable
import apysc as ap

ap.Stage(
    background_color="#333", stage_width=200, stage_height=200, stage_elem_id="stage"
)
path: ap.Path = ap.Path(
    path_data_list=[
        ap.PathMoveTo(x=50, y=50),
        ap.PathLineTo(x=150, y=50),
        ap.PathMoveTo(x=0, y=50, relative=True),
        ap.PathLineTo(x=0, y=50, relative=True),
    ],
    line_color="#0af",
    line_thickness=5,
)

ap.save_overall_html(dest_dir_path="path_move_to_relative/")
```

<iframe src="static/path_move_to_relative/index.html" width="200" height="200"></iframe>

## PathMoveTo class constructor API

<!-- Docstring: apysc._geom.path_move_to.PathMoveTo.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, x: Union[float, apysc._type.number.Number], y: Union[float, apysc._type.number.Number], *, relative: Union[bool, apysc._type.boolean.Boolean] = False, variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

Path data class for the SVG `move to` (M).<hr>

**[Parameters]**

- `x`: float or Number
  - X-coordinate of the destination point.
- `y`: float or Number
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - A boolean value indicates whether the path coordinates are relative or not (absolute).
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color="#fff", thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathLineTo(x=50, y=50),
...     ]
... )
```

<hr>

**[References]**

- [Path class](https://simon-ritchie.github.io/apysc/en/path.html)
- [Graphics draw_path interface](https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html)