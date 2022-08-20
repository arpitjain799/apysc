"""Class implementation for the center x-coordinate interface.
"""

from typing import Dict
from typing import Union

from apysc._animation.animation_cx_interface import AnimationCxInterface
from apysc._display.x_interface_base import XInterfaceBase
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_suffix_attr_interface import (
    VariableNameSuffixAttrInterface,
)
from apysc._validation import arg_validation_decos


class CxInterface(
    XInterfaceBase,
    VariableNameSuffixAttrInterface,
    AnimationCxInterface,
    RevertInterface,
    AttrLinkingInterface,
):
    def _initialize_x_if_not_initialized(self) -> None:
        """
        Initialize _x attribute if this interface does not
        initialize it yet.
        """
        if hasattr(self, "_x"):
            return
        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="x")
        self._x = Int(
            0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_x_attr_linking_setting()

    @add_debug_info_setting(module_name=__name__)
    def _append_x_attr_linking_setting(self) -> None:
        """
        Append x attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(new_attr=self._x, attr_name="x")
        self._append_attr_to_linking_stack(attr=self._x, attr_name="x")

    @property
    @add_debug_info_setting(module_name=__name__)
    def x(self) -> Int:
        """
        Get a center x-coordinate.

        Returns
        -------
        x : Int
            Center x-coordinate.

        References
        ----------
        - Display object x and y interfaces document
            - https://simon-ritchie.github.io/apysc/en/display_object_x_and_y.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)
        >>> circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)
        >>> circle.x = ap.Int(120)
        >>> circle.x
        Int(120)
        """
        import apysc as ap
        from apysc._type import value_util

        self._initialize_x_if_not_initialized()
        x: ap.Int = value_util.get_copy(value=self._x)
        return x

    @x.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def x(self, value: Int) -> None:
        """
        Update a center x-coordinate.

        Parameters
        ----------
        value : Int
            Center x-coordinate value.

        References
        ----------
        - Display object x and y interfaces document
            - https://simon-ritchie.github.io/apysc/en/display_object_x_and_y.html  # noqa
        """
        self._x = value
        self._x._append_incremental_calc_substitution_expression()
        self._append_x_update_expression()

        self._append_x_attr_linking_setting()

    def _append_x_update_expression(self) -> None:
        """
        Append x position updating expression.
        """
        import apysc as ap
        from apysc._type import value_util

        self._initialize_x_if_not_initialized()
        value_str: str = value_util.get_value_str_for_expression(value=self._x)
        expression: str = f"{self.variable_name}.cx({value_str});"
        ap.append_js_expression(expression=expression)

    def _update_x_and_skip_appending_exp(self, *, x: Union[int, Int]) -> None:
        """
        Update x-coordinate and skip appending an expression.

        Parameters
        ----------
        x : int or Int
            X-coordinate value.
        """
        if isinstance(x, Int):
            x_: Int = x
        else:
            suffix: str = self._get_attr_variable_name_suffix(attr_identifier="x")
            x_ = Int(x, variable_name_suffix=suffix)
        self._x = x_

    _x_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_x_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_x_snapshots",
            value=int(self._x._value),
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._x._value = self._x_snapshots[snapshot_name]
