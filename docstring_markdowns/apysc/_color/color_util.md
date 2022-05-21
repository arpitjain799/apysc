# `apysc._color.color_util` docstrings

## Module summary

Color-related implementations.

## `_append_complement_hex_color_expression` function docstring

Append complement_hex_color function's expression.<hr>

**[Parameters]**

- `hex_color_code`: String
  - Complemented hex color code string.

## `_append_remove_color_code_sharp_symbol_expression` function docstring

Append the remove_color_code_sharp_symbol function's expression.<hr>

**[Parameters]**

- `hex_color_code`: String
  - A sharp symbol removed string instance.

## `_fill_one_digit_hex_color_code` function docstring

Fill 1 digit hexadecimal color code until it becomes 6 digits.<hr>

**[Parameters]**

- `hex_color_code`: str
  - One digit hexadecimal color code (not including '#'). e.g., 'a', '0'

<hr>

**[Returns]**

- `filled_color_code`: str
  - Result color code. e.g., '00000a', '000000'

## `_fill_three_digit_hex_color_code` function docstring

Fill 3 digits hexadecimal color code until it becomes 6 digits.<hr>

**[Parameters]**

- `hex_color_code`: str
  - One digit hexadecimal color code (not including '#'). e.g., 'aaa', 'fff'

<hr>

**[Returns]**

- `filled_color_code`: str
  - Result color code. e.g., 'aaaaaa', 'ffffff'

## `complement_hex_color` function docstring

Complement hex color for convenience; for instance, add # prefix or three digits to become six digits, upper case to lower case.<hr>

**[Parameters]**

- `hex_color_code`: str or String
  - Hexadecimal color code. e.g., 'ff0000', '#666', '#0'

<hr>

**[Returns]**

- `complemented_hex_color_code`: str or String
  - Result hex color code. e.g., '#ff0000', '#666666, '#000000'

## `remove_color_code_sharp_symbol` function docstring

Remove a sharp symbol from a specified hexadecimal color code string.<hr>

**[Parameters]**

- `hex_color_code`: StrOrString
  - A targert hexadecimal color code string.

<hr>

**[Returns]**

- `hex_color_code`: StrOrString
  - A result string.