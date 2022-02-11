"""Debugging mode setting interface implementations for the HTML
and JavaScript.
"""

import inspect
from typing import Any, List
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union, TypeVar

from apysc._expression.indent_num import Indent


def set_debug_mode() -> None:
    """
    Set the debug mode for the HTML and JavaScript debugging.
    This interface applies the following setting if calling this function:
    - Disabling HTML minify setting.
    - Changing to append per each interface JavaScript divider string.

    References
    ----------
    - set_debug_mode interface document
        - https://simon-ritchie.github.io/apysc/set_debug_mode.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> ap.set_debug_mode()
    >>> int_val: ap.Int = ap.Int(10)
    """
    from apysc._expression import expression_data_util
    table_name: str = expression_data_util.TableName.DEBUG_MODE_SETTING.value
    query: str = f'DELETE FROM {table_name};'
    expression_data_util.exec_query(sql=query, commit=False)
    query = f'INSERT INTO {table_name}(is_debug_mode) VALUES(1);'
    expression_data_util.exec_query(sql=query)


def unset_debug_mode() -> None:
    """
    Unset the debug mode for the HTML and JavaScript debugging.

    References
    ----------
    - unset_debug_mode interface document
        - https://simon-ritchie.github.io/apysc/unset_debug_mode.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> ap.set_debug_mode()
    >>> int_val: ap.Int = ap.Int(10)
    >>> ap.unset_debug_mode()
    """
    from apysc._expression import expression_data_util
    table_name: str = expression_data_util.TableName.DEBUG_MODE_SETTING.value
    query: str = f'DELETE FROM {table_name};'
    expression_data_util.exec_query(sql=query)


def is_debug_mode() -> bool:
    """
    Get a boolean value whether the current debug mode is enabled or not.

    Returns
    -------
    result : bool
        If the current debug mode is enabled, True will be returned.

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> ap.set_debug_mode()
    >>> ap.is_debug_mode()
    True

    >>> int_val: ap.Int = ap.Int(10)
    >>> ap.unset_debug_mode()
    >>> ap.is_debug_mode()
    False
    """
    from apysc._expression import expression_data_util
    table_name: str = expression_data_util.TableName.DEBUG_MODE_SETTING.value
    query: str = f'SELECT is_debug_mode FROM {table_name} LIMIT 1;'
    expression_data_util.exec_query(sql=query)
    result_: Optional[Tuple[int]] = expression_data_util.cursor.fetchone()
    if result_ is None:
        return False
    result: bool = bool(result_[0])
    return result


def _get_callable_str(*, callable_: Union[Callable, str]) -> str:
    """
    Get a callable string (label).

    Parameters
    ----------
    callable_ : Callable or str
        Target function or method or property or dunder method name.

    Returns
    -------
    callable_str : str
        A callable string (label).
    """
    if isinstance(callable_, str):
        callable_str: str = callable_
    else:
        callable_str = callable_.__name__
    return callable_str


def _get_callable_path_name(
        *,
        callable_: Union[Callable, str],
        module_name: str,
        class_: Optional[Union[Type, str]] = None) -> str:
    """
    Get a specified callable count data path name.

    Parameters
    ----------
    callable_ : Callable or str
        Target function or method or property or dunder method name.
    module_name : str
        Module name. This value will be set the `__name__` value.
    class_ : Type or str or None, optional
        Target class type or type name. If the target callable_
        variable is not a method, this argument will be ignored.

    Returns
    -------
    path_name : str
        Target path name.
    """
    module_path: str = module_name.replace('.', '_')
    if class_ is None:
        class_name: str = ''
    elif inspect.isclass(class_):
        class_name = f'_{class_.__name__}'
    else:
        class_name = f'_{class_}'
    callable_str: str = _get_callable_str(callable_=callable_)
    path_name: str = f'{module_path}{class_name}_{callable_str}'
    return path_name


def _get_callable_count(
        *,
        callable_: Union[Callable, str],
        module_name: str,
        class_: Optional[Union[Type, str]] = None) -> int:
    """
    Get a specified callable count number.

    Parameters
    ----------
    callable_ : Callable or str
        Target function or method or property or dunder method name.
    module_name : str
        Module name. This value will be set the `__name__` value.
    class_ : Type or str or None, optional
        Target class type or type name. If the target callable_
        variable is not a method, this argument will be ignored.

    Returns
    -------
    callable_count : int
        Target count number.
    """
    from apysc._expression import expression_data_util
    path_name: str = _get_callable_path_name(
        callable_=callable_, module_name=module_name, class_=class_)
    table_name: str = \
        expression_data_util.TableName.DEBUG_MODE_CALLABLE_COUNT.value
    query: str = (
        f'SELECT count FROM {table_name} '
        f"WHERE name = '{path_name}' LIMIT 1;"
    )
    expression_data_util.exec_query(sql=query)
    result: Optional[Tuple[int]] = expression_data_util.cursor.fetchone()
    if result is None:
        return 0
    return result[0]


