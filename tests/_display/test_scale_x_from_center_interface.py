from random import randint

from retrying import retry

import apysc as ap
from apysc._display.scale_x_from_center_interface import \
    ScaleXFromCenterInterface
from apysc._expression import expression_file_util


class _TestInterface(ScaleXFromCenterInterface):

    def __init__(self) -> None:
        """
        The class for the testing of the ScaleXFromCenterInterface.
        """
        self.variable_name = 'scale_x_from_center_interface'


class TestScaleXFromCenterInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_scale_x_from_center_if_not_initialized(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_scale_x_from_center_if_not_initialized()
        assert interface._scale_x_from_center == 1.0
        interface._scale_x_from_center._value = 0.5
        interface._initialize_scale_x_from_center_if_not_initialized()
        assert interface._scale_x_from_center == 0.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_scale_x_from_center(self) -> None:
        interface: _TestInterface = _TestInterface()
        assert interface.scale_x_from_center == 1.0
        interface.scale_x_from_center = ap.Number(0.5)
        assert interface.scale_x_from_center == 0.5

        interface.scale_x_from_center = 0.3  # type: ignore
        assert interface.scale_x_from_center == 0.3

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_scale_x_from_center_update_expression(self) -> None:
        expression_file_util.empty_expression()
        interface: _TestInterface = _TestInterface()
        num_1: ap.Number = ap.Number(0.5)
        num_2: ap.Number = ap.Number(0.3)
        interface.scale_x_from_center = num_1
        interface.scale_x_from_center = num_2
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.scale(1 / {num_1.variable_name}, 1);'
            f'\n{interface.variable_name}.scale({num_2.variable_name}, 1);'
            f'\n{num_1.variable_name} = {num_2.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface.scale_x_from_center = ap.Number(0.5)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._scale_x_from_center_snapshots[snapshot_name] == 0.5
        interface.scale_x_from_center = ap.Number(0.3)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._scale_x_from_center_snapshots[snapshot_name] == 0.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface.scale_x_from_center = ap.Number(0.5)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.scale_x_from_center = ap.Number(0.3)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.scale_x_from_center == 0.5

        interface.scale_x_from_center = ap.Number(0.3)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.scale_x_from_center == 0.3
