"""This module is for the base class of the x-coordinate
interfaces.
"""

from abc import ABC
from abc import abstractmethod

from apysc._animation.animation_move_interface import AnimationMoveInterface
from apysc._animation.animation_x_interface import AnimationXInterface
from apysc._type.int import Int


class XInterfaceBase(AnimationXInterface, AnimationMoveInterface, ABC):

    @property
    @abstractmethod
    def x(self) -> Int:
        """
        Get a x-coordinate.
        """

    @x.setter
    @abstractmethod
    def x(self, value: Int) -> None:
        """
        Update x-coordinate.

        Parameters
        ----------
        value : Int
            X-coordinate value.
        """