def _increment_callable_count(
        *,
        callable_: Union[Callable, str],
        module_name: str,
        class_: Optional[Union[Type, str]] = None) -> None:
    """
    Increment a specified callable count number.

    Parameters
    ----------
    callable_ : Callable or str
        Target function or method or property or dunder method name.
    module_name : str
        Module name. This value will be set the `__name__` value.
    class_ : Type or str or None, optional
        Target class type or type name. If the target callable_
        variable is not a method, this argument will be ignored.
    """
    from apysc._expression import expression_data_util
    callable_count: int = _get_callable_count(
        callable_=callable_, module_name=module_name, class_=class_)
    callable_count += 1
    path_name: str = _get_callable_path_name(
        callable_=callable_, module_name=module_name, class_=class_)
    table_name: str = \
        expression_data_util.TableName.DEBUG_MODE_CALLABLE_COUNT.value
    query: str = (
        f'DELETE FROM {table_name} '
        f"WHERE name = '{path_name}';"
    )
    expression_data_util.exec_query(sql=query, commit=False)
    query = (
        f'INSERT INTO {table_name}(name, count) '
        f"VALUES ('{path_name}', {callable_count});"
    )
    expression_data_util.exec_query(sql=query)


class DebugInfo:
    """
    Save a debug information (append callable interface name
    comment and arguments information) to the JavaScript
    expression file. This class is used at the `with` statement.

    Notes
    -----
    If the debug mode setting is not enabled, saving will
    be skipped.

    References
    ----------
    - DebugInfo class document
        - https://simon-ritchie.github.io/apysc/debug_info.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> def any_func(a: int, b: str) -> None:
    ...     with ap.DebugInfo(
    ...             callable_=any_func, locals_=locals(),
    ...             module_name=__name__):
    ...         int_val: ap.Int = ap.Int(10)
    """

    _callable: Union[Callable, str]
    _locals: Dict[str, Any]
    _module_name: str
    _class: Optional[Union[Type, str]]
    _DIVIDER: str = '/' * 70
    _callable_count: int
    _indent: Indent

    def __init__(
            self, callable_: Union[Callable, str],
            locals_: Dict[str, Any],
            module_name: str,
            *,
            class_: Optional[Union[Type, str]] = None) -> None:
        """
        Save debug information (append callable interface
        name comment and arguments information) to the
        JavaScript expression file. This class needs
        to use the `with` statement when instantiating.

        Notes
        -----
        If the debug mode setting is not enabled,
        this interface skips the saving.

        Parameters
        ----------
        callable_ : Callable or str
            Target function or method or property or dunder method name.
        locals_ : dict
            Local variables. This value requires a `locals()`
            function's value.
        module_name : str
            Module name. This value requires the `__name__` value.
        class_ : Type or str None, optional
            Target class type or type name. If the target
            callable_ variable is not a method, this
            interface ignores this argument.

        References
        ----------
        - DebugInfo class document
            - https://simon-ritchie.github.io/apysc/debug_info.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> def any_func(a: int, b: str) -> None:
        ...     with ap.DebugInfo(
        ...             callable_=any_func, locals_=locals(),
        ...             module_name=__name__):
        ...         int_val: ap.Int = ap.Int(10)
        """
        self._callable = callable_
        self._locals = locals_
        self._module_name = module_name
        self._class = class_
        _increment_callable_count(
            callable_=callable_, module_name=module_name, class_=class_)
        self._callable_count = _get_callable_count(
            callable_=callable_, module_name=module_name, class_=class_)
        self._indent = Indent()

    def _get_class_info(self) -> str:
        """
        Get a class information string.

        Returns
        -------
        class_info : str
            Target class information string.
        """
        if self._class is None:
            class_info: str = ''
        elif inspect.isclass(self._class):
            class_info = f'\n// class: {self._class.__name__}'
        else:
            class_info = f'\n// class: {self._class}'
        return class_info

    def __enter__(self) -> None:
        """
        The method will be called at the start of the with block.
        """
        import apysc as ap
        from apysc._type.variable_name_interface import VariableNameInterface
        if not ap.is_debug_mode():
            return
        class_info: str = self._get_class_info()
        if not self._locals:
            arguments_info: str = ''
        else:
            arguments_info = '\n// arguments and variables:'
            for argument_name, argument in self._locals.items():
                if inspect.ismodule(argument):
                    continue
                if argument_name.startswith('__'):
                    continue
                if isinstance(argument, str):
                    argument = repr(argument)[1:-1]
                    argument = f"'{argument}'"
                if isinstance(argument, VariableNameInterface):
                    argument = f'{argument}({argument.variable_name})'
                arguments_info += f'\n//    {argument_name} = {argument}'
        callable_str: str = _get_callable_str(callable_=self._callable)
        expression: str = (
            f'{self._DIVIDER}'
            f'\n// [{callable_str} {self._callable_count}] '
            'started.'
            f'\n// module name: {self._module_name}'
            f'{class_info}'
            f'{arguments_info}'
        )
        ap.append_js_expression(expression=expression)
        self._indent.__enter__()

    def __exit__(self, *args: Any) -> None:
        """
        The method will be called at the end of the with block.

        Parameters
        ----------
        *args : list
            Positional arguments.
        """
        import apysc as ap
        if not ap.is_debug_mode():
            return
        class_info: str = self._get_class_info()
        callable_str: str = _get_callable_str(callable_=self._callable)
        expression: str = (
            f'// [{callable_str} {self._callable_count}] ended.'
            f'\n// module name: {self._module_name}'
            f'{class_info}'
            f'\n{self._DIVIDER}'
        )
        self._indent.__exit__()
        ap.append_js_expression(expression=expression)


