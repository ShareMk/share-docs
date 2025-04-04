# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Share docs'
copyright = '2025, ShareMk'
author = 'ShareMk'

# The short X.Y version
# version = '1.0'
# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'myst_parser',
]

# myst_parser 支持 Markdown 中一些扩展语法
myst_enable_extensions = [
    "deflist",  # 定义列表
    "dollarmath",  # 数学公式
    "amsmath",  # LaTeX 数学公式
]

# 支持的文件扩展名
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
master_doc = 'index'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['docs/_static']

# -- Options for HTMLHelp output ---------------------------------------------

htmlhelp_basename = 'MyProjectdoc'

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': '',
    'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'MyProject.tex', 'My Project Documentation',
     'Your Name', 'manual'),
]

# -- Options for manual page output ------------------------------------------

man_pages = [
    (master_doc, 'myproject', 'My Project Documentation',
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------

texinfo_documents = [
    (master_doc, 'MyProject', 'My Project Documentation',
     author, 'MyProject', 'One line description of project.',
     'Miscellaneous'),
]

# -- Options for Epub output -------------------------------------------------

epub_title = project
epub_exclude_files = ['search.html']

# 启用章节编号
numfig = True
numfig_format = {
    'figure': 'Figure %s',
    'table': 'Table %s',
    'code-block': 'Listing %s',
}

# 自动为章节编号
html_theme_options = {
    'navigation_depth': 4,  # 控制侧边栏的深度
    'collapse_navigation': False,  # 是否折叠侧边栏
    'sticky_navigation': True,  # 是否固定导航栏
    'number_sections': True,  # 启用章节编号
}

# GitHub 仓库信息
html_context = {
    "display_github": True,  # 启用 GitHub 链接
    "github_user": "ShareMk",  # GitHub 用户名
    "github_repo": "share-docs",  # 仓库名称
    "github_version": "main",  # 分支名称，例如 main 或 master
    "conf_py_path": "/",  # Sphinx 配置文件的路径（相对于仓库根目录）
}
