"""Class implementation for graphics clear method related interface.
"""


from typing import Optional

from apysc import Array
from apysc import Int
from apysc import Number
from apysc import String
from apysc.display.line_dash_setting import LineDashSetting
from apysc.display.line_dot_setting import LineDotSetting
from apysc.display.polyline import Polyline


class GraphicsClearInterface:

    _fill_color: String
    _fill_alpha: Number
    _line_color: String
    _line_thickness: Int
    _line_alpha: Number
    _children: Array
    _current_line: Optional[Polyline]
    _line_cap: String
    _line_joints: String
    _line_dot_setting: Optional[LineDotSetting]
    _line_dash_setting: Optional[LineDashSetting]

    def clear(self) -> None:
        """
        Clear all graphics and reset fill and line settings.
        """
        from apysc import LineCaps
        from apysc import LineJoints
        from apysc.display.begin_fill_interface import BeginFillInterface
        from apysc.display.child_interface import ChildInterface
        from apysc.display.fill_alpha_interface import FillAlphaInterface
        from apysc.display.fill_color_interface import FillColorInterface
        from apysc.display.line_alpha_interface import LineAlphaInterface
        from apysc.display.line_color_interface import LineColorInterface
        from apysc.display.line_style_interface import LineStyleInterface
        from apysc.display.line_thickness_interface import \
            LineThicknessInterface
        if isinstance(self, (FillColorInterface, BeginFillInterface)):
            self._initialize_fill_color_if_not_initialized()
        self._fill_color.value = ''
        if isinstance(self, (FillAlphaInterface, BeginFillInterface)):
            self._initialize_fill_alpha_if_not_initialized()
        self._fill_alpha.value = 1.0
        if isinstance(self, (LineColorInterface, LineStyleInterface)):
            self._initialize_line_color_if_not_initialized()
        self._line_color.value = ''
        if isinstance(self, (LineThicknessInterface, LineStyleInterface)):
            self._initialize_line_thickness_if_not_initialized()
        self._line_thickness.value = 1
        if isinstance(self, (LineAlphaInterface, LineStyleInterface)):
            self._initialize_line_alpha_if_not_initialized()
        self._line_alpha.value = 1.0
        if isinstance(self, ChildInterface):
            self._initialize_children_if_not_initialized()
        while self._children:
            self._children[0].remove_from_parent()
        if hasattr(self, '_current_line'):
            self._current_line = None
        if hasattr(self, '_line_cap'):
            self._line_cap = String(LineCaps.BUTT.value)
        if hasattr(self, '_line_joints'):
            self._line_joints = String(LineJoints.MITER.value)
        self._line_dot_setting = None
        self._line_dash_setting = None
