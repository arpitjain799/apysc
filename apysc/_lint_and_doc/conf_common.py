"""This module is for the common settings of each
Sphinx's conf.py module.
"""

import warnings
from typing import Dict
from typing import List

from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
from sphinx.application import Sphinx

PROJECT: str = 'apysc'
AUTHOR: str = 'simonritchie'
EXTENSIONS: List[str] = [
    'recommonmark',
    'sphinx_markdown_tables',
]
TEMPLATES_PATH: List[str] = ['_templates']
SOURCE_SUFFIX: Dict[str, str] = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
SOURCE_PARSERS: Dict[str, type] = {
    '.md': CommonMarkParser,
}
HTML_THEME: str = 'groundwork'
HTML_STATIC_PATH: List[str] = ['_static']
HTML_CSS_FILES: List[str] = [
    'base.css',
    'codeblock.css',
    'iframe.css',
    'add_navigation_to_footer.js',
]
HTML_LOGO: str = '../_static/logo_for_document.png'
HTML_COPY_SOURCE: bool = False


def setup(*, sphinx: Sphinx) -> None:
    """
    The Sphinx calls when it starts building.

    Parameters
    ----------
    sphinx : Sphinx
        The Sphinx instance.
    """
    warnings.filterwarnings(
        action='ignore',
        category=UserWarning,
        message=r'.*Container node skipped.*',
    )

    sphinx.add_config_value(
        name='recommonmark_config',
        default={
            'auto_toc_tree_section': 'Table of contents',
        },
        rebuild=True)
    sphinx.add_transform(AutoStructify)

    sphinx.add_js_file(filename='hide_toctree_heading_and_sidemenu.js')
