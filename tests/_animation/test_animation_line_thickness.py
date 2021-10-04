from random import randint

from retrying import retry

import apysc as ap
from apysc._display.line_thickness_interface import LineThicknessInterface
from apysc._expression import var_names
from tests.testing_helper import assert_attrs


class TestAnimationLineThickness:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: LineThicknessInterface = LineThicknessInterface()
        target.variable_name = 'test_line_thickness_interface'
        animation_line_thickness: ap.AnimationLineThickness = \
            ap.AnimationLineThickness(
                target=target, thickness=3, duration=1000, delay=500,
                easing=ap.Easing.EASE_OUT_QUINT)
        assert animation_line_thickness.variable_name.startswith(
            f'{var_names.ANIMATION_LINE_THICKNESS}_')
        assert_attrs(
            expected_attrs={
                '_target': target,
                '_line_thickness': 3,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_line_thickness)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: LineThicknessInterface = LineThicknessInterface()
        target.variable_name = 'test_line_thickness_interface'
        animation_line_thickness: ap.AnimationLineThickness = \
            ap.AnimationLineThickness(target=target, thickness=3)
        expression: str = animation_line_thickness.\
            _get_animation_func_expression()
        assert expression == (
            '\n  .attr({"stroke-width": '
            f'{animation_line_thickness._line_thickness.variable_name}}});'
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: LineThicknessInterface = LineThicknessInterface()
        target.variable_name = 'test_line_thickness_interface'
        animation_line_thickness: ap.AnimationLineThickness = \
            ap.AnimationLineThickness(target=target, thickness=3)
        expression: str = animation_line_thickness.\
            _get_complete_event_in_handler_head_expression()
        assert expression == (
            f'{target._line_thickness.variable_name} = '
            f'{animation_line_thickness._line_thickness.variable_name};'
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        target: LineThicknessInterface = LineThicknessInterface()
        target.variable_name = 'test_line_thickness_interface'
        animation_line_thickness: ap.AnimationLineThickness = \
            ap.AnimationLineThickness(target=target, thickness=3)
        snapshot_name: str = animation_line_thickness.\
            _get_next_snapshot_name()
        animation_line_thickness._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_line_thickness._line_thickness_snapshots[
            snapshot_name] == 3

        animation_line_thickness._line_thickness.value = 5
        animation_line_thickness._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert animation_line_thickness._line_thickness_snapshots[
            snapshot_name] == 3

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        target: LineThicknessInterface = LineThicknessInterface()
        target.variable_name = 'test_line_thickness_interface'
        animation_line_thickness: ap.AnimationLineThickness = \
            ap.AnimationLineThickness(target=target, thickness=3)
        snapshot_name: str = animation_line_thickness.\
            _get_next_snapshot_name()
        animation_line_thickness._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        animation_line_thickness._line_thickness.value = 5
        animation_line_thickness._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert animation_line_thickness._line_thickness == 3

        animation_line_thickness._line_thickness.value = 5
        animation_line_thickness._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert animation_line_thickness._line_thickness == 5
