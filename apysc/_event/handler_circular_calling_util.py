"""Handler circular calling related utilities.
"""

from typing import List, Tuple


def is_handler_circular_calling(handler_name: str) -> bool:
    """
    Get a boolean value whether a specified handler is
    a circular call or not.

    Parameters
    ----------
    handler_name : str
        Targer handler name.

    Returns
    -------
    result : bool
        If a specified handler is a circular call, True will be returned.
    """
    from apysc._expression import event_handler_scope
    handler_name = event_handler_scope.remove_suffix_num_from_handler_name(
        handler_name=handler_name)
    handler_names: List[str] = _read_handler_names()
    handler_names = _append_handler_name_to_last_of_list(
        handler_name=handler_name, handler_names=handler_names)
    count: int = handler_names.count(handler_name)
    if count < 2:
        return False
    prev_handler_name: str = handler_names[-2]
    prev_handler_count: int = 0
    for i, handler_name_ in enumerate(handler_names):
        if i == 0:
            continue
        if handler_name_ != handler_name:
            continue
        prev_handler_name_: str = handler_names[i - 1]
        if prev_handler_name_ != prev_handler_name:
            continue
        prev_handler_count += 1
        if prev_handler_count == 2:
            break
    if prev_handler_count == 2:
        return True
    return False


def _append_handler_name_to_last_of_list(
        handler_name: str, handler_names: List[str]) -> List[str]:
    """
    Append a specified handler's name to the last of the list
    if the last one is an other handler's name.

    This function is used to unify last value regardless of
    `HandlerScope` setting.

    Parameters
    ----------
    handler_name : str
        Targer handler name.
    handler_names : list of str
        List to be appended.

    Returns
    -------
    handler_names : list of str
        Result list value.
    """
    if not handler_names:
        return [handler_name]
    if handler_names[-1] == handler_name:
        return handler_names
    handler_names.append(handler_name)
    return handler_names


def _read_handler_names() -> List[str]:
    """
    Read the current handler names from the calling stack.

    Returns
    -------
    handler_names : list of str
        Target handler names.
    """
    from apysc._expression import expression_data_util
    expression_data_util.initialize_sqlite_tables_if_not_initialized()
    table_name: str = expression_data_util.TableName.\
        HANDLER_CALLING_STACK.value
    query: str = (
        f'SELECT handler_name FROM {table_name} '
        f'ORDER BY scope_count'
    )
    expression_data_util.cursor.execute(query)
    result: List[Tuple[str]] = expression_data_util.cursor.fetchall()
    handler_names: List[str] = [tpl[0] for tpl in result]
    return handler_names
