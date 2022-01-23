"""Utility implementations for docstrings.
"""

from ctypes import Union
from types import ModuleType
import importlib
from enum import Enum
from typing import Any, Callable, List, Match, Optional, Tuple, Type, TypeVar
import os
import re

from typing_extensions import TypedDict

_DOCSTRING_PATH_COMMENT_KEYWORD: str = 'Docstring:'
_DOCSTRING_PATH_COMMENT_PATTERN: str = (
    rf'\<\!\-\-.*?{_DOCSTRING_PATH_COMMENT_KEYWORD}'
    r'(?P<path>.*?)\-\-\>'
)

_HYPHENS_LINE_PATTERN: str = r'\s{4}-----'


class _SectionPattern(Enum):
    PARAMETERS = r'\s{4}Parameters$'
    RETURNS = r'\s{4}Returns$'
    YIELDS = r'\s{4}Yields$'
    RECEIVES = r'\s{4}Receives$'
    RAISES = r'\s{4}Raises$'
    WARNS = r'\s{4}Warns$'
    WARNINGS = r'\s{4}Warnings$'
    SEE_ALSO = r'\s{4}See Also$'
    NOTES = r'\s{4}Notes$'
    REFERENCES = r'\s{4}References$'
    EXAMPLES = r'\s{4}Examples$'
    ATTRIBUTES = r'\s{4}Attributes$'
    METHODS = r'\s{4}Methods$'


def reset_replaced_docstring_section(*, md_file_path: str) -> bool:
    """
    Reset converted a markdown's docstring section.

    Parameters
    ----------
    md_file_path : str
        Target markdown document file path.

    Returns
    -------
    is_executed : bool
        Replacing is executed or not.
    """
    from apysc._file import file_util
    md_txt: str = file_util.read_txt(file_path=md_file_path)
    matches: List[str] = _get_docstring_path_comment_matches(md_txt=md_txt)
    if not matches:
        return False
    md_txt = _remove_replaced_docstring_section_from_md_txt(
        md_txt=md_txt, matches=matches)
    with open(md_file_path, 'w') as f:
        f.write(md_txt)
    return True


def _remove_replaced_docstring_section_from_md_txt(
        *, md_txt: str, matches: List[str]) -> str:
    """
    Remove replaced docstring from a specified markdown text.

    Parameters
    ----------
    md_txt : str
        Target markdown text.
    matches : list of str
        Matched docstring path specification comments.

    Returns
    -------
    md_txt : str
        Result markdown text.
    """
    lines: List[str] = md_txt.splitlines()
    result_lines: List[str] = []
    is_reset_section_range: bool = False
    for line in lines:
        if is_reset_section_range:
            if line.startswith('#'):
                result_lines.append(f'\n{line}')
                is_reset_section_range = False
            continue
        docstring_path_specification_comment: str = \
            _extract_docstring_path_specification_comment_from_line(
                line=line, matches=matches)
        if docstring_path_specification_comment != '':
            result_lines.append(line)
            is_reset_section_range = True
            continue
        result_lines.append(line)
    md_txt = '\n'.join(result_lines)
    return md_txt


def _extract_docstring_path_specification_comment_from_line(
        *, line: str, matches: List[str]) -> str:
    """
    Extract a docstring path specification comment
    from a specified markdown line text.

    Parameters
    ----------
    line : str
        Target markdown line text.
    matches : list of str
        Matched docstring path specification comments.

    Returns
    -------
    docstring_path_specification_comment : str
        Extracted comment string.
    """
    for match in matches:
        if match in line:
            return match
    return ''


def _get_docstring_path_comment_matches(*, md_txt: str) -> List[str]:
    """
    Get matched docstring path specification comments.

    Parameters
    ----------
    md_txt : str
        Target markdown text.

    Returns
    -------
    matches : list of str
        Matched comments.
    """
    matches: List[str] = []
    for match in re.finditer(
            pattern=_DOCSTRING_PATH_COMMENT_PATTERN,
            string=md_txt,
            flags=re.MULTILINE):
        matches.append(match.group(0))
    return matches


