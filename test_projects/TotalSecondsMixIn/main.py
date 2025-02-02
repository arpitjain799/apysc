"""The test project for the `TotalSecondsMixIn` class.

Command examples:
$ python test_projects/TotalSecondsMixIn/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module), "test_output/"
)


def main() -> None:
    """
    Entry point of this test project.
    """
    ap.Stage(
        background_color="#333",
        stage_width=1000,
        stage_height=500,
        stage_elem_id="stage",
    )

    left_datetime: ap.DateTime = ap.DateTime(
        year=2022,
        month=12,
        day=24,
        millisecond=500,
    )
    right_datetime: ap.DateTime = ap.DateTime(year=2022, month=12, day=23)
    timedelta_: ap.TimeDelta = left_datetime - right_datetime
    ap.assert_equal(
        timedelta_.total_seconds(),
        60 * 60 * 24 + 0.5,
    )

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == "__main__":
    main()
