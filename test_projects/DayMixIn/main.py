"""The test project for the DayMixIn class.

Command examples:
$ python test_projects/DayMixIn/main.py
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
    datetime_: ap.DateTime = ap.DateTime(year=2022, month=11, day=24)
    day: ap.Int = datetime_.day
    ap.assert_equal(day, 24)
    datetime_.day = ap.Int(25)
    ap.assert_equal(datetime_.day, 25)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == "__main__":
    main()
