"""This module is for the SVG's `3D bezier curve` (C) path
data class implementation.
"""

from typing import Any
from typing import Union

from typing_extensions import final

from apysc._geom.path_control_x1_interface import PathControlX1Interface
from apysc._geom.path_control_x2_interface import PathControlX2Interface
from apysc._geom.path_control_y1_interface import PathControlY1Interface
from apysc._geom.path_control_y2_interface import PathControlY2Interface
from apysc._geom.path_data_base import PathDataBase
from apysc._geom.path_dest_x_mixin import PathDestXMixIn
from apysc._geom.path_dest_y_interface import PathDestYInterface
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.string import String
from apysc._validation import arg_validation_decos


class PathBezier3D(
    PathDataBase,
    PathDestXMixIn,
    PathDestYInterface,
    PathControlX1Interface,
    PathControlY1Interface,
    PathControlX2Interface,
    PathControlY2Interface,
):
    """
    Path data class for the SVG's `3D bezier curve` (C).

    References
    ----------
    - Path class
        - https://simon-ritchie.github.io/apysc/en/path.html
    - Graphics draw_path interface
        - https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html
    - PathBezier3D class
        - https://simon-ritchie.github.io/apysc/en/path_bezier_3d.html
    - PathBezier3DContinual class
        - https://simon-ritchie.github.io/apysc/en/path_bezier_3d_continual.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.line_style(color="#fff", thickness=3)
    >>> path: ap.Path = sprite.graphics.draw_path(
    ...     path_data_list=[
    ...         ap.PathMoveTo(x=0, y=50),
    ...         ap.PathBezier3D(
    ...             control_x1=0,
    ...             control_y1=0,
    ...             control_x2=50,
    ...             control_y2=0,
    ...             dest_x=50,
    ...             dest_y=50,
    ...         ),
    ...         ap.PathBezier3DContinual(
    ...             control_x=100, control_y=100, dest_x=100, dest_y=50
    ...         ),
    ...     ]
    ... )
    """

    @final
    @arg_validation_decos.is_integer(arg_position_index=1)
    @arg_validation_decos.is_integer(arg_position_index=2)
    @arg_validation_decos.is_integer(arg_position_index=3)
    @arg_validation_decos.is_integer(arg_position_index=4)
    @arg_validation_decos.is_integer(arg_position_index=5)
    @arg_validation_decos.is_integer(arg_position_index=6)
    @arg_validation_decos.is_boolean(arg_position_index=7)
    @arg_validation_decos.is_builtin_string(arg_position_index=8, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        control_x1: Union[int, Int],
        control_y1: Union[int, Int],
        control_x2: Union[int, Int],
        control_y2: Union[int, Int],
        dest_x: Union[int, Int],
        dest_y: Union[int, Int],
        *,
        relative: Union[bool, Boolean] = False,
        variable_name_suffix: str = "",
    ) -> None:
        """
        Path data class for the SVG's `3D bezier curve` (C).

        Parameters
        ----------
        control_x1 : Int or int
            X-coordinate of the bezier's first control point.
        control_y1 : Int or int
            Y-coordinate of the bezier's first control point.
        control_x2 : Int or int
            X-coordinate of the bezier's second control point.
        control_y2 : Int or int
            Y-coordinate of the bezier's second control point.
        dest_x : Int or int
            X-coordinate of the destination point.
        dest_y : Int or int
            Y-coordinate of the destination point.
        relative : bool or Boolean, default False
            A boolean value indicates whether the path
            coordinates are relative or not (absolute).
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript's debugging.

        References
        ----------
        - Path class
            - https://simon-ritchie.github.io/apysc/en/path.html
        - Graphics draw_path interface
            - https://simon-ritchie.github.io/apysc/en/graphics_draw_path.html
        - PathBezier3D class
            - https://simon-ritchie.github.io/apysc/en/path_bezier_3d.html
        - PathBezier3DContinual class
            - https://simon-ritchie.github.io/apysc/en/path_bezier_3d_continual.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color="#fff", thickness=3)
        >>> path: ap.Path = sprite.graphics.draw_path(
        ...     path_data_list=[
        ...         ap.PathMoveTo(x=0, y=50),
        ...         ap.PathBezier3D(
        ...             control_x1=0,
        ...             control_y1=0,
        ...             control_x2=50,
        ...             control_y2=0,
        ...             dest_x=50,
        ...             dest_y=50,
        ...         ),
        ...         ap.PathBezier3DContinual(
        ...             control_x=100, control_y=100, dest_x=100, dest_y=50
        ...         ),
        ...     ]
        ... )
        """
        from apysc._geom.path_label import PathLabel

        self._variable_name_suffix = variable_name_suffix
        super(PathBezier3D, self).__init__(
            path_label=PathLabel.BEZIER_3D, relative=relative
        )
        self.control_x1 = self._get_copied_int_from_builtin_val(
            integer=control_x1, attr_identifier="control_x1"
        )
        self.control_y1 = self._get_copied_int_from_builtin_val(
            integer=control_y1, attr_identifier="control_y1"
        )
        self.control_x2 = self._get_copied_int_from_builtin_val(
            integer=control_x2, attr_identifier="control_x2"
        )
        self.control_y2 = self._get_copied_int_from_builtin_val(
            integer=control_y2, attr_identifier="control_y2"
        )
        self.dest_x = self._get_copied_int_from_builtin_val(
            integer=dest_x, attr_identifier="dest_x"
        )
        self.dest_y = self._get_copied_int_from_builtin_val(
            integer=dest_y, attr_identifier="dest_y"
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_svg_str(self) -> str:
        """
        Get a path's SVG string created with the current setting.

        Returns
        -------
        svg_str : str
            An SVG path string was created with the current setting.
        """
        from apysc._type.value_util import get_value_str_for_expression

        svg_char: String = self._get_svg_char()
        svg_char_str: str = get_value_str_for_expression(value=svg_char)
        control_x1_str: str = get_value_str_for_expression(value=self._control_x1)
        control_y1_str: str = get_value_str_for_expression(value=self._control_y1)
        control_x2_str: str = get_value_str_for_expression(value=self._control_x2)
        control_y2_str: str = get_value_str_for_expression(value=self._control_y2)
        dest_x_str: str = get_value_str_for_expression(value=self._dest_x)
        dest_y_str: str = get_value_str_for_expression(value=self._dest_y)
        svg_str: str = (
            f"{svg_char_str} + String({control_x1_str}) "
            f'+ " " + String({control_y1_str}) '
            f'+ " " + String({control_x2_str}) '
            f'+ " " + String({control_y2_str}) '
            f'+ " " + String({dest_x_str}) '
            f'+ " " + String({dest_y_str})'
        )
        return svg_str

    @final
    @arg_validation_decos.is_integer(arg_position_index=1)
    @arg_validation_decos.is_integer(arg_position_index=2)
    @arg_validation_decos.is_integer(arg_position_index=3)
    @arg_validation_decos.is_integer(arg_position_index=4)
    @arg_validation_decos.is_integer(arg_position_index=5)
    @arg_validation_decos.is_integer(arg_position_index=6)
    @arg_validation_decos.is_boolean(arg_position_index=7)
    @add_debug_info_setting(module_name=__name__)
    def update_path_data(
        self,
        control_x1: Union[int, Int],
        control_y1: Union[int, Int],
        control_x2: Union[int, Int],
        control_y2: Union[int, Int],
        dest_x: Union[int, Int],
        dest_y: Union[int, Int],
        *,
        relative: Union[bool, Boolean] = False,
    ) -> None:
        """
        Update the path's data settings.

        Parameters
        ----------
        control_x1 : Int or int
            X-coordinate of the bezier's first control point.
        control_y1 : Int or int
            Y-coordinate of the bezier's first control point.
        control_x2 : Int or int
            X-coordinate of the bezier's second control point.
        control_y2 : Int or int
            Y-coordinate of the bezier's second control point.
        dest_x : Int or int
            X-coordinate of the destination point.
        dest_y : Int or int
            Y-coordinate of the destination point.
        relative : bool or Boolean, default False
            A boolean value indicates whether the path
            coordinates are relative or not (absolute).

        Examples
        --------
        >>> import apysc as ap
        >>> bezier_3d_continual = ap.PathBezier3D(
        ...     control_x1=0,
        ...     control_y1=0,
        ...     control_x2=50,
        ...     control_y2=0,
        ...     dest_x=50,
        ...     dest_y=50,
        ... )
        >>> bezier_3d_continual.update_path_data(
        ...     control_x1=100,
        ...     control_y1=100,
        ...     control_x2=150,
        ...     control_y2=100,
        ...     dest_x=150,
        ...     dest_y=150,
        ... )
        >>> bezier_3d_continual.control_x1
        Int(100)

        >>> bezier_3d_continual.control_y1
        Int(100)

        >>> bezier_3d_continual.control_x2
        Int(150)

        >>> bezier_3d_continual.control_y2
        Int(100)

        >>> bezier_3d_continual.dest_x
        Int(150)

        >>> bezier_3d_continual.dest_y
        Int(150)
        """
        self.control_x1 = self._get_copied_int_from_builtin_val(
            integer=control_x1, attr_identifier="control_x1"
        )
        self.control_y1 = self._get_copied_int_from_builtin_val(
            integer=control_y1, attr_identifier="control_y1"
        )
        self.control_x2 = self._get_copied_int_from_builtin_val(
            integer=control_x2, attr_identifier="control_x2"
        )
        self.control_y2 = self._get_copied_int_from_builtin_val(
            integer=control_y2, attr_identifier="control_y2"
        )
        self.dest_x = self._get_copied_int_from_builtin_val(
            integer=dest_x, attr_identifier="dest_x"
        )
        self.dest_y = self._get_copied_int_from_builtin_val(
            integer=dest_y, attr_identifier="dest_y"
        )
        self.relative = self._get_copied_boolean_from_builtin_val(
            bool_val=relative, attr_identifier="relative"
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def __eq__(self, other: Any) -> Any:
        """
        Equal comparison method.

        Parameters
        ----------
        other : Any
            The other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        import apysc as ap

        if not isinstance(other, PathBezier3D):
            result: ap.Boolean = ap.Boolean(
                False, variable_name_suffix=self._variable_name_suffix
            )
            return result
        return (
            self.control_x1 == other.control_x1
            and self.control_y1 == other.control_y1
            and self.control_x2 == other.control_x2
            and self.control_y2 == other.control_y2
            and self.dest_x == other.dest_x
            and self.dest_y == other.dest_y
            and self.relative == other.relative
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def __ne__(self, other: Any) -> Any:
        """
        Not equal comparison method.

        Parameters
        ----------
        other : Any
            The other value to compare.

        Returns
        -------
        result : Boolean
            Comparison result.
        """
        import apysc as ap

        result: ap.Boolean = self == other
        result = result.not_
        return result
