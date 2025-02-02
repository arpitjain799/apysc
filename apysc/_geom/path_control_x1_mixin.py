"""Mix-in class implementation for the first control x path data.
"""

from typing import Dict
from typing import Optional

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.number import Number
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class PathControlX1MixIn(
    VariableNameSuffixAttrOrVarMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
    VariableNameSuffixMixIn,
):

    _control_x1: Number

    @final
    def _initialize_control_x1_if_not_initialized(self) -> None:
        """
        Initialize the _control_x1 attribute if this instance does not
        initialize it yet.
        """
        if hasattr(self, "_control_x1"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="control_x1"
        )
        self._control_x1 = Number(
            0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_control_x1_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_control_x1_linking_setting(self) -> None:
        """
        Append a control_x1 attribute to the linking setting.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._control_x1, attr_name="control_x1"
        )
        self._append_attr_to_linking_stack(
            attr=self._control_x1, attr_name="control_x1"
        )

    @property
    @add_debug_info_setting(module_name=__name__)
    def control_x1(self) -> Number:
        """
        Get a first x-coordinate of the control point.

        Returns
        -------
        control_x1 : Number
            First x-coordinate of the control point.

        Examples
        --------
        >>> import apysc as ap
        >>> bezier_3d: ap.PathBezier3D = ap.PathBezier3D(
        ...     control_x1=50,
        ...     control_y1=0,
        ...     control_x2=100,
        ...     control_y2=0,
        ...     dest_x=150,
        ...     dest_y=50,
        ... )
        >>> bezier_3d.control_x1 = ap.Number(75)
        >>> bezier_3d.control_x1
        Number(75.0)
        """
        self._initialize_control_x1_if_not_initialized()
        return self._control_x1._copy()

    @control_x1.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def control_x1(self, value: Number) -> None:
        """
        Set a first x-coordinate of the control point.

        Parameters
        ----------
        value : Number
            First x-coordinate of the control point.
        """
        self._initialize_control_x1_if_not_initialized()
        self._control_x1.value = value

        self._append_control_x1_linking_setting()

    _control_x1_snapshots: Optional[Dict[str, float]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_control_x1_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_control_x1_snapshots",
            value=float(self._control_x1._value),
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_control_x1_if_not_initialized()
        self._control_x1._value = self._get_snapshot_val_if_exists(
            current_value=self._control_x1._value,
            snapshot_dict=self._control_x1_snapshots,
            snapshot_name=snapshot_name,
        )
