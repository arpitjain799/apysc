from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import event_handler_scope
from apysc._expression import expression_file_util
from tests.testing_helper import assert_raises


class TestReturn:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__validate_current_scope_is_event_handler(self) -> None:
        expression_file_util.empty_expression()
        assert_raises(
            expected_error_class=Exception,
            func_or_method=ap.Return,
            match=(
                'The `Return` class can be instantiated only in an event '
                'handler scope.'))

        with event_handler_scope.HandlerScope():
            _: ap.Return = ap.Return()

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        expression_file_util.empty_expression()
        with event_handler_scope.HandlerScope():
            _: ap.Return = ap.Return()
        expression: str = expression_file_util.\
            get_current_event_handler_scope_expression()
        assert 'return;' in expression
