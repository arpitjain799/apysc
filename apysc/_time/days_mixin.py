"""Class implementations for the days-related mix-in.
"""

from typing import TYPE_CHECKING
from datetime import datetime
from datetime import timedelta

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos
from apysc._time.left_and_right_datetimes_mixin import LeftAndRightDatetimesMixIn

if TYPE_CHECKING:
    from apysc._time.datetime_ import DateTime


class DaysMixIn(
    VariableNameMixIn, VariableNameSuffixAttrMixIn, LeftAndRightDatetimesMixIn):

    _days_value: int

    @final
    @arg_validation_decos.is_apysc_datetime(arg_position_index=1)
    @arg_validation_decos.is_apysc_datetime(arg_position_index=2)
    @add_debug_info_setting(module_name=__name__)
    def _set_init_days_value_for_python(
        self,
        *,
        left_datetime: "DateTime",
        right_datetime: "DateTime",
    ) -> None:
        """
        Set an initial days value for Python.

        Parameters
        ----------
        left_datetime : DateTime
            A left-side `DateTime` instance to compare.
        right_datetime : DateTime
            A right-side `DateTime` instance to compare.
        """
        left_py_datetime: datetime
        right_py_datetime: datetime
        (
            left_py_datetime,
            right_py_datetime,
        ) = self._get_left_and_right_py_datetimes_from_apysc_datetime(
            left_apysc_datetime=left_datetime,
            right_apysc_datetime=right_datetime,
        )
        timedelta_: timedelta = left_py_datetime - right_py_datetime
        self._days_value = timedelta_.days
