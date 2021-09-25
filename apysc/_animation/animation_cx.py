"""Class implementation for the center-x animation value.
"""

from typing import Dict
from typing import Generic
from typing import TypeVar
from typing import Union

import apysc as ap
from apysc._animation.animation_base import AnimationBase
from apysc._animation.easing import Easing
from apysc._type.variable_name_interface import VariableNameInterface

_T = TypeVar('_T', bound=VariableNameInterface)


class AnimationCx(AnimationBase[_T], Generic[_T]):
    """
    The animation class for a center-x coordinate.
    """

    _cx: ap.Int

    def __init__(
            self,
            target: _T,
            x: Union[int, ap.Int],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> None:
        """
        The animation class for a center-x coordinate.

        Parameters
        ----------
        target : VariableNameInterface
            A target instance of the animation target
            (e.g., `Circle` instance).
        x : int or Int
            Destination of the center x-coordinate.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationCx):
            from apysc._converter import to_apysc_val_from_builtin
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            variable_name: str = expression_variables_util.\
                get_next_variable_name(type_name=var_names.ANIMATION_CX)
            self._cx = to_apysc_val_from_builtin.\
                get_copied_int_from_builtin_val(integer=x)
            self._set_basic_animation_settings(
                target=target,
                duration=duration,
                delay=delay,
                easing=easing)
            super(AnimationCx, self).__init__(variable_name=variable_name)

    def _get_animation_func_expression(self) -> str:
        """
        Get a animation function expression.

        Returns
        -------
        expression : str
            Animation function expression.
        """
        from apysc._type import value_util
        cx_str: str = value_util.get_value_str_for_expression(value=self._cx)
        return f'\n  .cx({cx_str});'

    _cx_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_cx_snapshots'):
            self._cx_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._cx_snapshots[snapshot_name] = int(self._cx._value)

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._cx._value = self._cx_snapshots[snapshot_name]
