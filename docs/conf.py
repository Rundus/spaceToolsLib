# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# get the scope of this file to your project
# import os
# import sys
# sys.path.insert(0,os.path.abspath(r"C:\Users\cfelt\PycharmProjects\spaceToolsLib"))
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

# import the modules
import spaceToolsLib.tools.CDF_output
import spaceToolsLib.tools.coordinates

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'spaceToolsLib'
copyright = '2025, Connor Feltman'
author = 'Connor Feltman'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.duration',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_static_path = ['_static']

# html_theme = 'alabaster'
html_theme = 'classic'
# html_theme = 'sphinxdoc'
html_last_updated_fmt = '%b %d, %Y'
html_logo = 'photos//spaceToolsLib_logo.png'
html_favicon = 'photos//spaceToolsLib_favicon.png'


html_theme_options = {

}