def replace_docstring_path_specification(*, md_file_path: str) -> None:
    """
    Replace a docstring path specification in a specified
    markdown document by a converted docstring text.

    Parameters
    ----------
    md_file_path : str
        Target markdown file path.
    """
    from apysc._file import file_util
    md_txt: str = file_util.read_txt(file_path=md_file_path)
    lines: List[str] = md_txt.splitlines()
    result_lines: List[str] = []
    for line in lines:
        match: Optional[Match] = re.search(
            pattern=_DOCSTRING_PATH_COMMENT_PATTERN, string=line)
        if match is not None:
            result_lines.append(line)
            result_lines.append('')
            markdown_format_docstring: str = \
                _convert_docstring_path_comment_to_markdown_format(
                    docstring_path_comment=match.group(0)
                )
            result_lines.append(markdown_format_docstring)
            continue

        result_lines.append(line)
        continue
    pass


def _convert_docstring_path_comment_to_markdown_format(
        *, docstring_path_comment: str) -> str:
    """
    Convert a specified docstring path comment to a
    markdown format text.

    Parameters
    ----------
    docstring_path_comment : str
        Target docstring path comment.

    Returns
    -------
    markdown_format_docstring : str
        Converted text.
    """
    from apysc._file import module_util
    module_or_class_package_path: str
    callable_name: str
    module_or_class_package_path, callable_name = \
        _extract_package_path_and_callable_name_from_path(
            docstring_path_comment=docstring_path_comment,
        )
    module_or_class: Any = module_util.read_module_or_class_from_package_path(
        module_or_class_package_path=module_or_class_package_path)
    callable_: Callable = getattr(module_or_class, callable_name)
    if callable_.__doc__ is None:
        return ''
    markdown_format_docstring: str = _convert_docstring_to_markdown(
        docstring=callable_.__doc__)
    pass


def _convert_docstring_to_markdown(*, docstring: str) -> str:
    """
    Convert a specified docstring to a markdown format text.

    Parameters
    ----------
    docstring : str
        Target docstring.

    Returns
    -------
    markdown : str
        Converted markdown text.
    """
    summary: str = _extract_summary_from_docstring(docstring=docstring)
    parameters: List[_Parameter] = \
        _extract_param_or_rtn_values_from_docstring(
            target_type=_Parameter, docstring=docstring)
    returns: List[_Return] = _extract_param_or_rtn_values_from_docstring(
        target_type=_Return, docstring=docstring)
    raises: List[_Raise] = _extract_raise_values_from_docstring(
        docstring=docstring)
    notes: str = _extract_notes_from_docstring(docstring=docstring)
    references: List[_Reference] = _extract_reference_values_from_docstring(
        docstring=docstring)
    pass


def _extract_notes_from_docstring(*, docstring: str) -> str:
    """
    Extract a notes value from a docstring.

    Parameters
    ----------
    docstring : str
        Target docstring.

    Returns
    -------
    notes : str
        Extract notes text value.
    """
    lines: List[str] = docstring.splitlines()
    lines = _remove_blank_lines_from_list(lines=lines)
    is_notes_section_range: bool = False
    base_indent_num: int = 0
    notes_lines: List[str] = []
    for line in lines:
        base_indent_num = _get_base_indent_num_if_not_set(
            line=line, base_indent_num=base_indent_num)
        if _is_target_section_pattern_line(
                line=line,
                section_pattern=_SectionPattern.NOTES):
            is_notes_section_range = True
            continue
        if _is_skip_target_line(
                is_target_section_range=is_notes_section_range,
                line=line):
            continue
        if _is_section_line(line=line):
            break
        notes_lines.append(line)
    notes: str = '\n'.join(notes_lines)
    notes = _remove_line_breaks_and_unnecessary_spaces(text=notes)
    return notes


class _ParamOrRtnBase:
    _name: str
    _type_str: str
    _description: str

    def __init__(
            self, *, name: str, type_str: str, description: str) -> None:
        """
        Parameter or return value's base class.

        Parameters
        ----------
        name : str
            Parameter or return value name.
        type_str : str
            Parameter or return value type name.
        description : str
            Parameter or return value description.
        """
        self._name = name
        self._type_str = type_str
        self._description = description

    def __eq__(self, other: Any) -> bool:
        """
        The method for equality comparison.

        Parameters
        ----------
        other : Any
            Other instance to compare with.

        Returns
        -------
        result : bool
            If each attribute is equal to the other, this
            method returns True.
        """
        if not isinstance(other, _ParamOrRtnBase):
            return False
        if self.name != other.name:
            return False
        if self.type_str != other.type_str:
            return False
        if self.description != other.description:
            return False
        return True

    @property
    def name(self) -> str:
        """
        Get a parameter or return value name.

        Returns
        -------
        name : str
            A parameter or return value name.
        """
        return self._name

    @property
    def type_str(self) -> str:
        """
        Get a parameter or return value type name.

        Returns
        -------
        type_str : str
            A parameter or return value type name.
        """
        return self._type_str

    @property
    def description(self) -> str:
        """
        Get a parameter or return value description.

        Returns
        -------
            A parameter or return value description.
        """
        return self._description


