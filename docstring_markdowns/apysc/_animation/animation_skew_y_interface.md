# `apysc._animation.animation_skew_y_interface` docstrings

## Module summary

Class implementation for the animation_skew_y interface.

## `AnimationSkewYInterface` class docstring

### `_animation_skew_y` method docstring

**Important notes** Currently, this interface does not work correctly. For more details, please see: https://github.com/svgdotjs/svg.js/issues/1222 Set the skew-y animation.<hr>

**[Parameters]**

- `skew_y`: Int or int
  - The final skew-y of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_skew_y`: AnimationSkewY
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle._animation_skew_y(
...     skew_y=50,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/en/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/en/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/en/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/en/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/en/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/en/easing_enum.html)