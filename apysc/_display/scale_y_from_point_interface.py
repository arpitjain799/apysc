"""Class implementation for the scale_y_from_point interfaces.
"""

from typing import Any
from typing import Dict

import apysc as ap
from apysc._type.expression_string import ExpressionString
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class ScaleYFromPointInterface(VariableNameInterface, RevertInterface):

    _scale_y_from_point: ap.Dictionary[str, ap.Number]

    def _initialize_scale_y_from_point_if_not_initialized(self) -> None:
        """
        Initialize the `_scale_y_from_point` attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_scale_y_from_point'):
            return
        self._scale_y_from_point = ap.Dictionary({})

    def get_scale_y_from_point(self, y: ap.Int) -> ap.Number:
        """
        Get a scale-y value from the given y-coordinate.

        Parameters
        ----------
        y : Int
            Y-coordinate.

        Returns
        -------
        scale_y : ap.Number
            Scale-y value from the given y-coordinate.
        """
        with ap.DebugInfo(
                callable_=self.get_scale_y_from_point, locals_=locals(),
                module_name=__name__, class_=ScaleYFromPointInterface):
            from apysc._display import scale_interface_helper
            from apysc._validation import number_validation
            number_validation.validate_integer(integer=y)
            self._initialize_scale_y_from_point_if_not_initialized()
            default_val: ap.Number = ap.Number(1.0)
            key_exp_str: ExpressionString = scale_interface_helper.\
                get_coordinate_key_for_expression(coordinate=int(y._value))
            scale_y: ap.Number = self._scale_y_from_point.get(
                key=key_exp_str, default=default_val)
            return scale_y

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert a value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
