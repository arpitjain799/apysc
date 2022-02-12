"""Class implementation for the move animation value.
"""

from typing import Generic
from typing import TypeVar
from typing import Union

from apysc._animation.animation_base import AnimationBase
from apysc._animation.easing import Easing
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.variable_name_interface import VariableNameInterface

_T = TypeVar('_T', bound=VariableNameInterface)


class AnimationMove(AnimationBase[_T], Generic[_T]):
    """
    The animation class for moving x and y coordinates.

    References
    ----------
    - animation_move interface document
        - https://simon-ritchie.github.io/apysc/animation_move.html
    - Animation interfaces duration setting document
        - https://simon-ritchie.github.io/apysc/animation_duration.html
    - Animation interfaces delay setting document
        - https://simon-ritchie.github.io/apysc/animation_delay.html
    - Each animation interface return value document
        - https://simon-ritchie.github.io/apysc/animation_return_value.html  # noqa
    - Sequential animation setting document
        - https://simon-ritchie.github.io/apysc/sequential_animation.html
    - animation_parallel interface document
        - https://simon-ritchie.github.io/apysc/animation_parallel.html
    - Easing enum document
        - https://simon-ritchie.github.io/apysc/easing_enum.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color='#0af')
    >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    ...     x=50, y=50, width=50, height=50)
    >>> animation: ap.AnimationMove = rectangle.animation_move(
    ...     x=100, y=150,
    ...     duration=1500,
    ...     easing=ap.Easing.EASE_OUT_QUINT,
    ... )
    >>> _ = animation.start()
    """

    _x: Int
    _y: Int

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='AnimationMove')
    def __init__(
            self,
            *,
            target: _T,
            x: Union[int, Int],
            y: Union[int, Int],
            duration: Union[int, Int] = 3000,
            delay: Union[int, Int] = 0,
            easing: Easing = Easing.LINEAR) -> None:
        """
        The animation class for moving x and y coordinates.

        Parameters
        ----------
        target : VariableNameInterface
            A target instance of the animation target
            (e.g., `DisplayObject` instance).
        x : int or Int
            Destination of the x-coordinate.
        y : int or Int
            Destination of the y-coordinate.
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.
        """
        from apysc._converter import to_apysc_val_from_builtin
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        variable_name: str = expression_variables_util.\
            get_next_variable_name(type_name=var_names.ANIMATION_MOVE)
        self._x = to_apysc_val_from_builtin.\
            get_copied_int_from_builtin_val(integer=x)
        self._y = to_apysc_val_from_builtin.\
            get_copied_int_from_builtin_val(integer=y)
        self._set_basic_animation_settings(
            target=target,
            duration=duration,
            delay=delay,
            easing=easing)
        super(AnimationMove, self).__init__(variable_name=variable_name)

    def _get_animation_func_expression(self) -> str:
        """
        Get a animation function expression.

        Returns
        -------
        expression : str
            Animation function expression.
        """
        from apysc._type import value_util
        x_str: str = value_util.get_value_str_for_expression(value=self._x)
        y_str: str = value_util.get_value_str_for_expression(value=self._y)
        return f'\n  .move({x_str}, {y_str});'

    def _get_complete_event_in_handler_head_expression(self) -> str:
        """
        Get an expression to be inserted into the complete event
        handler's head.

        Returns
        -------
        expression : str
            An expression to insert into the complete event
            handler's head.
        """
        from apysc._display.x_interface import XInterface
        from apysc._display.y_interface import YInterface
        expression: str = ''
        if isinstance(self._target, XInterface):
            self._target._initialize_x_if_not_initialized()
            expression += (
                f'{self._target._x.variable_name} = '
                f'{self._x.variable_name};'
            )
        if isinstance(self._target, YInterface):
            self._target._initialize_y_if_not_initialized()
            expression += (
                f'\n{self._target._y.variable_name} = '
                f'{self._y.variable_name};'
            )
        return expression
