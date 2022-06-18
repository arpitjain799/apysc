"""Implementations for DisplayObject class.
"""

from typing import TYPE_CHECKING

from apysc._animation.animation_parallel_interface import \
    AnimationParallelInterface
from apysc._display.css_interface import CssInterface
from apysc._display.parent_interface import ParentInterface
from apysc._display.visible_interface import VisibleInterface
from apysc._display.x_interface_base import XInterfaceBase
from apysc._display.y_interface_base import YInterfaceBase
from apysc._event.custom_event_interface import CustomEventInterface
from apysc._event.mouse_event_interfaces import MouseEventInterfaces
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos

if TYPE_CHECKING:
    from apysc._display.stage import Stage


class DisplayObject(
        XInterfaceBase, YInterfaceBase, ParentInterface, MouseEventInterfaces,
        VisibleInterface, CustomEventInterface, CssInterface,
        AnimationParallelInterface):
    """
    Display object (base) class for the common interfaces.

    References
    ----------
    - DisplayObject document
        - https://simon-ritchie.github.io/apysc/en/display_object.html
    """

    stage: 'Stage'

    @arg_validation_decos.not_empty_string(arg_position_index=1)
    @add_debug_info_setting(
        module_name=__name__, class_name='DisplayObject')
    def __init__(self, *, variable_name: str) -> None:
        """
        Display object (base) class for the common interfaces.

        Parameters
        ----------
        variable_name : str
            Variable name of this instance. A js expression
            uses this setting.

        References
        ----------
        - DisplayObject document
            - https://simon-ritchie.github.io/apysc/en/display_object.html
        """
        import apysc as ap
        stage: ap.Stage = ap.get_stage()
        self.stage: ap.Stage = stage
        self._variable_name = variable_name

    @add_debug_info_setting(
        module_name=__name__, class_name='DisplayObject')
    def _set_overflow_visible_setting(self) -> None:
        """
        Set the `visible` value to the `overflow` CSS property.
        """
        self.set_css(name='overflow', value='visible')
