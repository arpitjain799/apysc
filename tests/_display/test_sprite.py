from random import randint
from typing import List

from retrying import retry

import apysc as ap
from apysc._display.graphics import Graphics
from apysc._display.stage import get_stage_variable_name
from apysc._expression import expression_data_util
from apysc._testing import testing_helper


class TestSprite:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(
            variable_name_suffix='test_sprite')
        testing_helper.assert_attrs(
            expected_attrs={
                'stage': stage,
                '_variable_name_suffix': 'test_sprite',
            },
            any_obj=sprite)
        testing_helper.assert_attrs_type(
            expected_types={
                'graphics': Graphics,
            },
            any_obj=sprite)
        assert sprite.graphics._variable_name_suffix == \
            'test_sprite__graphics'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_add_child(self) -> None:
        ap.Stage()
        parent_sprite: ap.Sprite = ap.Sprite()
        child_sprite: ap.Sprite = ap.Sprite()
        parent_sprite.add_child(child=child_sprite)
        assert parent_sprite._children == ap.Array(
            [parent_sprite.graphics, child_sprite])

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_constructor_expression(self) -> None:
        ap.Stage()
        stage_variable_name: str = get_stage_variable_name()
        sprite: ap.Sprite = ap.Sprite()
        expression: str = expression_data_util.get_current_expression()
        expected_strs: List[str] = [
            f'\nvar {sprite.variable_name} = {stage_variable_name}.nested();',
            f'\nvar {sprite.graphics.variable_name} = ',
            f'{stage_variable_name}.nested();',
            f'\n{sprite.variable_name}',
            f'.add({sprite.graphics.variable_name});'
        ]
        for expected_str in expected_strs:
            assert expected_str in expression, \
                f'{expected_str}\n-----------------\n{expression}'
        expression_data_util.empty_expression()

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.begin_fill(color='#333', alpha=0.5)
        snapshot_name: str = 'snapshot_1'
        sprite._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert (
            sprite.graphics._fill_color_snapshots[snapshot_name]
            == '#333333')
        assert (
            sprite.graphics._fill_alpha_snapshots[snapshot_name] == 0.5)

        sprite.graphics.clear()
        sprite._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert (
            sprite.graphics._fill_color_snapshots[snapshot_name]
            == '#333333')
        assert (
            sprite.graphics._fill_alpha_snapshots[snapshot_name] == 0.5)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.begin_fill(color='#333', alpha=0.5)
        snapshot_name: str = 'snapshot_1'
        sprite._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        sprite.graphics.clear()
        sprite._run_all_revert_methods(snapshot_name=snapshot_name)
        assert sprite.graphics.fill_color == '#333333'
        assert sprite.graphics.fill_alpha == 0.5

        sprite.graphics.clear()
        sprite._run_all_revert_methods(snapshot_name=snapshot_name)
        assert sprite.graphics.fill_alpha == 1.0

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___repr__(self) -> None:
        ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        repr_str: str = repr(sprite)
        assert repr_str == f"Sprite('{sprite.variable_name}')"
