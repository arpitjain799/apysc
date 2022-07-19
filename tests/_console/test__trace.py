from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_trace() -> None:
    stage: ap.Stage = ap.Stage()
    ap.trace(stage, 100, "Hello!")
    expression: str = expression_data_util.get_current_expression()
    expected: str = f'console.log({stage.variable_name}, "100", "Hello!");'
    assert expected in expression
