"""Dash setting class implementation for line.
"""

from typing import Union

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.dictionary import Dictionary
from apysc._type.int import Int


class LineDashSetting(Dictionary[str, Int]):
    """
    Dash setting class for a line.

    References
    ----------
    - Graphics line_style interface document
        - https://simon-ritchie.github.io/apysc/graphics_line_style.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.line_style(color='#fff', thickness=10)
    >>> line: ap.Line = sprite.graphics.draw_line(
    ...     x_start=50, y_start=50, x_end=150, y_end=50)
    >>> line.line_dash_setting = ap.LineDashSetting(
    ...     dash_size=5, space_size=2)
    >>> line.line_dash_setting.dash_size
    Int(5)

    >>> line.line_dash_setting.space_size
    Int(2)
    """

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='LineDashSetting')
    def __init__(
            self, dash_size: Union[int, Int],
            space_size: Union[int, Int]) -> None:
        """
        Dash setting class for a line.

        Parameters
        ----------
        dash_size : int or Int
            Dash size.
        space_size : int or Int
            Blank space size between dashes.

        References
        ----------
        - Graphics line_style interface document
            - https://simon-ritchie.github.io/apysc/graphics_line_style.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_dash_setting = ap.LineDashSetting(
        ...     dash_size=5, space_size=2)
        >>> line.line_dash_setting.dash_size
        Int(5)

        >>> line.line_dash_setting.space_size
        Int(2)
        """
        import apysc as ap
        from apysc._converter.to_apysc_val_from_builtin import \
            get_copied_int_from_builtin_val
        from apysc._validation import number_validation
        number_validation.validate_nums_are_int_and_gt_zero(
            nums=[dash_size, space_size])
        dash_size_: ap.Int = get_copied_int_from_builtin_val(
            integer=dash_size)
        space_size_: ap.Int = get_copied_int_from_builtin_val(
            integer=space_size)
        super(LineDashSetting, self).__init__({
            'dash_size': dash_size_,
            'space_size': space_size_,
        })

    @property
    def dash_size(self) -> Int:
        """
        Get a dash size setting.

        Returns
        -------
        dash_size : Int
            Dash size setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_dash_setting = ap.LineDashSetting(
        ...     dash_size=5, space_size=2)
        >>> line.line_dash_setting.dash_size
        Int(5)
        """
        from apysc._html.debug_mode import _DebugInfo
        with _DebugInfo(
                callable_='dash_size', args=[], kwargs={},
                module_name=__name__,
                class_name=LineDashSetting.__name__):
            return self['dash_size']

    @property
    def space_size(self) -> Int:
        """
        Get a space size setting.

        Returns
        -------
        space_size : Int
            Space size setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_dash_setting = ap.LineDashSetting(
        ...     dash_size=5, space_size=2)
        >>> line.line_dash_setting.space_size
        Int(2)
        """
        from apysc._html.debug_mode import _DebugInfo
        with _DebugInfo(
                callable_='space_size', args=[], kwargs={},
                module_name=__name__,
                class_name=LineDashSetting.__name__):
            return self['space_size']
