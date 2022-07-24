"""Class implementation for the stop_propagation interface.
"""

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.variable_name_interface import VariableNameInterface


class StopPropagationInterface(VariableNameInterface):
    @add_debug_info_setting(module_name=__name__)
    def stop_propagation(self) -> None:
        """
        Stop event propagation.

        References
        ----------
        - Event class prevent_default and stop_propagation interfaces document
            - https://simon-ritchie.github.io/apysc/en/event_prevent_default_and_stop_propagation.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> def on_click(e: ap.MouseEvent, options: dict) -> None:
        ...     e.stop_propagation()
        ...     ap.trace("Clicked!")
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = sprite.click(on_click)
        >>> _ = rectangle.click(on_click)
        """
        import apysc as ap

        expression: str = f"{self.variable_name}.stopPropagation();"
        ap.append_js_expression(expression=expression)
