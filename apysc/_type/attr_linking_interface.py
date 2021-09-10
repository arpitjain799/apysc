"""Class implementation for the attribute linking interface.

This interface is used for updating an old property value to
achieve consistency in the handler functions.
"""

from typing import Dict, List, Union

import apysc as ap

_AttrName = str
_Attr = Union[ap.Int, ap.Number, ap.String, ap.Boolean]


class AttrLinkingInterface:

    _attr_linking_stack: Dict[_AttrName, List[_Attr]]

    def _initialize_attr_linking_stack(self, attr_name: str) -> None:
        """
        Initialize the _attr_linking_stack attribute if it hasn't been
        initialized yet.

        Parameters
        ----------
        attr_name : str
            Target attribute name.
        """
        if not hasattr(self, '_attr_linking_stack'):
            self._attr_linking_stack = {}
        if attr_name in self._attr_linking_stack:
            return
        self._attr_linking_stack[attr_name] = []

    def _append_attr_to_linking_stack(
            self, attr: _Attr, attr_name: str) -> None:
        """
        Append an attribute to the linking attribute stack.

        Parameters
        ----------
        attr : Int or Number or String or Boolean
            Target attribute to be appended.
        attr_name : str
            Target attribute name.
        """
        self._initialize_attr_linking_stack(attr_name=attr_name)
        self._attr_linking_stack[attr_name].append(attr)

    def _append_applying_new_attr_val_exp(
            self, new_attr: _Attr, attr_name: str) -> None:
        """
        Append the expression of applying new attribute value to each
        stacked value.

        Parameters
        ----------
        new_attr : Int or Number or String or Boolean
            New attribute value.

        attr_name : str
            Target attribute name.
        """
        self._initialize_attr_linking_stack(attr_name=attr_name)
        if not self._attr_linking_stack:
            return
        new_attr_name: str = new_attr.variable_name
        expression: str = ''
        for stacked_value in self._attr_linking_stack[attr_name]:
            if stacked_value.variable_name == new_attr_name:
                continue
            if expression != '':
                expression += '\n'
            expression += (
                f'{stacked_value.variable_name} = {new_attr_name};'
            )
        ap.append_js_expression(expression=expression)
