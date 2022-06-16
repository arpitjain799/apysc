"""Class implementation for the x-coordinate interface.
"""

from typing import Dict

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface
from apysc._validation import arg_validation_decos
from apysc._display.x_interface_base import XInterfaceBase


class XInterface(
        XInterfaceBase, RevertInterface, AttrLinkingInterface):

    _x: Int

    def _initialize_x_if_not_initialized(self) -> None:
        """
        Initialize the _x attribute if this instance does not
        initialize it yet.
        """
        if hasattr(self, '_x'):
            return
        self._x = Int(0)

        self._append_x_attr_linking_setting()

    @add_debug_info_setting(
        module_name=__name__, class_name='XInterface')
    def _append_x_attr_linking_setting(self) -> None:
        """
        Append an x attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._x, attr_name='x')
        self._append_attr_to_linking_stack(
            attr=self._x, attr_name='x')

    @property
    @add_debug_info_setting(
        module_name=__name__, class_name='XInterface')
    def x(self) -> Int:
        """
        Get a x-coordinate.

        Returns
        -------
        x : Int
            X-coordinate.

        References
        ----------
        - Display object x and y interfaces document
            - https://simon-ritchie.github.io/apysc/display_object_x_and_y.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> rectangle.x = ap.Int(100)
        >>> rectangle.x
        Int(100)
        """
        import apysc as ap
        from apysc._type import value_util
        self._initialize_x_if_not_initialized()
        x: ap.Int = value_util.get_copy(value=self._x)
        return x

    @x.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(
        module_name=__name__, class_name='XInterface')
    def x(self, value: Int) -> None:
        """
        Update x-coordinate.

        Parameters
        ----------
        value : Int
            X-coordinate value.

        References
        ----------
        - Display object x and y interfaces document
            - https://simon-ritchie.github.io/apysc/display_object_x_and_y.html  # noqa
        """
        self._x = value
        self._x._append_incremental_calc_substitution_expression()
        self._append_x_update_expression()

        self._append_x_attr_linking_setting()

    @add_debug_info_setting(
        module_name=__name__, class_name='XInterface')
    def _append_x_update_expression(self) -> None:
        """
        Append the x position updating expression.
        """
        import apysc as ap
        from apysc._type import value_util
        self._initialize_x_if_not_initialized()
        value_str: str = value_util.get_value_str_for_expression(
            value=self._x)
        expression: str = (
            f'{self.variable_name}.x({value_str});'
        )
        ap.append_js_expression(expression=expression)

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
            dict_name='_x_snapshots',
            value=int(self._x._value), snapshot_name=snapshot_name)

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
