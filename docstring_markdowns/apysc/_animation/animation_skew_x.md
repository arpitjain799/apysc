# `apysc._animation.animation_skew_x` docstrings

## Module summary

Class implementation for the skew-x animation value.

## `AnimationSkewX` class docstring

The animation class for a skew-x.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> animation: ap.AnimationSkewX = rectangle.animation_skew_x(
...     skew_x=50,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... )
>>> _ = animation.start()
```

<hr>

**[References]**

- [animation_skew_x interface document](https://simon-ritchie.github.io/apysc/en/animation_skew_x.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/en/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/en/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/en/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/en/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/en/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/en/easing_enum.html)

### `__init__` method docstring

The animation class for a skew-x.<hr>

**[Parameters]**

- `target`: SkewXInterface
  - A target instance of the animation target (e.g., `Rectangle` instance).
- `skew_x`: Int or int
  - The final skew-x of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Raises]**

- TypeError: If a specified target is not a SkewXInterface instance.

### `_get_animation_func_expression` method docstring

Get a animation function expression.<hr>

**[Returns]**

- `expression`: str
  - Animation function expression.

### `_get_complete_event_in_handler_head_expression` method docstring

Get an expression to insert into the complete event handler's head.<hr>

**[Returns]**

- `expression`: str
  - An expression to insert into the complete event handler's head.