# `apysc._animation.animation_rotation_around_point_mixin` docstrings

## Module summary

Class implementation for the animation_rotation_around_point mix-in.

## `AnimationRotationAroundPointMixIn` class docstring

### `animation_rotation_around_point` method docstring

Set the rotation around the given point animation setting.<hr>

**[Parameters]**

- `rotation_around_point`: Int or int
  - The final rotation of the animation.
- `x`: float or Number
  - X-coordinate.
- `y`: float or Number
  - Y-coordinate.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_rotation_around_point`: AnimationRotationAroundPoint
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
>>> _ = rectangle.animation_rotation_around_point(
...     rotation_around_point=90,
...     x=ap.Int(100),
...     y=ap.Int(100),
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_rotation_around_point interface](https://simon-ritchie.github.io/apysc/en/animation_rotation_around_point.html)
- [Animation interfaces duration setting](https://simon-ritchie.github.io/apysc/en/animation_duration.html)
- [Animation interfaces delay setting](https://simon-ritchie.github.io/apysc/en/animation_delay.html)
- [Each animation interface return value](https://simon-ritchie.github.io/apysc/en/animation_return_value.html)
- [Sequential animation setting](https://simon-ritchie.github.io/apysc/en/sequential_animation.html)
- [animation_parallel interface](https://simon-ritchie.github.io/apysc/en/animation_parallel.html)
- [Easing enum](https://simon-ritchie.github.io/apysc/en/easing_enum.html)