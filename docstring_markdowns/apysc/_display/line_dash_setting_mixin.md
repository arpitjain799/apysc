# `apysc._display.line_dash_setting_mixin` docstrings

## Module summary

Class implementation for line dash setting mix-in.

## `LineDashSettingMixIn` class docstring

### `_append_line_dash_setting_update_expression` method docstring

Append line dash setting updating expression.

### `_initialize_line_dash_setting_if_not_initialized` method docstring

Initialize the _line_dash_setting attribute if this interface does not initialize it yet.

### `_make_snapshot` method docstring

Make value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_revert` method docstring

Revert value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_update_line_dash_setting_and_skip_appending_exp` method docstring

Update line dash setting and skip appending expression.<hr>

**[Parameters]**

- `value`: LineDashSetting or None
  - Line dash setting to set.