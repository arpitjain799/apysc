# `apysc._animation.animation_line_thickness` docstrings

## Module summary

Class implementation for the line thickness animation value.

## `AnimationLineThickness` class docstring

The animation class for a line thickness.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> sprite.graphics.line_style(color="#fff", thickness=1)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> animation: ap.AnimationLineThickness
>>> animation = rectangle.animation_line_thickness(
...     thickness=6,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... )
>>> _ = animation.start()
```

<hr>

**[References]**

- [animation_line_thickness interface](https://simon-ritchie.github.io/apysc/en/animation_line_thickness.html)
- [Animation interfaces duration setting](https://simon-ritchie.github.io/apysc/en/animation_duration.html)
- [Animation interfaces delay setting](https://simon-ritchie.github.io/apysc/en/animation_delay.html)
- [Each animation interface return value](https://simon-ritchie.github.io/apysc/en/animation_return_value.html)
- [Sequential animation setting](https://simon-ritchie.github.io/apysc/en/sequential_animation.html)
- [animation_parallel interface](https://simon-ritchie.github.io/apysc/en/animation_parallel.html)
- [Easing enum](https://simon-ritchie.github.io/apysc/en/easing_enum.html)

### `__init__` method docstring

The animation class for a line thickness.<hr>

**[Parameters]**

- `target`: VariableNameMixIn
  - A target instance of the animation target (e.g., `Rectangle` instance).
- `thickness`: Int or int
  - The final line thickness of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

### `_get_animation_func_expression` method docstring

Get a animation function expression.<hr>

**[Returns]**

- `expression`: str
  - Animation function expression.

### `_get_complete_event_in_handler_head_expression` method docstring

Get an expression to be inserted into the complete event handler's head.<hr>

**[Returns]**

- `expression`: str
  - An expression to insert into the complete event handler's head.