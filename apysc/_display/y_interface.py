"""Class implementation for the y-coordinate interface.
"""

from typing import Dict

from apysc._animation.animation_move_interface import AnimationMoveInterface
from apysc._animation.animation_y_interface import AnimationYInterface
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface
from apysc._validation import arg_validation_decos


class YInterface(
        AnimationYInterface, AnimationMoveInterface, RevertInterface,
        AttrLinkingInterface):

    _y: Int

    def _initialize_y_if_not_initialized(self) -> None:
        """
        Initialize the _y attribute if this instance does not
        initialize it yet.
        """
        if hasattr(self, '_y'):
            return
        self._y = Int(0)

        self._append_y_attr_linking_setting()

    @add_debug_info_setting(
        module_name=__name__, class_name='YInterface')
    def _append_y_attr_linking_setting(self) -> None:
        """
        Append a y attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._y, attr_name='y')
        self._append_attr_to_linking_stack(
            attr=self._y, attr_name='y')

    @property
    @add_debug_info_setting(
        module_name=__name__, class_name='YInterface')
    def y(self) -> Int:
        """
        Get a y-coordinate.

        Returns
        -------
        y : Int
            Y-coordinate.

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
        >>> rectangle.y = ap.Int(100)
        >>> rectangle.y
        Int(100)
        """
        import apysc as ap
        from apysc._type import value_util
        self._initialize_y_if_not_initialized()
        y: ap.Int = value_util.get_copy(value=self._y)
        return y

    @y.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    def y(self, value: Int) -> None:
        """
        Update y-coordinate.

        Parameters
        ----------
        value : Int
            Y-coordinate value.

        References
        ----------
        - Display object x and y interfaces document
            - https://simon-ritchie.github.io/apysc/display_object_x_and_y.html  # noqa
        """
        from apysc._html.debug_mode import DebugInfo
        with DebugInfo(
                callable_='y', args=[value], kwargs={},
                module_name=__name__,
                class_name=YInterface.__name__):
            self._y = value
            self._y._append_incremental_calc_substitution_expression()
            self._append_y_update_expression()

            self._append_y_attr_linking_setting()

    @add_debug_info_setting(
        module_name=__name__, class_name='YInterface')
    def _append_y_update_expression(self) -> None:
        """
        Append y position updating expression.
        """
        import apysc as ap
        from apysc._type import value_util
        self._initialize_y_if_not_initialized()
        value_str: str = value_util.get_value_str_for_expression(
            value=self._y)
        expression: str = (
            f'{self.variable_name}.y({value_str});'
        )
        ap.append_js_expression(expression=expression)

    _y_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_y_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_y_snapshots',
            value=int(self._y._value), snapshot_name=snapshot_name)

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
        self._y._value = self._y_snapshots[snapshot_name]
