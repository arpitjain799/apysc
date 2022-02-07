"""The script to convert and sync each docstring to
markdown files.
"""

from typing import Dict
import os
from types import ModuleType
from typing import Callable, List, Optional, Tuple, Type
import inspect


def convert_recursively(*, dir_path: str) -> None:
    """
    Convert each docstring in the specified directory
    to markdown files recursively.

    Parameters
    ----------
    dir_path : str
        Target directory path.
    """
    from apysc._file import module_util
    if not os.path.isdir(dir_path):
        return
    file_or_dir_names: List[str] = os.listdir(dir_path)
    for file_or_dir_name in file_or_dir_names:
        file_or_dir_path: str = os.path.join(
            dir_path, file_or_dir_name)
        if os.path.isfile(file_or_dir_path):
            convert_recursively(dir_path=file_or_dir_path)
            continue
        if not file_or_dir_path.endswith('.py'):
            continue
        module: ModuleType = module_util.read_target_path_module(
            module_path=file_or_dir_path)
        markdown: str = _convert_module_docstring_to_markdown(
            module=module)
        pass
    pass


def _convert_module_docstring_to_markdown(
        *, module: ModuleType) -> str:
    """
    Convert a specified module's docstring to a markdown string.

    Parameters
    ----------
    module : ModuleType
        Target module.

    Returns
    -------
    markdown : str
        Converted markdown string.
    """
    markdown: str = f'# {module.__name__} docstrings'
    markdown = _append_module_docstring_to_markdown(
        markdown=markdown,
        docstring=module.__doc__)

    toplevel_functions: List[Callable] = _get_module_toplevel_functions(
        module=module)
    for toplevel_function in toplevel_functions:
        markdown = _append_toplevel_function_docstring_to_markdown(
            markdown=markdown, toplevel_function=toplevel_function)

    toplevel_classes: List[Type] = _get_toplevel_classes(
        module=module)
    for toplevel_class in toplevel_classes:
        markdown = _append_toplevel_class_docstring_to_markdown(
            markdown=markdown, toplevel_class=toplevel_class)

    return markdown


def _append_toplevel_class_docstring_to_markdown(
        *, markdown: str, toplevel_class: Type) -> str:
    """
    Append a top-level class docstring to a specified
    markdown string.

    Parameters
    ----------
    markdown : str
        Target markdown string.
    toplevel_class : Type
        Target top-level class.

    Returns
    -------
    markdown : str
        Result markdown string.
    """
    from apysc._lint_and_doc import docstring_util
    if markdown != '':
        markdown += '\n\n'
    markdown += f'## {toplevel_class.__name__} class docstring\n\n'
    if toplevel_class.__doc__ is not None:
        markdown += docstring_util.extract_summary_from_docstring(
            docstring=toplevel_class.__doc__)
        markdown = _append_each_section_to_markdown(
            markdown=markdown, docstring=toplevel_class.__doc__)

    methods: List[Callable] = _get_methods_from_class(
        class_=toplevel_class)
    for method in methods:
        if method.__doc__ is None:
            continue
        markdown += f'\n\n### {method.__name__} method docstring'
        markdown = _append_each_section_to_markdown(
            markdown=markdown, docstring=method.__doc__)

    return markdown


_EXCLUDING_TARGET_BUILTIN_METHODS: Dict[str, str] = {
    'type':
    "type(object_or_name, bases, dict)"
    "\ntype(object) -> the object's type"
    "\ntype(name, bases, dict) -> a new type",

    '__delattr__': 'Implement delattr(self, name).',

    '__dir__':
    '__dir__() -> list'
    '\ndefault dir() implementation',

    '__eq__': 'Return self==value.',

    '__format__': 'default object formatter',

    '__ge__': 'Return self>=value.',

    '__getattribute__': 'Return getattr(self, name).',

    '__gt__': 'Return self>value.',

    '__hash__': 'Return hash(self).',

    '__init_subclass__':
    'This method is called when a class is subclassed.'
    '\n\nThe default implementation does nothing. It may be'
    '\noverridden to extend subclasses.\n',

    '__le__': 'Return self<=value.',

    '__lt__': 'Return self<value.',

    '__ne__': 'Return self!=value.',

    '__new__':
    'Create and return a new object.  '
    'See help(type) for accurate signature.',

    '__reduce__': 'helper for pickle',

    '__reduce_ex__': 'helper for pickle',

    '__repr__': 'Return repr(self).',

    '__setattr__': 'Implement setattr(self, name, value).',

    '__sizeof__':
    '__sizeof__() -> int'
    '\nsize of object in memory, in bytes',

    '__str__': 'Return str(self).',

    '__subclasshook__':
    'Abstract classes can override this to customize issubclass().'
    '\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().'
    '\nIt should return True, False or NotImplemented.  If it returns'
    '\nNotImplemented, the normal algorithm is used.  Otherwise, it'
    '\noverrides the normal algorithm (and the outcome is cached).\n',
}


def _get_methods_from_class(*, class_: Type) -> List[Callable]:
    """
    Get methods from a specified class.

    Parameters
    ----------
    class_ : Type
        Target class.

    Returns
    -------
    methods : list of Callable
        Extracted methods.
    """
    members: List[Tuple[str, Callable]] = inspect.getmembers(
        class_, predicate=callable)
    methods: List[Callable] = []
    for _, method in members:
        if method.__doc__ is None:
            continue
        builtin_docstring: str = _EXCLUDING_TARGET_BUILTIN_METHODS.get(
            method.__name__, '')
        if method.__doc__ == builtin_docstring:
            continue
        methods.append(method)
    return methods