class _Parameter(_ParamOrRtnBase):
    """Parameter value type.
    """


class _Return(_ParamOrRtnBase):
    """Return value type.
    """


class _Raise:
    """Raise value type.
    """
    _err_class_name: str
    _description: str

    def __init__(self, *, err_class_name: str, description: str) -> None:
        """
        Raise value type.

        Parameters
        ----------
        err_class_name : str
            Target error class name.
        description : str
            Error condition description.
        """
        self._err_class_name = err_class_name
        self._description = description

    @property
    def err_class_name(self) -> str:
        """
        Get a target error class name.

        Returns
        -------
        err_class_name : str
            A target error class name.
        """
        return self._err_class_name

    @property
    def description(self) -> str:
        """
        Get a error condition description.

        Returns
        -------
        description : str
            A error condition description.
        """
        return self._description

    def __eq__(self, other: Any) -> bool:
        """
        The method for equality comparison.

        Parameters
        ----------
        other : Any
            Other value to compare with.

        Returns
        -------
        result : bool
            If each attribute is equal to the other, this
            method returns True.
        """
        if not isinstance(other, _Raise):
            return False
        if self.err_class_name != other.err_class_name:
            return False
        if self._description != other._description:
            return False
        return True


class _Reference:
    """Reference value type.
    """

    _page_label: str
    _url: str

    def __init__(self, *, page_label: str, url: str) -> None:
        """
        Reference value type.

        Parameters
        ----------
        page_label : str
            Target reference page label.
        url : str
            Target reference page URL.
        """
        self._page_label = page_label
        self._url = url

    @property
    def page_label(self) -> str:
        """
        Get a target reference page label.

        Returns
        -------
        page_label : str
            A target reference page label.
        """
        return self._page_label

    @property
    def url(self) -> str:
        """
        Get a target reference page URL.

        Returns
        -------
        url : str
            A target reference page.
        """
        return self._url

    def __eq__(self, other: Any) -> bool:
        """
        The method for equality comparison.

        Parameters
        ----------
        other : Any
            Other value to compare with.

        Returns
        -------
        result : bool
            If each attribute is equal to the other, this
            method returns True.
        """
        if not isinstance(other, _Reference):
            return False
        if self.page_label != other.page_label:
            return False
        if self.url != other.url:
            return False
        return True


def _extract_reference_values_from_docstring(
        *, docstring: str) -> List[_Reference]:
    """
    Extract reference values from a docstring.

    Parameters
    ----------
    docstring : str
        Target docstring.

    Returns
    -------
    reference_values : list of _Reference
        Extracted reference values.
    """
    lines: List[str] = docstring.splitlines()
    lines = _remove_blank_lines_from_list(lines=lines)
    is_references_section_range: bool = False
    page_label: str = ''
    url: str = ''
    base_indent_num: int = 0
    reference_values: List[_Reference] = []
    for line in lines:
        current_indent_num: int = _get_indent_num_from_line(line=line)
        base_indent_num = _get_base_indent_num_if_not_set(
            line=line, base_indent_num=base_indent_num)
        if _is_target_section_pattern_line(
                line=line,
                section_pattern=_SectionPattern.REFERENCES):
            is_references_section_range = True
            continue
        if _is_skip_target_line(
                is_target_section_range=is_references_section_range,
                line=line):
            continue
        if _is_section_line(line=line):
            break
        if current_indent_num == base_indent_num:
            page_label = _remove_unnecessary_markdown_list_from_line(
                line=line)
            continue
        url = _remove_unnecessary_markdown_list_from_line(line=line)
        _make_reference_and_append_to_list(
            reference_values=reference_values,
            page_label=page_label, url=url)
        url = ''
    _make_reference_and_append_to_list(
        reference_values=reference_values,
        page_label=page_label, url=url)
    return reference_values


