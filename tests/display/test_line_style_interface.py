from apyscript.display.line_style_interface import LineStyleInterface
from apyscript.type import Int
from apyscript.type import Number
from apyscript.type import String
from tests import testing_helper


class TestLineStyleInterface:

    def test_line_style(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface.line_style(
            color='#333', thickness=3, alpha=0.5)
        testing_helper.assert_attrs(
            expected_attrs={
                '_line_color': '#333333',
                '_line_thickness': 3,
                '_line_alpha': 0.5,
            },
            any_obj=line_style_interface)

        line_style_interface.line_style(color=String('222'))
        assert line_style_interface.line_color == '#222222'

    def test_line_color(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface.line_style(
            color='#333', thickness=3, alpha=0.5)
        assert line_style_interface.line_color == '#333333'

        line_color_1: String = line_style_interface.line_color
        assert (line_color_1.variable_name
                != line_style_interface.line_color.variable_name)

    def test_line_thickness(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface.line_style(
            color='#333', thickness=3, alpha=0.5)
        assert line_style_interface.line_thickness == 3

        line_thickness: Int = line_style_interface.line_thickness
        assert (line_thickness.variable_name
                != line_style_interface.line_thickness.variable_name)

    def test_line_alpha(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface.line_style(
            color='#333', thickness=3, alpha=0.5)
        assert line_style_interface.line_alpha == 0.5

        line_alpha: Number = line_style_interface.line_alpha
        assert (line_alpha.variable_name
                != line_style_interface.line_alpha.variable_name)

    def test__initialize_line_color_if_not_initialized(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface._initialize_line_color_if_not_initialized()
        assert line_style_interface.line_color == ''

        line_style_interface.line_style(
            color='#333', thickness=1, alpha=0.5)
        line_style_interface._initialize_line_color_if_not_initialized()
        assert line_style_interface.line_color == '#333333'

    def test__initialize_line_thickness_if_not_initialized(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface._initialize_line_thickness_if_not_initialized()
        assert line_style_interface.line_thickness == 1

        line_style_interface.line_style(
            color='#333', thickness=2, alpha=0.5)
        line_style_interface._initialize_line_thickness_if_not_initialized()
        assert line_style_interface.line_thickness == 2

    def test__initialize_line_alpha_if_not_initialized(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface._initialize_line_alpha_if_not_initialized()
        assert line_style_interface.line_alpha == 1.0

        line_style_interface.line_style(
            color='#333', thickness=2, alpha=0.5)
        line_style_interface._initialize_line_alpha_if_not_initialized()
        assert line_style_interface.line_alpha == 0.5
