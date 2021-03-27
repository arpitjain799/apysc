"""If condition implementations.
"""

from typing import Any, List
from typing import Dict
from typing import Type

from apysc.type import Boolean


class If:

    _condition: Boolean
    _locals: Dict[str, Any]
    _globals: Dict[str, Any]

    def __init__(
            self,
            condition: Boolean,
            locals_: Dict[str, Any],
            globals_: Dict[str, Any]) -> None:
        """
        A class to append if branch instruction expression.

        Parameters
        ----------
        condition : Boolean
            Boolean value to be used for judgment.
        locals_ : dict
            Current scope's local variables. Set locals() value to
            this argument.
        globals_ : dict
            Current scope's golobal variables. Set golobals() value
            to this argument.
        """
        self._condition = condition
        self._locals = locals_
        self._globals = globals_

    def __enter__(self) -> None:
        """
        Method to be called when begining of with statement.
        """
        from apysc.type import revert_interface
        revert_interface.make_snapshots_of_each_scope_vars(
            locals_=self._locals, globals_=self._globals)

    def __exit__(
            self, exc_type: Type,
            exc_value: Any,
            traceback: Any) -> None:
        pass