def _make_reference_and_append_to_list(
        *,
        reference_values: List[_Reference],
        page_label: str,
        url: str) -> None:
    """
    Make a reference value and append it to a specified list.

    Parameters
    ----------
    reference_values : list of _Reference
        A list to append a reference value.
    page_label : str
        Target reference page label.
    url : str
        Target reference page URL.
    """
    if url == '':
        return
    reference: _Reference = _Reference(
        page_label=page_label, url=url)
    reference_values.append(reference)


def _remove_unnecessary_markdown_list_from_line(
        *, line: str) -> str:
    """
    Remove unnecessary markdown list string from a line.

    Parameters
    ----------
    line : str
        Target docstring line.

    Returns
    -------
    line : str
        Result docstring line.
    """
    line = line.replace('- ', '', 1)
    line = line.strip()
    return line


def _extract_raise_values_from_docstring(*, docstring: str) -> List[_Raise]:
    """
    Extract raise values from a docstring.

    Parameters
    ----------
    docstring : str
        Target docstring.

    Returns
    -------
    raise_values : list of _Raise
        Extracted raise values.
    """
    lines: List[str] = docstring.splitlines()
    lines = _remove_blank_lines_from_list(lines=lines)
    is_raises_section_range: bool = False
    err_class_name: str = ''
    base_indent_num: int = 0
    description_lines: List[str] = []
    raise_values: List[_Raise] = []
    for line in lines:
        current_indent_num: int = _get_indent_num_from_line(line=line)
        base_indent_num = _get_base_indent_num_if_not_set(
            line=line, base_indent_num=base_indent_num)
        if _is_target_section_pattern_line(
                line=line,
                section_pattern=_SectionPattern.RAISES):
            is_raises_section_range = True
            continue
        if _is_skip_target_line(
                is_target_section_range=is_raises_section_range,
                line=line):
            continue
        if _is_section_line(line=line):
            _make_raise_description_and_append_to_list(
                raise_values=raise_values,
                err_class_name=err_class_name,
                description_lines=description_lines,
            )
            break
        if current_indent_num == base_indent_num:
            _make_raise_description_and_append_to_list(
                raise_values=raise_values,
                err_class_name=err_class_name,
                description_lines=description_lines,
            )
            err_class_name = line.strip()
            continue
        description_lines.append(line)
    return raise_values


def _remove_blank_lines_from_list(*, lines: List[str]) -> List[str]:
    """
    Remove blank lines from a list of lines.

    Parameters
    ----------
    lines : list of str
        Target list of lines.

    Returns
    -------
    result_lines : list of str
        A lines list which removed blank lines.
    """
    result_lines: List[str] = []
    for line in lines:
        if line.strip() == '':
            continue
        result_lines.append(line)
    return result_lines


def _get_base_indent_num_if_not_set(
        *, line: str, base_indent_num: int) -> int:
    """
    Get a base indent number from line if it is not set.

    Parameters
    ----------
    line : str
        Target docstring line.
    base_indent_num : int
        Current base indent number.

    Returns
    -------
    base_indent_num : int
        If the base_indent_num argument is zero, this function
        returns the current line indent number. Otherwise, it
        returns the same value of the base_indent_num argument.
    """
    if base_indent_num != 0:
        return base_indent_num
    current_indent_num: int = _get_indent_num_from_line(line=line)
    return current_indent_num


def _make_raise_description_and_append_to_list(
        *,
        raise_values: List[_Raise],
        err_class_name: str,
        description_lines: List[str]) -> None:
    """
    Make a raise value description from a list of lines and
    append raise value to a specified list.

    Notes
    -----
    This function clears a list of description lines.

    Parameters
    ----------
    raise_values : list of _Raise
        A list to append a raise value.
    err_class_name : str
        Target error class name.
    description_lines : list of str
        A list of description lines.
    """
    if not description_lines:
        return
    description: str = '\n'.join(description_lines)
    description = _remove_line_breaks_and_unnecessary_spaces(
        text=description)
    raise_: _Raise = _Raise(
        err_class_name=err_class_name, description=description)
    raise_values.append(raise_)
    description_lines.clear()


_ParamOrRtn = TypeVar('_ParamOrRtn', _Parameter, _Return)


