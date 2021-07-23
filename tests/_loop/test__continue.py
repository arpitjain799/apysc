from random import randint

from retrying import retry

import apysc as ap
from tests.testing_helper import assert_raises
from apysc._expression import expression_file_util


class TestContinue:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        expression_file_util.empty_expression_dir()
        assert_raises(
            expected_error_class=Exception,
            func_or_method=ap.Continue,
        )

        arr: ap.Array = ap.Array([1, 2, 3])
        with ap.For(arr):
            ap.Continue()
        expression: str = expression_file_util.get_current_expression()
        assert 'continue;' in expression
