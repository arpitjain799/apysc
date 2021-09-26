"""Class implementation for the animation_width (for ellipse) interface.
"""

from typing import Union

import apysc as ap
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_width_for_ellipse import AnimationEllipseWidth
from apysc._animation.easing import Easing


class AnimationEllipseWidthInterface(AnimationInterfaceBase):

    def animation_width(
            self,
            ellipse_width: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationEllipseWidth:
        """
        Set the ellipse-width animation setting.

        Parameters
        ----------
        ellipse_width : int or Int
            The final ellipse-width of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_width_for_ellipse : AnimationEllipseWidth
            Created animation setting instance.

        References
        ----------
        - Animation interfaces duration setting
            - https://simon-ritchie.github.io/apysc/animation_duration.html
        - Each animation interface return value document
            - https://bit.ly/2XOoa8w
        - Easing enum document
            - https://simon-ritchie.github.io/apysc/easing_enum.html
        """
        animation_width_for_ellipse: AnimationEllipseWidth = \
            AnimationEllipseWidth(
                target=self,
                ellipse_width=ellipse_width,
                duration=duration,
                delay=delay,
                easing=easing)
        return animation_width_for_ellipse
