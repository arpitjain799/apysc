"""Class implementation for the mouse-down interface.
"""

from typing import Callable
from typing import Dict
from typing import Optional
from typing import TypeVar

from apysc._event.handler import HandlerData
from apysc._event.mouse_event import MouseEvent
from apysc._event.mouse_event_interface_base import MouseEventInterfaceBase
from apysc._html.debug_mode import add_debug_info_setting

_O = TypeVar('_O')
_Handler = Callable[[MouseEvent, _O], None]


class MouseDownInterface(MouseEventInterfaceBase):

    _mouse_down_handlers: Dict[str, HandlerData]

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='MouseDownInterface')
    def mousedown(
            self,
            handler: _Handler[_O],
            *,
            options: Optional[_O] = None) -> str:
        """
        Add mouse down event listener setting.

        Parameters
        ----------
        handler : _Handler
            Callable that would be called when mouse down
            on this instance.
        options : dict or None, default None
            Optional arguments dictionary to be passed to a handler.

        Returns
        -------
        name : str
            Handler's name.

        References
        ----------
        - Mousedown and mouseup interfaces document
            - https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html  # noqa
        - About the handler options' type document
            - https://simon-ritchie.github.io/apysc/about_handler_options_type.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mousedown(
        ...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String('#f0a')
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.mousedown(on_mousedown)
        """
        import apysc as ap
        from apysc._event.handler import append_handler_expression
        from apysc._event.handler import get_handler_name
        from apysc._type.variable_name_interface import VariableNameInterface
        from apysc._validation.handler_options_validation import \
            validate_options_type
        from apysc._validation.variable_name_validation import \
            validate_variable_name_interface_type
        self_instance: VariableNameInterface = \
            validate_variable_name_interface_type(instance=self)
        validate_options_type(options=options)
        self._initialize_mouse_down_handlers_if_not_initialized()
        name: str = get_handler_name(handler=handler, instance=self)
        self._set_mouse_event_handler_data(
            handler=handler, handlers_dict=self._mouse_down_handlers,
            options=options)
        self._append_mouse_event_binding_expression(
            name=name, mouse_event_type=ap.MouseEventType.MOUSEDOWN)
        e: ap.MouseEvent = ap.MouseEvent(this=self_instance)
        append_handler_expression(
            handler_data=self._mouse_down_handlers[name],
            handler_name=name, e=e)
        return name

    def _initialize_mouse_down_handlers_if_not_initialized(self) -> None:
        """
        Initialize _mouse_down_handlers attribute if this instance
        does not initialize it yet.
        """
        if hasattr(self, '_mouse_down_handlers'):
            return
        self._mouse_down_handlers = {}

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='MouseDownInterface')
    def unbind_mousedown(self, handler: _Handler[_O]) -> None:
        """
        Unbind a specified handler's mouse down event.

        Parameters
        ----------
        handler : _Handler
            Unbinding target Callable.

        References
        ----------
        - Mousedown and mouseup interfaces document
            - https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mousedown(
        ...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String('#f0a')
        ...     rectangle.unbind_mousedown(on_mousedown)
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.mousedown(on_mousedown)
        """
        import apysc as ap
        self._initialize_mouse_down_handlers_if_not_initialized()
        self._unbind_mouse_event(
            handler=handler, mouse_event_type=ap.MouseEventType.MOUSEDOWN,
            handlers_dict=self._mouse_down_handlers)

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='MouseDownInterface')
    def unbind_mousedown_all(self) -> None:
        """
        Unbind all mouse down events.

        References
        ----------
        - Mousedown and mouseup interfaces document
            - https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mousedown(
        ...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     rectangle: ap.Rectangle = e.this
        ...     rectangle.fill_color = ap.String('#f0a')
        ...     rectangle.unbind_mousedown_all()
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.mousedown(on_mousedown)
        """
        import apysc as ap
        self._initialize_mouse_down_handlers_if_not_initialized()
        self._unbind_all_mouse_events(
            mouse_event_type=ap.MouseEventType.MOUSEDOWN,
            handlers_dict=self._mouse_down_handlers)
