from datetime import datetime
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'The Dataverse Project'
copyright = u'%d, The President & Fellows of Harvard College' % datetime.now().year
author = 'The Dataverse Project'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_logo = '_static/_images/dataverse_r_project.png'
html_static_path = ['_static']
# "The header navigation bar is at the top of each page and contains top-level navigation across pages in your documentation, as well as extra links and components that you can add." -- https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/header-links.html
html_theme_options = {
  "show_prev_next": False,
  "header_links_before_dropdown": 5,
  # see https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/source-buttons.html
  "use_edit_page_button": True,
  "external_links": [
      {"name": "Working Groups", "url": "https://www.gdcc.io/working-groups.html"}
  ]
}
html_context = {
    "github_user": "IQSS",
    "github_repo": "sphinx.dataverse.org",
    "github_version": "main",
    "doc_path": "source",
}
# see use_edit_page_button, which we use instead
html_show_sourcelink = False