class _DebugInfo:
    """
    Save a debug information (append callable interface name
    comment and arguments information) to the JavaScript
    expression file. This class is used at the `with` statement.

    Notes
    -----
    If the debug mode setting is not enabled, saving will
    be skipped.

    References
    ----------
    - DebugInfo class document
        - https://simon-ritchie.github.io/apysc/debug_info.html
    """

    _callable: Union[Callable, str]
    _module_name: str
    _args: List[Any]
    _kwargs: Dict[str, Any]
    _class_name: Optional[str]
    _DIVIDER: str = '/' * 70
    _callable_count: int
    _indent: Indent

    def __init__(
            self,
            *,
            callable_: Union[Callable, str],
            args: List[Any],
            kwargs: Dict[str, Any],
            module_name: str,
            class_name: Optional[str] = None) -> None:
        """
        Save debug information (append callable interface
        name comment and arguments information) to the
        JavaScript expression file. This class needs
        to use the `with` statement when instantiating.

        Notes
        -----
        If the debug mode setting is not enabled,
        this interface skips the saving.

        Parameters
        ----------
        callable_ : Callable or str
            Target function or method or property or dunder method name.
        args : list
            Function positional arguments.
        kwargs : dict
            Function keyword arguments.
        module_name : str
            Module name. This value requires the `__name__` value.
        class_name : str or None, optional
            Target class type name. If the target
            callable_ variable is not a method, this
            interface ignores this argument.
        """
        self._callable = callable_
        self._args = args
        self._kwargs = kwargs
        self._module_name = module_name
        self._class_name = class_name
        _increment_callable_count(
            callable_=callable_, module_name=module_name,
            class_=class_name)
        self._callable_count = _get_callable_count(
            callable_=callable_, module_name=module_name,
            class_=class_name)
        self._indent = Indent()

    def _get_class_info(self) -> str:
        """
        Get a class information string.

        Returns
        -------
        class_info : str
            Target class information string.
        """
        if self._class_name is None:
            class_info: str = ''
        else:
            class_info = f'\n// class: {self._class_name}'
        return class_info

    def __enter__(self) -> None:
        """
        The method will be called at the start of the with block.
        """
        import apysc as ap
        from apysc._type.variable_name_interface import VariableNameInterface
        if not ap.is_debug_mode():
            return
        class_info: str = self._get_class_info()
        arguments_info: str = ''
        if self._args:
            arguments_info += (
                f'\n// Positional arguments: {self._args}'
            )
        if self._kwargs:
            arguments_info += f'\n// Keyword arguments: {self._kwargs}'
        callable_str: str = _get_callable_str(callable_=self._callable)
        expression: str = (
            f'{self._DIVIDER}'
            f'\n// [{callable_str} {self._callable_count}] '
            'started.'
            f'\n// module name: {self._module_name}'
            f'{class_info}'
            f'{arguments_info}'
        )
        ap.append_js_expression(expression=expression)
        self._indent.__enter__()

    def __exit__(self, *args: Any) -> None:
        """
        The method will be called at the end of the with block.

        Parameters
        ----------
        *args : list
            Positional arguments.
        """
        import apysc as ap
        if not ap.is_debug_mode():
            return
        class_info: str = self._get_class_info()
        callable_str: str = _get_callable_str(callable_=self._callable)
        expression: str = (
            f'// [{callable_str} {self._callable_count}] ended.'
            f'\n// module name: {self._module_name}'
            f'{class_info}'
            f'\n{self._DIVIDER}'
        )
        self._indent.__exit__()
        ap.append_js_expression(expression=expression)


_F = TypeVar('_F', bound=Callable)


def add_debug_info_setting(
        module_name: str, *,
        class_name: Optional[str] = None) -> _F:
    """
    Set a debug information setting to a target
    callable object (decorator function).

    Parameters
    ----------
    module_name : str
        A target module name.
    class_name : str or None, default None
        Target class name. If a target callable is
        function, this interface requires None of
        this argument.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(func: _F) -> _F:
        """
        Wrapping function for a decorator setting.

        Parameters
        ----------
        func : Callable
            A target function or method to wrap.

        Returns
        -------
        inner_wrapped : Callable
            Wrapped callable object.
        """

        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            """
            Wrapping function for a decorator setting.

            Parameters
            ----------
            *args : list
                Target positional arguments.
            **kwargs : dict
                Target keyword arguments.

            Returns
            -------
            result : Any
                A return value(s) of a callable execution result.
            """
            with _DebugInfo(
                    callable_=func,
                    args=list(args),
                    kwargs=kwargs, module_name=module_name,
                    class_name=class_name):
                result: Any = func(*args, **kwargs)
                return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore
