from random import randint
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display.line_style_interface import LineStyleInterface
from apysc._testing import testing_helper


class TestLineStyleInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
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

        line_style_interface.line_style(color=ap.String('222'))
        assert line_style_interface.line_color == '#222222'

        line_dot_setting: ap.LineDotSetting = ap.LineDotSetting(dot_size=5)
        line_style_interface.line_style(
            color='#333',
            cap=ap.LineCaps.ROUND,
            joints=ap.LineJoints.BEVEL,
            dot_setting=line_dot_setting)
        testing_helper.assert_attrs(
            expected_attrs={
                '_line_cap': ap.LineCaps.ROUND.value,
                '_line_joints': ap.LineJoints.BEVEL.value,
            },
            any_obj=line_style_interface)
        assert line_style_interface._line_dot_setting == line_dot_setting

        line_dash_setting: ap.LineDashSetting = ap.LineDashSetting(
            dash_size=5, space_size=2)
        line_style_interface.line_style(
            color='#333',
            dash_setting=line_dash_setting)
        assert line_style_interface._line_dash_setting == line_dash_setting

        line_round_dot_setting: ap.LineRoundDotSetting = \
            ap.LineRoundDotSetting(round_size=10, space_size=5)
        line_style_interface.line_style(
            color='#333',
            round_dot_setting=line_round_dot_setting)
        assert line_style_interface._line_round_dot_setting == \
            line_round_dot_setting

        line_dash_dot_setting: ap.LineDashDotSetting = ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=5)
        line_style_interface.line_style(
            color='#333', dash_dot_setting=line_dash_dot_setting)
        assert line_style_interface._line_dash_dot_setting == \
            line_dash_dot_setting

        line_style_interface.line_style(
            color='')
        assert line_style_interface.line_color == ''

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_color(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface.line_style(
            color='#333', thickness=3, alpha=0.5)
        assert line_style_interface.line_color == '#333333'

        line_color_1: ap.String = line_style_interface.line_color
        assert (line_color_1.variable_name
                != line_style_interface.line_color.variable_name)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_thickness(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface.line_style(
            color='#333', thickness=3, alpha=0.5)
        assert line_style_interface.line_thickness == 3

        line_thickness: ap.Int = line_style_interface.line_thickness
        assert (line_thickness.variable_name
                != line_style_interface.line_thickness.variable_name)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_alpha(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface.line_style(
            color='#333', thickness=3, alpha=0.5)
        assert line_style_interface.line_alpha == 0.5

        line_alpha: ap.Number = line_style_interface.line_alpha
        assert (line_alpha.variable_name
                != line_style_interface.line_alpha.variable_name)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_color_if_not_initialized(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface._initialize_line_color_if_not_initialized()
        assert line_style_interface.line_color == ''

        line_style_interface.line_style(
            color='#333', thickness=1, alpha=0.5)
        line_style_interface._initialize_line_color_if_not_initialized()
        assert line_style_interface.line_color == '#333333'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_thickness_if_not_initialized(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface._initialize_line_thickness_if_not_initialized()
        assert line_style_interface.line_thickness == 1

        line_style_interface.line_style(
            color='#333', thickness=2, alpha=0.5)
        line_style_interface._initialize_line_thickness_if_not_initialized()
        assert line_style_interface.line_thickness == 2

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_alpha_if_not_initialized(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface._initialize_line_alpha_if_not_initialized()
        assert line_style_interface.line_alpha == 1.0

        line_style_interface.line_style(
            color='#333', thickness=2, alpha=0.5)
        line_style_interface._initialize_line_alpha_if_not_initialized()
        assert line_style_interface.line_alpha == 0.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_dot_setting: ap.LineDotSetting = ap.LineDotSetting(dot_size=10)
        line_dash_setting: ap.LineDashSetting = ap.LineDashSetting(
            dash_size=10, space_size=5)
        line_round_dot_setting: ap.LineRoundDotSetting = \
            ap.LineRoundDotSetting(round_size=10, space_size=5)
        line_dash_dot_setting: ap.LineDashDotSetting = ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7)
        line_style_interface.line_style(
            color='#333', thickness=3, alpha=0.5, cap=ap.LineCaps.ROUND,
            joints=ap.LineJoints.BEVEL,
            dot_setting=line_dot_setting)
        line_style_interface._line_dash_setting = line_dash_setting
        line_style_interface._line_round_dot_setting = line_round_dot_setting
        line_style_interface._line_dash_dot_setting = line_dash_dot_setting
        snapshot_name: str = 'snapshot_1'
        line_style_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert (
            line_style_interface._line_color_snapshots[snapshot_name]
            == '#333333')
        assert (
            line_style_interface._line_thickness_snapshots[snapshot_name]
            == 3)
        assert (
            line_style_interface._line_alpha_snapshots[snapshot_name]
            == 0.5)
        assert (
            line_style_interface._line_cap_snapshots[snapshot_name]
            == ap.LineCaps.ROUND.value)
        assert (
            line_style_interface._line_joints_snapshots[snapshot_name]
            == ap.LineJoints.BEVEL.value)
        assert (
            line_style_interface._line_dot_setting_snapshots[
                snapshot_name] == line_dot_setting)
        assert (
            line_style_interface._line_dash_setting_snapshots[
                snapshot_name] == line_dash_setting)
        assert (
            line_style_interface._line_round_dot_setting_snapshots[
                snapshot_name] == line_round_dot_setting)
        assert(
            line_style_interface._line_dash_dot_setting_snapshots[
                snapshot_name] == line_dash_dot_setting)

        line_style_interface.line_style(
            color='#222', thickness=2, alpha=0.3)
        line_style_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert (
            line_style_interface._line_color_snapshots[snapshot_name]
            == '#333333')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_dot_setting: ap.LineDotSetting = ap.LineDotSetting(dot_size=10)
        line_dash_setting: ap.LineDashSetting = ap.LineDashSetting(
            dash_size=10, space_size=5)
        line_round_dot_setting: ap.LineRoundDotSetting = \
            ap.LineRoundDotSetting(round_size=10, space_size=5)
        line_dash_dot_setting: ap.LineDashDotSetting = ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7)
        line_style_interface.line_style(
            color='#333', thickness=3, alpha=0.5, cap=ap.LineCaps.ROUND,
            joints=ap.LineJoints.BEVEL, dot_setting=line_dot_setting)
        line_style_interface._line_dash_setting = line_dash_setting
        line_style_interface._line_round_dot_setting = line_round_dot_setting
        line_style_interface._line_dash_dot_setting = line_dash_dot_setting
        snapshot_name: str = 'snapshot_1'
        line_style_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        line_style_interface.line_style(
            color='#222', thickness=2, alpha=0.3, cap=ap.LineCaps.BUTT,
            joints=ap.LineJoints.MITER,
            dot_setting=ap.LineDotSetting(dot_size=20))
        line_style_interface._line_dash_setting = None
        line_style_interface._line_round_dot_setting = None
        line_style_interface._line_dash_dot_setting = None
        line_style_interface._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert line_style_interface.line_color == '#333333'
        assert line_style_interface.line_thickness == 3
        assert line_style_interface.line_alpha == 0.5
        assert line_style_interface.line_cap == ap.LineCaps.ROUND.value
        assert line_style_interface.line_joints == ap.LineJoints.BEVEL.value
        assert line_style_interface.line_dot_setting == line_dot_setting
        assert line_style_interface.line_dash_setting == line_dash_setting
        assert line_style_interface.line_round_dot_setting == \
            line_round_dot_setting
        assert line_style_interface.line_dash_dot_setting == \
            line_dash_dot_setting

        line_style_interface.line_style(
            color='#222', thickness=2, alpha=0.3)
        line_style_interface._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert line_style_interface.line_color == '#222222'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_line_cap(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface.line_style(color='#333')
        assert line_style_interface._line_cap == ap.LineCaps.BUTT.value

        line_style_interface.line_style(color='#333', cap=ap.LineCaps.ROUND)
        assert line_style_interface._line_cap == ap.LineCaps.ROUND.value

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=line_style_interface.line_style,
            kwargs={
                'color': '#333',
                'cap': 'round',
            },
            match=r'Specified cap style type is not LineCaps or String one: ')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_cap(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_cap: ap.String = line_style_interface.line_cap
        assert line_cap == ap.LineCaps.BUTT.value

        line_style_interface.line_style(color='#333', cap=ap.LineCaps.ROUND)
        line_cap = line_style_interface.line_cap
        assert line_cap == ap.LineCaps.ROUND.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_cap_if_not_initialized(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface._initialize_line_cap_if_not_initialized()
        assert line_style_interface._line_cap == ap.LineCaps.BUTT.value

        line_style_interface._line_cap = ap.String(ap.LineCaps.ROUND.value)
        line_style_interface._initialize_line_cap_if_not_initialized()
        assert line_style_interface._line_cap == ap.LineCaps.ROUND.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_line_joints(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface.line_style(color='#333')
        assert line_style_interface._line_joints == ap.LineJoints.MITER.value

        line_style_interface.line_style(
            color='#333', joints=ap.LineJoints.BEVEL)
        assert line_style_interface._line_joints == ap.LineJoints.BEVEL.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_joints_if_not_initialized(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface._initialize_line_joints_if_not_initialized()
        assert line_style_interface._line_joints == ap.LineJoints.MITER.value

        line_style_interface._line_joints = ap.String(
            ap.LineJoints.BEVEL.value)
        line_style_interface._initialize_line_joints_if_not_initialized()
        assert line_style_interface._line_joints == ap.LineJoints.BEVEL.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_joints(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface.line_style(
            color='#333', joints=ap.LineJoints.BEVEL)
        assert line_style_interface.line_joints == ap.LineJoints.BEVEL.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_dot_setting(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_dot_setting: Optional[ap.LineDotSetting] = \
            line_style_interface.line_dot_setting
        assert line_dot_setting is None

        line_style_interface.line_style(
            color='#333', dot_setting=ap.LineDotSetting(dot_size=10))
        line_dot_setting = line_style_interface.line_dot_setting
        assert line_dot_setting.dot_size == 10  # type: ignore
        assert isinstance(line_dot_setting, ap.LineDotSetting)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_dot_setting_if_not_initialized(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface._initialize_line_dot_setting_if_not_initialized()
        line_dot_setting: Optional[ap.LineDotSetting] = \
            line_style_interface.line_dot_setting
        assert line_dot_setting is None

        line_style_interface.line_style(
            color='#333', dot_setting=ap.LineDotSetting(dot_size=10))
        line_style_interface._initialize_line_dot_setting_if_not_initialized()
        line_dot_setting = line_style_interface.line_dot_setting
        assert line_dot_setting.dot_size == 10  # type: ignore

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_dash_setting_if_not_initialized(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface._initialize_line_dash_setting_if_not_initialized()
        assert line_style_interface._line_dash_setting is None

        line_style_interface._line_dash_setting = ap.LineDashSetting(
            dash_size=10, space_size=5)
        line_style_interface._initialize_line_dash_setting_if_not_initialized()
        assert line_style_interface._line_dash_setting is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_dash_setting(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_dash_setting: Optional[ap.LineDashSetting] = \
            line_style_interface.line_dash_setting
        assert line_dash_setting is None

        line_style_interface.line_style(
            color='#333',
            dash_setting=ap.LineDashSetting(dash_size=10, space_size=5))
        line_dash_setting = line_style_interface.line_dash_setting
        assert line_dash_setting.dash_size == 10  # type: ignore

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_round_dot_setting_if_not_initialized(
            self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface.\
            _initialize_line_round_dot_setting_if_not_initialized()
        assert line_style_interface._line_round_dot_setting is None

        line_style_interface._line_round_dot_setting = ap.LineRoundDotSetting(
            round_size=10, space_size=5)
        line_style_interface.\
            _initialize_line_round_dot_setting_if_not_initialized()
        assert isinstance(
            line_style_interface._line_round_dot_setting,
            ap.LineRoundDotSetting)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_round_dot_setting(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_round_dot_setting: Optional[ap.LineRoundDotSetting] = \
            line_style_interface.line_round_dot_setting
        assert line_round_dot_setting is None

        line_style_interface.line_style(
            color='#333',
            round_dot_setting=ap.LineRoundDotSetting(
                round_size=10, space_size=5))
        line_round_dot_setting = line_style_interface.line_round_dot_setting
        assert isinstance(line_round_dot_setting, ap.LineRoundDotSetting)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_dash_dot_setting_if_not_initialized(
            self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_style_interface.\
            _initialize_line_dash_dot_setting_if_not_initialized()
        assert line_style_interface._line_dash_dot_setting is None

        line_style_interface._line_dash_dot_setting = ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7)
        line_style_interface.\
            _initialize_line_dash_dot_setting_if_not_initialized()
        assert isinstance(
            line_style_interface._line_dash_dot_setting,
            ap.LineDashDotSetting)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_dash_dot_setting(self) -> None:
        line_style_interface: LineStyleInterface = LineStyleInterface()
        line_dash_dot_setting: Optional[ap.LineDashDotSetting] = \
            line_style_interface.line_dash_dot_setting
        assert line_dash_dot_setting is None

        line_style_interface._line_dash_dot_setting = ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7)
        line_dash_dot_setting = line_style_interface.line_dash_dot_setting
        assert isinstance(line_dash_dot_setting, ap.LineDashDotSetting)
