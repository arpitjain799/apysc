"""Class implementation for ellipse the width interface.
"""

from typing import Dict

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class EllipseWidthInterface(
        VariableNameInterface, RevertInterface, AttrLinkingInterface):

    _ellipse_width: Int

    def _initialize_ellipse_width_if_not_initialized(self) -> None:
        """
        Initialize _ellipse_width attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_ellipse_width'):
            return
        self._ellipse_width = Int(0)

        self._append_ellipse_width_attr_linking_setting()

    @add_debug_info_setting(  # type: ignore
        module_name=__name__, class_name='EllipseWidthInterface')
    def _append_ellipse_width_attr_linking_setting(self) -> None:
        """
        Append a ellipse-height attribute linking setting.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._ellipse_width, attr_name='ellipse_width')
        self._append_attr_to_linking_stack(
            attr=self._ellipse_width, attr_name='ellipse_width')

    @property
    def ellipse_width(self) -> Int:
        """
        Get ellipse width value.

        Returns
        -------
        ellipse_width : Int
            Ellipse width value.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> rectangle.ellipse_width = ap.Int(10)
        >>> rectangle.ellipse_height = ap.Int(15)
        >>> rectangle.ellipse_width
        Int(10)
        """
        from apysc._html.debug_mode import _DebugInfo
        with _DebugInfo(
                callable_='ellipse_height', args=[], kwargs={},
                module_name=__name__,
                class_name=EllipseWidthInterface.__name__):
            from apysc._type import value_util
            self._initialize_ellipse_width_if_not_initialized()
            return value_util.get_copy(value=self._ellipse_width)

    @ellipse_width.setter
    def ellipse_width(self, value: Int) -> None:
        """
        Update ellipse width value.

        Parameters
        ----------
        value : int or Int
            Ellipse width value.
        """
        from apysc._html.debug_mode import _DebugInfo
        with _DebugInfo(
                callable_='ellipse_height', args=[], kwargs={},
                module_name=__name__,
                class_name=EllipseWidthInterface.__name__):
            import apysc as ap
            from apysc._validation import number_validation
            number_validation.validate_integer(integer=value)
            if isinstance(value, int):
                value = ap.Int(value)
            self._ellipse_width = value
            self._ellipse_width.\
                _append_incremental_calc_substitution_expression()
            self._append_ellipse_width_update_expression()

            self._append_ellipse_width_attr_linking_setting()

    @add_debug_info_setting(  # type: ignore
        module_name=__name__, class_name='EllipseWidthInterface')
    def _append_ellipse_width_update_expression(self) -> None:
        """
        Append ellipse width updating expression.
        """
        import apysc as ap
        from apysc._type import value_util
        self._initialize_ellipse_width_if_not_initialized()
        width_value_str: str = value_util.get_value_str_for_expression(
            value=self._ellipse_width)
        if hasattr(self, '_ellipse_height'):
            height_value_str: str = value_util.\
                get_value_str_for_expression(
                    value=getattr(self, '_ellipse_height'))
        else:
            height_value_str = value_util.get_value_str_for_expression(
                value=0)
        expression: str = (
            f'{self.variable_name}.radius({width_value_str}, '
            f'{height_value_str});'
        )
        ap.append_js_expression(expression=expression)

    _ellipse_width_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make the value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_ellipse_width_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_ellipse_width_snapshots',
            value=int(self._ellipse_width._value),
            snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert the value if the snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._ellipse_width._value = self._ellipse_width_snapshots[
            snapshot_name]
