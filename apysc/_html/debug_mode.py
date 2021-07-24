"""Debugging mode setting interface implementations for the HTML
and JavaScript.
"""

import os
from typing import Any, Callable, Dict, Optional, Type


def set_debug_mode() -> None:
    """
    Set the debug mode for the HTML and JavaScript debugging.
    If this functions is called, the following setting will be applied:
    - HTML minify setting will be disabled.
    - Per each interface JavaScript divider string will be appended.
    """
    from apysc._expression import expression_file_util
    file_path: str = expression_file_util.DEBUG_MODE_SETTING_FILE_PATH
    with open(file_path, 'w') as f:
        f.write('1')


def is_debug_mode() -> bool:
    """
    Get a boolean value whether the current debug mode is enabled or not.

    Returns
    -------
    result : bool
        If the current debug mode is enabled, True will be returned.
    """
    from apysc._expression import expression_file_util
    file_path: str = expression_file_util.DEBUG_MODE_SETTING_FILE_PATH
    if not os.path.isfile(file_path):
        return False
    with open(file_path) as f:
        txt: str = f.read()
    if txt == '1':
        return True
    return False


def _get_callable_count_file_path(
        callable_: Callable,
        module_name: str,
        class_: Optional[Type] = None) -> str:
    """
    Get a specified callable count data file path.

    Parameters
    ----------
    callable_ : Callable
        Target function or method.
    module_name : str
        Module name. This value will be set the `__name__` value.
    class_ : Type or None, optional
        Target class type. If the target callable_ variable is not
        a method, this argument will be ignored.

    Returns
    -------
    file_path : str
        Target file path.
    """
    from apysc._expression import expression_file_util
    module_path: str = module_name.replace('.', '_')
    if class_ is None:
        class_name: str = ''
    else:
        class_name = f'_{class_.__name__}'
    file_path: str = os.path.join(
        expression_file_util.EXPRESSION_ROOT_DIR,
        f'callable_count_{module_path}{class_name}_{callable_.__name__}.txt'
    )
    return file_path


def _get_callable_count(
        callable_: Callable,
        module_name: str,
        class_: Optional[Type] = None) -> int:
    """
    Get a specified callable count number.

    Parameters
    ----------
    callable_ : Callable
        Target function or method.
    module_name : str
        Module name. This value will be set the `__name__` value.
    class_ : Type or None, optional
        Target class type. If the target callable_ variable is not
        a method, this argument will be ignored.

    Returns
    -------
    callable_count : int
        Target count number.
    """
    file_path: str = _get_callable_count_file_path(
        callable_=callable_,
        module_name=module_name,
        class_=class_)
    if not os.path.isfile(file_path):
        return 0
    with open(file_path) as f:
        txt: str = f.read()
    try:
        callable_count: int = int(txt)
    except Exception:
        return 0
    return callable_count


class DebugInfo:

    _callable: Callable
    _locals: Dict[str, Any]
    _module_name: str
    _class: Optional[Type]

    def __init__(
            self, callable_: Callable, locals_: Dict[str, Any],
            module_name: str,
            class_: Optional[Type] = None) -> None:
        """
        Save a debug information (append callable interface name
        comment and arguments information) to the JavaScript
        expression file.

        Notes
        -----
        If the debug mode setting is not enabled, saving will
        be skipped.

        Parameters
        ----------
        callable_ : Callable
            Target function or method.
        locals_ : dict
            Local variables. This value will be set by the `locals()`
            function.
        module_name : str
            Module name. This value will be set the `__name__` value.
        class_ : Type or None, optional
            Target class type. If the target callable_ variable is not
            a method, this argument will be ignored.
        """
        self._callable = callable_
        self._locals = locals_
        self._module_name = module_name
        self._class = class_
