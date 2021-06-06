"""Implementations of Circle class.
"""

from typing import Any
from typing import Union

from apysc import Int
from apysc.display.radius_interface import RadiusInterface
from apysc.display.line_base import LineBase

_Graphics = Any


class Circle(LineBase, RadiusInterface):

    def __init__(
            self,
            parent: _Graphics,
            x: Union[int, Int],
            y: Union[int, Int],
            radius: Union[int, Int]) -> None:
        """
        Create a circle vector graphics.

        Parameters
        ----------
        parent : Graphics
            Graphics instance to link this graphics.
        x : int or Int
            X-coordinate of the circle center.
        y : int or Int
            Y-coordinate of the circle center.
        radius : int or Int
            Circle radius.
        """
        from apysc.expression import expression_variables_util
        from apysc.expression import var_names
        from apysc.validation import size_validation
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.CIRCLE)
        super(Circle, self).__init__(
            parent=parent, x=x, y=y, variable_name=variable_name)
        size_validation.validate_size_is_gt_zero(size=radius)
        self._radius = self._get_converted_radius_int(radius=radius)
        self._set_initial_basic_values(parent=parent)
        self._append_constructor_expression()
        self._set_line_setting_if_not_none_value_exists(
            parent_graphics=parent)

    def _append_constructor_expression(self) -> None:
        """
        Append construcor expression to the file.
        """
        from apysc.display.stage import get_stage_variable_name
        from apysc.expression import expression_file_util
        from apysc.type import value_util
        stage_variable_name: str = get_stage_variable_name()
        radius_str: str = value_util.get_value_str_for_expression(
            value=self._radius)
        expression: str = (
            f'var {self.variable_name} = {stage_variable_name}'
            f'\n  .circle({radius_str})'
            '\n  .attr({'
        )
        expression = self._append_basic_vals_expression(
            expression=expression, indent_num=2)
        expression += '\n  });'
        expression_file_util.append_js_expression(expression=expression)

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            Type name and variable name will be set
            (e.g., `Circle('<variable_name>')`).
        """
        repr_str: str = f"Circle('{self.variable_name}')"
        return repr_str
