import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display.line_dash_dot_setting_interface import \
    LineDashDotSettingInterface
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import assert_raises


class TestLineDashDotSettingInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_dash_dot_setting_if_not_initialized(
            self) -> None:
        interface: LineDashDotSettingInterface = LineDashDotSettingInterface()
        interface._initialize_line_dash_dot_setting_if_not_initialized()
        assert interface._line_dash_dot_setting is None

        interface._line_dash_dot_setting = ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7)
        interface._initialize_line_dash_dot_setting_if_not_initialized()
        assert isinstance(
            interface._line_dash_dot_setting, ap.LineDashDotSetting)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_dash_dot_setting(self) -> None:
        interface: LineDashDotSettingInterface = LineDashDotSettingInterface()
        interface.variable_name = 'test_line_dash_dot_setting_interface'
        line_dash_dot_setting: ap.LineDashDotSetting = ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7)
        interface._line_dash_dot_setting = line_dash_dot_setting
        assert interface.line_dash_dot_setting == line_dash_dot_setting

        interface.line_dash_dot_setting = None
        assert interface.line_dash_dot_setting is None
        interface.line_dash_dot_setting = line_dash_dot_setting
        assert interface.line_dash_dot_setting == line_dash_dot_setting

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_line_dash_dot_setting_and_skip_appending_exp(
            self) -> None:
        interface: LineDashDotSettingInterface = LineDashDotSettingInterface()
        interface._update_line_dash_dot_setting_and_skip_appending_exp(
            value=None)
        assert interface._line_dash_dot_setting is None

        line_dash_dot_setting: ap.LineDashDotSetting = ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7)
        interface._update_line_dash_dot_setting_and_skip_appending_exp(
            value=line_dash_dot_setting)
        assert interface._line_dash_dot_setting == line_dash_dot_setting

        assert_raises(
            expected_error_class=TypeError,
            callable_=interface.
            _update_line_dash_dot_setting_and_skip_appending_exp,
            kwargs={'value': 10},
            match='Not supported line_dash_dot_setting type specified: ')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_line_dash_dot_setting_update_expression(self) -> None:
        expression_data_util.empty_expression()
        interface: LineDashDotSettingInterface = LineDashDotSettingInterface()
        interface.variable_name = 'test_line_dash_dot_setting_interface'
        interface._initialize_line_dash_dot_setting_if_not_initialized()
        interface._append_line_dash_dot_setting_update_expression()
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.css("stroke-dasharray", "");'
        )
        assert expected in expression

        expression_data_util.empty_expression()
        interface._line_dash_dot_setting = ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7)
        interface._append_line_dash_dot_setting_update_expression()
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{interface.variable_name}.css\("stroke-dasharray", '
                rf'String\(.*?\) \+ " " \+ '
                rf'String\(.+?\) \+ " " \+ '
                rf'String\(.+?\) \+ " " \+ '
                rf'String\(.+?\)\);'
            ),
            string=expression, flags=re.MULTILINE)
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: LineDashDotSettingInterface = LineDashDotSettingInterface()
        line_dash_dot_setting: ap.LineDashDotSetting = ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7)
        interface._line_dash_dot_setting = line_dash_dot_setting
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._line_dash_dot_setting_snapshots == {
            snapshot_name: line_dash_dot_setting}

        interface._line_dash_dot_setting = None
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._line_dash_dot_setting_snapshots == {
            snapshot_name: line_dash_dot_setting}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: LineDashDotSettingInterface = LineDashDotSettingInterface()
        line_dash_dot_setting: ap.LineDashDotSetting = ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7)
        interface._line_dash_dot_setting = line_dash_dot_setting
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface._line_dash_dot_setting = None
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface._line_dash_dot_setting == line_dash_dot_setting
