from typing import List

import apysc as ap
from apysc._display.svg_text import SVGText
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs
from tests._display.test_graphics_expression import (
    assert_fill_opacity_attr_expression_exists,
)
from tests._display.test_graphics_expression import (
    assert_stroke_opacity_attr_expression_exists,
)
from tests._display.test_graphics_expression import (
    assert_stroke_width_attr_expression_exists,
)


class TestSVGText:
    @apply_test_settings()
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        svg_text: SVGText = SVGText(
            text="test text",
            x=50,
            y=100,
            fill_color="#0af",
            fill_alpha=0.5,
            line_color="#fff",
            line_alpha=0.3,
            line_thickness=1,
            leading=1.8,
            bold=True,
            italic=True,
            variable_name_suffix="test_suffix",
        )
        assert var_names.SVG_TEXT in svg_text.variable_name
        assert_attrs(
            expected_attrs={
                "_x": 50,
                "_y": 100,
                "_fill_color": "#00aaff",
                "_fill_alpha": 0.5,
                "_line_color": "#ffffff",
                "_line_alpha": 0.3,
                "_line_thickness": 1,
                "_leading": 1.8,
                "_bold": True,
                "_italic": True,
                "_parent": stage,
            },
            any_obj=svg_text,
        )
        assert svg_text._variable_name_suffix == "test_suffix"
        assert "test_suffix" in svg_text.variable_name
        assert var_names.SVG_TEXT in svg_text.variable_name

        expression: str = expression_data_util.get_current_expression()
        assert "text(" in expression
        assert_fill_opacity_attr_expression_exists(expression=expression)
        assert_fill_opacity_attr_expression_exists(expression=expression)
        assert_stroke_opacity_attr_expression_exists(expression=expression)
        assert_stroke_width_attr_expression_exists(expression=expression)

    @apply_test_settings()
    def test___repr__(self) -> None:
        ap.Stage()
        svg_text: SVGText = SVGText(
            text="test text 1",
        )
        repr_str: str = repr(svg_text)
        expected: str = f'SVGText("{svg_text.variable_name}")'
        assert repr_str == expected

    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        svg_text: SVGText = SVGText(
            text="test text 1",
        )
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"var {svg_text.variable_name} = {stage.variable_name}" "\n  .text()"
        )
        assert expected in expression

    @apply_test_settings()
    def test__convert_text_spans_list_to_array(self) -> None:
        ap.Stage()
        svg_text: SVGText = SVGText(
            text="test text 1",
        )
        text_spans_: ap.Array[
            ap.SVGTextSpan
        ] = svg_text._convert_text_spans_list_to_array(
            text_spans=[
                ap.SVGTextSpan(text="test text 2"),
                ap.SVGTextSpan(text="test text 3"),
            ],
        )
        assert len(text_spans_._value) == 2
        assert text_spans_._value[0].text == "test text 2"
        assert text_spans_._value[1].text == "test text 3"

        text_spans__: ap.Array[
            ap.SVGTextSpan
        ] = svg_text._convert_text_spans_list_to_array(text_spans=text_spans_)
        assert text_spans_ == text_spans__

    @apply_test_settings()
    def test_create_with_svg_text_spans(self) -> None:
        stage: ap.Stage = ap.Stage()
        text_spans: List[ap.SVGTextSpan] = [
            ap.SVGTextSpan(text="a"),
            ap.SVGTextSpan(text="b"),
            ap.SVGTextSpan(text="c"),
        ]
        svg_text: ap.SVGText = ap.SVGText.create_with_svg_text_spans(
            text_spans=text_spans,
            font_size=14,
            font_family=["Arial", "Helvetica"],
            x=50,
            y=100,
            fill_color="#fff",
            fill_alpha=0.5,
            line_color="#0af",
            line_alpha=0.3,
            line_thickness=2,
            leading=1.8,
            align=ap.SVGTextAlign.CENTER,
            bold=True,
            italic=True,
            variable_name_suffix="test_svg_text",
        )
        expression: str = expression_data_util.get_current_expression()
        assert f"{svg_text.variable_name}.add(" in expression
        assert var_names.SVG_TEXT in svg_text.variable_name
        assert "test_svg_text" in svg_text.variable_name
        assert_attrs(
            expected_attrs={
                "_font_size": 14,
                "_x": 50,
                "_y": 100,
                "_fill_color": "#ffffff",
                "_fill_alpha": 0.5,
                "_line_color": "#00aaff",
                "_line_alpha": 0.3,
                "_line_thickness": 2,
                "_leading": 1.8,
                "_align": ap.SVGTextAlign.CENTER,
                "_bold": True,
                "_italic": True,
                "_parent": stage,
            },
            any_obj=svg_text,
        )
