"""Class implementation for the parallel animation value.
"""

from typing import Generic, List
from typing import TypeVar
from typing import Union

import apysc as ap
from apysc._animation.animation_base import AnimationBase
from apysc._animation.easing import Easing
from apysc._type.variable_name_interface import VariableNameInterface

_T = TypeVar('_T', bound=VariableNameInterface)


class AnimationParallel(AnimationBase[_T], Generic[_T]):
    """
    The parallel animation setting class.
    """

    _animations: List[AnimationBase]

    def __init__(
            self,
            target: _T,
            animations: List[AnimationBase],
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> None:
        """
        The parallel animation setting class.

        Raises
        ------
        ValueError
            - If the animations's target is not unified.
            - If there are changed `duration`, `delay`, or
                `easing` animation settings in the `animations`
                list.

        Parameters
        ----------
        target : VariableNameInterface
            A target instance of the animation target
            (e.g., `DisplayObject` instance).
        animations : list of AnimationBase
            Target animations (e.g., `AnimationX`, `AnimationFillColor`).
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationParallel):
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            variable_name: str = expression_variables_util.\
                get_next_variable_name(type_name=var_names.ANIMATION_PARALLEL)
            self._animations = animations
            self._set_basic_animation_settings(
                target=target,
                duration=duration,
                delay=delay,
                easing=easing)
            super(AnimationParallel, self).__init__(variable_name=variable_name)
            self._validate_animation_targets_are_unified()

    def _validate_animation_targets_are_unified(self) -> None:
        """
        Validate whether the specified animation's targets are unified.

        Raises
        ------
        ValueError
            If the specified animation targets are not unified.
        """
        for animation in self._animations:
            if animation._target == self._target:
                continue
            err_msg: str = (
                'There is not unified animation target instance: '
                f'{animation._target} (type: {type(animation._target)})'
                f'\nExpected instance: {self._target} (type: '
                f'{type(self._target)})'
                f'\nPlease unify the animation targets of the '
                'animation_parallel interface argument.'
            )
            raise ValueError(err_msg)

    def _get_animation_func_expression(self) -> str:
        """
        Get a animation function expression.

        Returns
        -------
        expression : str
            Animation function expression.
        """
        expression: str = ''
        for i, animation in enumerate(self._animations):
            single_expression: str = \
                animation._get_animation_func_expression()
            single_expression = single_expression.replace(';', '')
            expression += single_expression
            if i == len(self._animations) - 1:
                expression += ';'
        return expression

    def _get_complete_event_in_handler_head_expression(self) -> str:
        """
        Get an expression to be inserted into the complete event
        handler's head.

        Returns
        -------
        expression : str
            An expression to be inserted into the complete event
            handler's head.
        """
        expression: str = ''
        for animation in self._animations:
            if expression != '':
                expression += '\n'
            single_expression: str = animation.\
                _get_complete_event_in_handler_head_expression()
            expression += single_expression
        return expression
