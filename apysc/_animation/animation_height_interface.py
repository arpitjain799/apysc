"""Class implementation for the animation_height interface.
"""

from typing import Union

import apysc as ap
from apysc._animation.animation_height import AnimationHeight
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.easing import Easing


class AnimationHeightInterface(AnimationInterfaceBase):

    def animation_height(
            self,
            height: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> AnimationHeight:
        """
        Set the height animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        height : int or Int
            The final height of the animation.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_height : AnimationHeight
            Created animation setting instance.

        References
        ----------
        - animation_width and animation_height interfaces document
            - https://bit.ly/39XPUdq
        - Animation interfaces duration setting
            - https://simon-ritchie.github.io/apysc/animation_duration.html
        - Each animation interface return value document
            - https://bit.ly/2XOoa8w
        - Easing enum document
            - https://simon-ritchie.github.io/apysc/easing_enum.html
        """
        animation_height: AnimationHeight = AnimationHeight(
            target=self,
            height=height,
            duration=duration,
            delay=delay,
            easing=easing)
        return animation_height
