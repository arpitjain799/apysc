"""This module is for the data model of the fixed-translation
mapping settings.
"""

from typing import List, Optional

from apysc._lint_and_doc.add_doc_translation_mapping_blank_data import Lang


class Mapping:
    """The class of a single fixed-translation mapping settings.
    """

    _key: str
    _value: str

    def __init__(self, *, key: str, value: str) -> None:
        """
        A single fixed-translation mapping settings.

        Parameters
        ----------
        key : str
            A key value (this value needs to set a source
            english string).
        value : str
            A translated value.
        """
        self._key = key
        self._value = value

    @property
    def key(self) -> str:
        """
        Get a key value (a source english string).

        Returns
        -------
        key : str
            A key value (a source english string).
        """
        return self._key

    @property
    def value(self) -> str:
        """
        Get a translated value.

        Returns
        -------
        value : str
            A translated value.
        """
        return self._value


class Mappings:
    """The class for fixed-translation mappings settings.
    """

    mapping: List[Mapping]

    def __init__(self, mappings: List[Mapping]) -> None:
        """
        The class for fixed-translation mappings settings.

        Parameters
        ----------
        mappings : list of Mapping
            A target mappings list.
        """
        self.mapping = mappings


def get_fixed_translation_str_if_exists(
        *, key: str, lang: Lang) -> str:
    """
    Get a fixed-translation string from a specified language key
    string if there is a mapping setting.

    Parameters
    ----------
    key : str
        A target key string (source english string).
    lang : Lang
        A target language.

    Returns
    -------
    translation_str : str
        A translated string. If there is no fixed-translation
        mapping setting, this interface returns a blank string.
    """
    mappings: Optional[Mappings] = _read_mappings(lang=lang)
    pass


def _read_mappings(*, lang) -> Optional[Mappings]:
    """
    Read a fixed-translation mappings settings if it exists.

    Parameters
    ----------
    lang : Lang
        A target language.

    Returns
    -------
    mappings : Mappings
        A read mappings settings. If there is no mappings
        settings, this interface returns None.
    """
    module_path: str = _get_mappings_module_path_from_lang(lang=lang)
    pass


def _get_mappings_module_path_from_lang(*, lang: Lang) -> str:
    """
    Get a fixed-translation mappings settings module path
    of a specified language.

    Parameters
    ----------
    lang : Lang
        A target language.

    Returns
    -------
    module_path : str
        A fixed-translation mappings settings module path
        of a specified language.
    """
    module_path: str = (
        './apysc/_lint_and_doc/fixed_translation_mapping/'
        f'{lang.value}.py'
    )
    return module_path
