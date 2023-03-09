"""The mix-in class implementation for the `SVGText`'s `_set_italic` method.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean


class SVGTextSetItalicMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_italic(self, *, italic: Union[bool, Boolean]) -> None:
        """
        Set an italic style setting.

        Parameters
        ----------
        italic : Union[bool, Boolean]
            A boolean whether a text is in an italic style or not (normal).
        """
        from apysc._display.svg_text_italic_mixin import SVGTextItalicMixIn
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        if not isinstance(self, SVGTextItalicMixIn):
            raise TypeError(
                f"This method is only supported a {SVGTextItalicMixIn.__name__} "
                f"instance: {type(self).__name__}"
            )

        if isinstance(italic, bool):
            suffix: str = get_attr_or_variable_name_suffix(
                instance=self,
                value_identifier="italic",
            )
            italic_: Boolean = Boolean(italic, variable_name_suffix=suffix)
        else:
            italic_ = italic
        self.italic = italic_