def _extract_param_or_rtn_values_from_docstring(
        *, target_type: Type[_ParamOrRtn],
        docstring: str) -> List[_ParamOrRtn]:
    """
    Extract parameter or return values from a docstring.

    Parameters
    ----------
    docstring : str
        Target docstring.

    Returns
    -------
    param_or_rtn_values : list of _Parameter or _Return
        Extracted parameter or return values.
    """
    lines: List[str] = docstring.splitlines()
    lines = _remove_blank_lines_from_list(lines=lines)
    is_param_or_rtn_section_range: bool = False
    value_name: str = ''
    value_type_str: str = ''
    base_indent_num: int = 0
    description_lines: List[str] = []
    param_or_rtn_values: List[_ParamOrRtn] = []
    params_or_rtns_section_pattern: _SectionPattern = \
        _get_params_or_rtns_section_pattern_by_type(target_type=target_type)
    for line in lines:
        current_indent_num: int = _get_indent_num_from_line(line=line)
        base_indent_num = _get_base_indent_num_if_not_set(
            line=line, base_indent_num=base_indent_num)
        if _is_target_section_pattern_line(
                line=line,
                section_pattern=params_or_rtns_section_pattern):
            is_param_or_rtn_section_range = True
            continue
        if _is_skip_target_line(
                is_target_section_range=is_param_or_rtn_section_range,
                line=line):
            continue
        if _is_section_line(line=line):
            _make_prm_or_rtn_description_and_append_to_list(
                target_type=target_type,
                param_or_rtn_values=param_or_rtn_values,
                value_name=value_name,
                value_type_str=value_type_str,
                description_lines=description_lines,
            )
            break
        if current_indent_num == base_indent_num:
            _make_prm_or_rtn_description_and_append_to_list(
                target_type=target_type,
                param_or_rtn_values=param_or_rtn_values,
                value_name=value_name,
                value_type_str=value_type_str,
                description_lines=description_lines,
            )
            value_name, value_type_str = _get_value_name_and_type_from_line(
                line=line)
            continue
        description_lines.append(line)
    return param_or_rtn_values


def _is_skip_target_line(
        *, is_target_section_range: bool, line: str) -> bool:
    """
    Get a boolean indicating whether a specified line
    is skipping target or not.

    Parameters
    ----------
    is_target_section_range : bool
        A boolean indicating whether a specified line
        is in a range of target section.
    line : str
        Target docstring line.

    Returns
    -------
    result : bool
        A boolean indicating whether a specified line
        is skipping target or not.
    """
    if not is_target_section_range:
        return True
    if _is_hyphens_line(line=line):
        return True
    return False


def _get_params_or_rtns_section_pattern_by_type(
        *,
        target_type: Type[_ParamOrRtnBase]) -> _SectionPattern:
    """
    Get the parameters or returns section pattern
    of a specified type.

    Parameters
    ----------
    target_type : _Parameter or _Return
        Target type.

    Returns
    -------
    pattern : _SectionPattern
        Target section pattern.

    Raises
    ------
    ValueError
        If an invalid target type is provided.
    """
    if target_type == _Parameter:
        return _SectionPattern.PARAMETERS
    if target_type == _Return:
        return _SectionPattern.RETURNS
    raise ValueError(
        f'Invalid type argument is provided: {target_type}')


def _make_prm_or_rtn_description_and_append_to_list(
        *,
        target_type: Type[_ParamOrRtn],
        param_or_rtn_values: List[_ParamOrRtn],
        value_name: str,
        value_type_str: str,
        description_lines: List[str]) -> None:
    """
    Make a parameter or return value description from a list of
    lines and append parameter or return value to a specified list.

    Notes
    -----
    This function clears a list of description lines.

    Parameters
    ----------
    param_or_rtn_values : lisf of _ParamOrRtnBase
        A list to append a parameter or return value.
    value_name : str
        Parameter or return value name.
    value_type_str : str
        Parameter or return type name.
    description_lines : list of str
        A list of description lines.
    """
    if not description_lines:
        return
    description: str = '\n'.join(description_lines)
    description = _remove_line_breaks_and_unnecessary_spaces(
        text=description)
    param_or_rtn: _ParamOrRtn = target_type(
        name=value_name, type_str=value_type_str,
        description=description)
    param_or_rtn_values.append(param_or_rtn)
    description_lines.clear()


def _get_indent_num_from_line(*, line: str) -> int:
    """
    Get an indent number from a specified docstring line.

    Parameters
    ----------
    line : str
        Target docstring line.

    Returns
    -------
    indent_num : int
        Indent number of a specified docstring line.
    """
    spaces: int = 0
    for char in line:
        if char != ' ':
            break
        spaces += 1
    indent_num: int = spaces // 4
    return indent_num


