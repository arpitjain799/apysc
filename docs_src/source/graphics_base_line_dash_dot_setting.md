# GraphicsBase line_dash_dot_setting interface

This page explains the `GraphicsBase` class `line_dash_dot_setting` property interface.

## What interface is this?

The `line_dash_dot_setting` property interface updates or get the instance's current line dash-dot setting.

## Basic usage

The getter or setter interface value becomes (or requires) the `LineDashDotSetting` instance value.

The following example sets the 10-pixel dash and 3-pixel dot to the line:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=250, stage_height=100, background_color="#333", stage_elem_id="stage"
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color="#0af", thickness=5)

line: ap.Line = sprite.graphics.draw_line(x_start=50, y_start=50, x_end=200, y_end=50)
line.line_dash_dot_setting = ap.LineDashDotSetting(
    dot_size=10, dash_size=3, space_size=3
)

ap.save_overall_html(dest_dir_path="./graphics_base_line_dash_dot_setting_basic_usage/")
```

<iframe src="static/graphics_base_line_dash_dot_setting_basic_usage/index.html" width="250" height=100></iframe>


## line_dash_dot_setting API

<!-- Docstring: apysc._display.line_dash_dot_setting_interface.LineDashDotSettingInterface.line_dash_dot_setting -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get current dash dot (1-dot chain) setting.<hr>

**[Returns]**

- `line_dash_dot_setting`: LineDashDotSetting or None
  - Dash dot (1-dot chain) setting.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color="#fff", thickness=10)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50
... )
>>> line.line_dash_dot_setting = ap.LineDashDotSetting(
...     dot_size=2, dash_size=5, space_size=3
... )
>>> line.line_dash_dot_setting.dot_size
Int(2)

>>> line.line_dash_dot_setting.dash_size
Int(5)

>>> line.line_dash_dot_setting.space_size
Int(3)
```