def _get_toplevel_classes(*, module: ModuleType) -> List[Type]:
    """
    Get top-level classes from a specified module.

    Parameters
    ----------
    module : ModuleType
        Target module.

    Returns
    -------
    toplevel_classes : list of Type
        Top-level classes.
    """
    members: List[Tuple[str, Type]] = inspect.getmembers(
        module, predicate=inspect.isclass)
    toplevel_classes: List[Type] = [class_ for _, class_ in members]
    return toplevel_classes


def _append_toplevel_function_docstring_to_markdown(
        *, markdown: str,
        toplevel_function: Callable) -> str:
    """
    Append a top-level function docstring to a specified
    markdown string.

    Parameters
    ----------
    markdown : str
        Target markdown string.
    toplevel_function : Callable
        Target top-level functions.

    Returns
    -------
    markdown : str
        Result markdown string.
    """
    if toplevel_function.__doc__ is None:
        return markdown
    if markdown != '':
        markdown += '\n\n'
    markdown += f'## {toplevel_function.__name__} function docstring'
    markdown = _append_each_section_to_markdown(
        markdown=markdown,
        docstring=toplevel_function.__doc__,
    )
    return markdown


def _append_each_section_to_markdown(
        markdown: str, docstring: str) -> str:
    """
    Append each docstring section to a specified markdown string.

    Parameters
    ----------
    markdown : str
        Target markdown string.
    docstring : str
        Target docstring.

    Returns
    -------
    markdown : str
        Result markdown string.
    """
    from apysc._lint_and_doc import docstring_util
    from apysc._lint_and_doc.docstring_util import Parameter, Return, Raise, Example, Reference
    summary: str = docstring_util.extract_summary_from_docstring(
        docstring=docstring)
    parameters: List[Parameter] = \
        docstring_util.extract_param_or_rtn_values_from_docstring(
            target_type=Parameter, docstring=docstring)
    returns: List[Return] = \
        docstring_util.extract_param_or_rtn_values_from_docstring(
            target_type=Return, docstring=docstring)
    raises: List[Raise] = docstring_util.extract_raise_values_from_docstring(
        docstring=docstring)
    notes: str = docstring_util.extract_notes_from_docstring(
        docstring=docstring)
    examples: List[Example] = \
        docstring_util.extract_example_values_from_docstring(
            docstring=docstring)
    references: List[Reference] = \
        docstring_util.extract_reference_values_from_docstring(
            docstring=docstring)

    markdown = docstring_util.append_summary_to_markdown(
        markdown=markdown, summary=summary,
        heading_label='')
    markdown = docstring_util.append_params_or_rtns_to_markdown(
        markdown=markdown, params_or_rtns=parameters)
    markdown = docstring_util.append_params_or_rtns_to_markdown(
        markdown=markdown, params_or_rtns=returns)
    markdown = docstring_util.append_raises_to_markdown(
        markdown=markdown, raises=raises)
    markdown = docstring_util.append_notes_to_markdown(
        markdown=markdown, notes=notes)
    markdown = docstring_util.append_examples_to_markdown(
        markdown=markdown, examples=examples)
    markdown = docstring_util.append_references_to_markdown(
        markdown=markdown, references=references)
    markdown = docstring_util.remove_trailing_hr_tag(markdown=markdown)
    return markdown


def _get_module_toplevel_functions(*, module: ModuleType) -> List[Callable]:
    """
    Get top-level functions from a specified module.

    Parameters
    ----------
    module : ModuleType
        Target module.

    Returns
    -------
    toplevel_functions : list of Callable
        Top-level functions.
    """
    members: List[Tuple[str, Callable]] = inspect.getmembers(
        module, predicate=inspect.isfunction)
    toplevel_functions: List[Callable] = [
        function for _, function in members]
    return toplevel_functions


def _append_module_docstring_to_markdown(
        *, markdown: str,
        docstring: Optional[str]) -> str:
    """
    Append a module description docstring to a
    specified markdown string.

    Parameters
    ----------
    markdown : str
        Target markdown string.
    docstring : str or None
        Target module description docstring.
    summary_heading : str
        Summary heading string.

    Returns
    -------
    markdown : str
        Result markdown string.
    """
    from apysc._lint_and_doc import docstring_util
    from apysc._lint_and_doc.docstring_util import Reference
    if docstring is None:
        return markdown
    summary: str = docstring_util.extract_summary_from_docstring(
        docstring=docstring)
    notes: str = docstring_util.extract_notes_from_docstring(
        docstring=docstring)
    references: List[Reference] = docstring_util.\
        extract_reference_values_from_docstring(docstring=docstring)

    if markdown != '':
        markdown += '\n\n'
    markdown += '## Module summary'
    markdown = docstring_util.append_summary_to_markdown(
        markdown=markdown, summary=summary,
        heading_label='')
    markdown = docstring_util.append_notes_to_markdown(
        markdown=markdown, notes=notes)
    markdown = docstring_util.append_references_to_markdown(
        markdown=markdown, references=references)
    markdown = docstring_util.remove_trailing_hr_tag(markdown=markdown)
    return markdown
