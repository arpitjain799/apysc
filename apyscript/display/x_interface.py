"""Class implementation for x position interface.
"""

from apyscript.type.number_value_interface import NumberValueInterface
from typing import Union
from apyscript.expression import expression_file_util
from apyscript.type.variable_name_interface import VariableNameInterface
from apyscript.validation import number_validation
from apyscript.type.int import Int


class XInterface(VariableNameInterface):

    _x: Union[int, Int] = Int(value=0)

    @property
    def x(self) -> Union[int, Int]:
        """
        Get x position.

        Returns
        -------
        x : Int
            X position.
        """
        return self._x

    @x.setter
    def x(self, value: Union[int, Int]) -> None:
        """
        Update x position.

        Parameters
        ----------
        value : int or Int
            X potision value.
        """
        if not isinstance(value, NumberValueInterface):
            number_validation.validate_integer(integer=value)
            value = Int(value=value)
        self._x = value
        self._append_x_update_expression()

    def _append_x_update_expression(self) -> None:
        """
        Append x position updating expression.
        """
        expression: str = (
            f'{self.variable_name}.x({self.x});'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)
