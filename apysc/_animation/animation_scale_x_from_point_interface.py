"""Class implementation for the animation_scale_x_from_point
interface.
"""

from typing import Union

from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_scale_x_from_point import \
    AnimationScaleXFromPoint
from apysc._animation.easing import Easing
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._validation import arg_validation_decos


class AnimationScaleXFromPointInterface(AnimationInterfaceBase):

    @arg_validation_decos.is_num(arg_position_index=1)
    @arg_validation_decos.is_integer(arg_position_index=2)
    @arg_validation_decos.is_integer(arg_position_index=3)
    @arg_validation_decos.num_is_gt_zero(arg_position_index=3)
    @arg_validation_decos.is_integer(arg_position_index=4)
    @arg_validation_decos.is_easing(arg_position_index=5)
    def animation_scale_x_from_point(
            self,
            *,
            scale_x_from_point: Union[float, Number],
            x: Union[int, Int],
            duration: Union[int, Int] = 3000,
            delay: Union[int, Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationScaleXFromPoint:
        """
        Set the scale-x from the given point animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        scale_x_from_point : float or Number
            The final scale-x from the given point of the animation.
        x : Int or int
            X-coordinate.
        duration : Int or int, default 3000
            Milliseconds before an animation ends.
        delay : Int or int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_scale_x_from_point : AnimationScaleXFromPoint
            Created animation setting instance.

        References
        ----------
        - animation_scale_x_from_point interface document
            - https://simon-ritchie.github.io/apysc/en/animation_scale_x_and_y_from_point.html  # noqa
        - Animation interfaces duration setting document
            - https://simon-ritchie.github.io/apysc/en/animation_duration.html
        - Animation interfaces delay setting document
            - https://simon-ritchie.github.io/apysc/en/animation_delay.html
        - Each animation interface return value document
            - https://simon-ritchie.github.io/apysc/en/animation_return_value.html  # noqa
        - Sequential animation setting document
            - https://simon-ritchie.github.io/apysc/en/sequential_animation.html
        - animation_parallel interface document
            - https://simon-ritchie.github.io/apysc/en/animation_parallel.html
        - Easing enum document
            - https://simon-ritchie.github.io/apysc/en/easing_enum.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.animation_scale_x_from_point(
        ...     scale_x_from_point=0.5,
        ...     x=ap.Int(100),
        ...     duration=1500,
        ...     easing=ap.Easing.EASE_OUT_QUINT,
        ... ).start()
        """
        animation_scale_x_from_point: AnimationScaleXFromPoint = \
            AnimationScaleXFromPoint(
                target=self,
                scale_x_from_point=scale_x_from_point,
                x=x,
                duration=duration,
                delay=delay,
                easing=easing)
        return animation_scale_x_from_point
