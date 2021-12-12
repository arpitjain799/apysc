"""Interface class implementation for the path control y data.
"""

from apysc._type.int import Int


class PathControlYInterface:

    _control_y: Int

    @property
    def control_y(self) -> Int:
        """
        Get a Y-coordinate of the control point.

        Returns
        -------
        control_y : Int
            Y-coordinate of the control point.
        """
        return self._control_y

    @control_y.setter
    def control_y(self, value: Int) -> None:
        """
        Set a Y-coordinate of the control point.

        Parameters
        ----------
        value : Int
            Y-coordinate of the control point.
        """
        self._control_y.value = value