def _get_value_name_and_type_from_line(*, line: str) -> Tuple[str, str]:
    """
    Get a parameter or return value and type from
    a specified line.

    Parameters
    ----------
    line : str
        Target docstring line.

    Returns
    -------
    value_name : str
        Target parameter or return value name.
    type_name : str
        Target parameter or return value type name.
    """
    if ':' not in line:
        return '', ''
    splitted: List[str] = line.split(':', maxsplit=1)
    value_name: str = splitted[0].strip()
    type_name: str = splitted[1].strip()
    return value_name, type_name


def _is_hyphens_line(*, line: str) -> bool:
    """
    Get a boolean indicating whether a specified line is
    a hyphens line or not.

    Parameters
    ----------
    line : str
        Target docstring line.

    Returns
    -------
    result : bool
        If a specified line is a hyphens line, this function
        returns True.
    """
    match: Optional[Match] = re.search(
        pattern=_HYPHENS_LINE_PATTERN, string=line)
    if match is None:
        return False
    return True


def _is_target_section_pattern_line(
        *,
        line: str,
        section_pattern: _SectionPattern) -> bool:
    """
    Get a boolean indicating whether a specified line
    is matching with a target section pattern or not.

    Parameters
    ----------
    line : str
        Target docstring line.
    section_pattern : _SectionPattern
        Target section pattern.

    Returns
    -------
    result : bool
        If a specified line is the parameters section,
        this function returns True.
    """
    match: Optional[Match] = re.search(
        pattern=section_pattern.value, string=line)
    if match is None:
        return False
    return True


def _extract_summary_from_docstring(*, docstring: str) -> str:
    """
    Extract a summary text from a docstring.

    Parameters
    ----------
    docstring : str
        Target docstring.

    Returns
    -------
    summary : str
        Extracted summary text.

    Notes
    -----
    This function converts line break to a space.
    """
    lines: List[str] = docstring.splitlines()
    result_lines: List[str] = []
    for line in lines:
        if _is_section_line(line=line):
            break
        result_lines.append(line)
    summary: str = '\n'.join(result_lines)
    summary = _remove_line_breaks_and_unnecessary_spaces(text=summary)
    return summary


def _remove_line_breaks_and_unnecessary_spaces(*, text: str) -> str:
    """
    Remove line breaks to a single space and unnecessary
    spaces (e.g., double spaces and leading and trailing spaces).

    Parameters
    ----------
    text : str
        Target text.

    Returns
    -------
    text : str
        Converted text.
    """
    from apysc._string import string_util
    text = text.strip()
    text = text.replace('\n', ' ')
    text = string_util.replace_double_spaces_to_single_space(
        string=text)
    text = text.strip()
    return text


def _is_section_line(*, line: str) -> bool:
    """
    Get a boolean indicating whether a specified docstring line
    is a section line or not.

    Parameters
    ----------
    line : str
        Target docstring line text.

    Returns
    -------
    result : bool
        If a specified docstring line is section line, this
        function returns True.
    """
    for pattern in _SectionPattern:
        match: Optional[Match] = re.search(
            pattern=pattern.value, string=line)
        if match is None:
            continue
        return True
    return False


def _extract_package_path_and_callable_name_from_path(
        *, docstring_path_comment) -> Tuple[str, str]:
    """
    Extract a module or class package path and callable
    name from a specified path comment.

    Parameters
    ----------
    docstring_path_comment : str
        Target docstring path comment.

    Returns
    -------
    module_or_class_package_path : str
        Extracted module or class package path.
        e.g., 'apy.path' or 'any.path.AnyClass'.
    callable_name : str
        Extracted callable name.
    """
    path: str = _extract_path_from_docstring_comment(
        docstring_path_comment=docstring_path_comment)
    if '.' not in path:
        return '', ''
    splitted: List[str] = path.rsplit('.', maxsplit=1)
    module_or_class_package_path: str = splitted[0]
    callable_name: str = splitted[1]
    return module_or_class_package_path, callable_name


def _extract_path_from_docstring_comment(
        *, docstring_path_comment: str) -> str:
    """
    Extract a path string from a specified docstring path comment.

    Parameters
    ----------
    docstring_path_comment : str
        Target docstring path comment.

    Returns
    -------
    path : str
        Extracted path string.
    """
    match: Optional[Match] = re.search(
        pattern=_DOCSTRING_PATH_COMMENT_PATTERN,
        string=docstring_path_comment)
    if match is None:
        return ''
    path: str = match.group(1)
    path = path.strip()
    return path
