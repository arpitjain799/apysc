"""Path data class implementation for the svg's `horizontal line` (H).
"""

from typing import Union

from apysc._converter.to_apysc_val_from_builtin import \
    get_copied_int_from_builtin_val
from apysc._geom.path_data_base import PathDataBase
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.string import String
from apysc._geom.update_path_data_interface import UpdatePathDataInterface


class PathHorizontal(PathDataBase, UpdatePathDataInterface):
    """
    Path data class for the svg's `horizontal line` (H).
    """

    _x: Int

    def __init__(
            self, x: Union[int, Int], *,
            relative: Union[bool, Boolean] = False) -> None:
        """
        Path data class for the svg's `horizontal line` (H).

        Parameters
        ----------
        x : int or Int
            X-coordinate of the destination point.
        relative : bool or Boolean, default False
            The boolean value indicating whether the path
            coordinates are relative or not (absolute).
        """
        from apysc._geom.path_label import PathLabel
        super(PathHorizontal, self).__init__(
            path_label=PathLabel.HORIZONTAL,
            relative=relative)
        self._x = get_copied_int_from_builtin_val(integer=x)

    def _get_svg_str(self) -> str:
        """
        Get a path's SVG string created with the current setting.

        Returns
        -------
        svg_str : str
            A path's SVG string created with the current setting.
        """
        from apysc._type import value_util
        svg_char: String = self._get_svg_char()
        svg_char_str: str = value_util.get_value_str_for_expression(
            value=svg_char)
        x_str: str = value_util.get_value_str_for_expression(value=self._x)
        svg_str: str = f'{svg_char_str} + String({x_str})'
        return svg_str

    def update_path_data(
            self, x: Union[int, Int],
            relative: Union[bool, Boolean]) -> None:
        """
        Update the path's data settings.

        Parameters
        ----------
        x : int or Int
            X-coordinate of the destination point.
        relative : bool or Boolean, default False
            The boolean value indicating whether the path
            coordinates are relative or not (absolute).
        """
        self._x.value = x
        self._relative.value = relative
