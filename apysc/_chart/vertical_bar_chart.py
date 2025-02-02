# mypy: disable-error-code=assignment

"""Class implementation for the vertical bar chart.
"""

from typing import Dict
from typing import List
from typing import TypeVar
from typing import Union

from apysc._chart.background_container_mixin import BackgroundContainerMixIn
from apysc._chart.chart_container_mixin import ChartContainerMixIn
from apysc._chart.initialize_each_container_mixin import InitializeEachContainerMixIn
from apysc._chart.overall_container_mixin import OverallContainerMixIn
from apysc._chart.set_initial_background_fill_alpha_mixin import (
    SetInitialBackgroundFillAlphaMixIn,
)
from apysc._chart.set_initial_background_fill_color_mixin import (
    SetInitialBackgroundFillColorMixIn,
)
from apysc._chart.set_initial_border_alpha_mixin import SetInitialBorderAlphaMixIn
from apysc._chart.set_initial_border_color_mixin import SetInitialBorderColorMixIn
from apysc._chart.set_initial_border_thickness_mixin import (
    SetInitialBorderThicknessMixIn,
)
from apysc._chart.set_initial_height_mixin import SetInitialHeightMixIn
from apysc._chart.set_initial_width_mixin import SetInitialWidthMixIn
from apysc._chart.set_initial_x_mixin import SetInitialXMixIn
from apysc._chart.set_initial_y_mixin import SetInitialYMixIn
from apysc._chart.x_axis_settings import XAxisSettings
from apysc._chart.y_axis_single_column_settings import YAxisSingleColumnSettings
from apysc._type.array import Array
from apysc._type.dictionary import Dictionary
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn

_DataType = Union[
    Array[Dictionary[String, Union[Int, Number, String]]],
    List[Dict[str, Union[int, float, str]]],
]
_StrOrString = TypeVar("_StrOrString", str, String)


class VerticalBarChart(
    VariableNameSuffixMixIn,
    SetInitialXMixIn,
    SetInitialYMixIn,
    SetInitialWidthMixIn,
    SetInitialHeightMixIn,
    SetInitialBackgroundFillColorMixIn,
    SetInitialBackgroundFillAlphaMixIn,
    SetInitialBorderColorMixIn,
    SetInitialBorderAlphaMixIn,
    SetInitialBorderThicknessMixIn,
    OverallContainerMixIn,
    BackgroundContainerMixIn,
    ChartContainerMixIn,
    InitializeEachContainerMixIn,
):
    """
    The class for the vertical bar chart.
    """

    _data: _DataType
    _x_axis_settings: XAxisSettings
    _y_axis_settings: YAxisSingleColumnSettings

    def __init__(
        self,
        *,
        data: _DataType,
        x_axis_settings: XAxisSettings,
        y_axis_settings: YAxisSingleColumnSettings,
        x: Union[float, Number] = 0,
        y: Union[float, Number] = 0,
        width: Union[int, Int] = 640,
        height: Union[int, Int] = 395,
        background_fill_color: _StrOrString = "#ffffff",
        background_fill_alpha: Union[float, Number] = 1.0,
        border_color: _StrOrString = "",
        border_alpha: Union[float, Number] = 1.0,
        border_thickness: Union[int, Int] = 1,
        variable_name_suffix: str = "",
    ) -> None:
        """
        Create a vertical bar chart instance.

        Parameters
        ----------
        data : Union[Array[Dictionary[String, Union[Int, Number, String]]], List[Dict[str, Union[int, float, str]]]]  # noqa
            A data array, which contains a 1-dimensional string key dictionary.
            A list of dictionaries or an `ap.Array` of `ap.Dictionary` values
            are acceptable.
            E.g., `[{"column_name_1": 10, "column_name_2"}]`
        x_axis_settings : XAxisSettings
            An x-axis setting.
        y_axis_settings : YAxisSingleColumnSettings
            A y-axis setting.
        x : Union[Number]
            A chart's x-coordinate.
        y : Union[float, Number]
            A chart's y-coordinate.
        width : Union[int, Int], default 640
            A chart's width.
        height : Union[int, Int], default 395
            A chart's height.
        background_fill_color : str or String, default "#ffffff"
            A chart's background fill-color.
        background_fill_alpha : Union[float, Number], default 1.0
            A chart's background fill-alpha.
        border_color : str or String, default ""
            A chart's border color.
        border_alpha : Union[float, Number], default 1.0
            A chart's border alpha.
        border_thickness : Union[int, Int], default 1
            A chart's border thickness.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        self._data = data
        self._x_axis_settings = x_axis_settings
        self._y_axis_settings = y_axis_settings
        self._set_initial_x(x=x, variable_name_suffix=variable_name_suffix)
        self._set_initial_y(y=y, variable_name_suffix=variable_name_suffix)
        self._set_initial_width(width=width, variable_name_suffix=variable_name_suffix)
        self._set_initial_height(
            height=height, variable_name_suffix=variable_name_suffix
        )
        self._set_initial_background_fill_color(
            background_fill_color=background_fill_color,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_background_fill_alpha(
            background_fill_alpha=background_fill_alpha,
            variable_name_suffix=variable_name_suffix,
        )
        self._set_initial_border_color(
            border_color=border_color, variable_name_suffix=variable_name_suffix
        )
        self._set_initial_border_alpha(
            border_alpha=border_alpha, variable_name_suffix=variable_name_suffix
        )
        self._set_initial_border_thickness(
            border_thickness=border_thickness, variable_name_suffix=variable_name_suffix
        )
        self._initialize_each_container(variable_name_suffix=variable_name_suffix)
        self._variable_name_suffix = variable_name_suffix
