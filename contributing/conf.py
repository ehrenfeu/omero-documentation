#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ome documentation build configuration file, created by
# sphinx-quickstart on Wed Feb 22 20:24:38 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# Append the top level directory of the docs, so we can import from the config dir.
sys.path.insert(0, os.path.abspath('../common'))
from conf import *


# -- General configuration -----------------------------------------------------

# General information about the project.
project = u'OME Contributing Developer'
title = project + u' Documentation'

# OME contributing-specific extlinks
contributing_extlinks = {
    # Github links
    'source' : (omero_github_root + 'blob/'+ branch + '/%s', ''),
    'sourcedir' : (omero_github_root + 'tree/'+ branch + '/%s', ''),
    'commit' : (omero_github_root + 'commit/%s', ''),
    'bf_source' : (bf_github_root + 'blob/'+ branch + '/%s', ''),
    'bf_sourcedir' : (bf_github_root + 'tree/'+ branch + '/%s', ''),
    'bf_commit' : (bf_github_root + 'commit/%s', ''),
    # Doc links
    'omero_doc' : (oo_site_root + '/support/omero/%s', ''),
    'bf_doc' : (oo_site_root + '/support/bio-formats/%s', ''),
    }
extlinks.update(contributing_extlinks)

extensions += ['sphinx.ext.graphviz']
graphviz_dot_args = [
    '-Nfontname=Helvetica',
    '-Nfontsize=9',
    '-Nshape=box',
    '-Gfixedsize=true']
graphviz_output_format = 'svg'

rst_epilog += """
.. _openmicroscopy.git: https://github.com/openmicroscopy/openmicroscopy
.. _bioformats.git: https://github.com/openmicroscopy/bioformats
.. _ome-documentation.git: https://github.com/openmicroscopy/ome-documentation
.. _scripts.git: https://github.com/ome/scripts
..  |merge| replace:: Merges PRs using :ref:`scc merge`
..  |buildOMERO| replace:: Builds the OMERO.server and the clients using :source:`OMERO.sh <docs/hudson/OMERO.sh>`
..  |archiveOMEROartifacts| replace:: Archives the build artifacts
..  |copyreleaseartifacts| replace:: Copies the build artifacts to a LDAP-protected folder under downloads.openmicroscopy.org
..  |promoteOMERO| replace:: copies the artifacts to necromancer
..  |buildVM| replace:: Builds a |VM| using :source:`omerovm.sh <docs/install/VM/omerovm.sh>`
..  |updatesubmodules| replace:: Updates submodules using ``scc update-submodules``
..  |buildBF| replace:: Builds Bio-Formats using ``ant clean jars tools tools-ome utils dist-bftools``
..  |testBF| replace:: Runs Bio-Formats tests using ``ant test-common test-ome-xml test-formats test-ome-io``
..  |fulltestBF| replace:: Runs Bio-Formats full test-suite using ``ant test``
..  |sphinxbuild| replace:: Runs ``make clean html latexpdf`` to build the HTML and PDF versions of the Sphinx documentation
..  |linkcheck| replace:: Runs ``make linkcheck`` and :ref:`parse the Sphinx linkcheck output <linkcheck_parser>`
..  |ssh-doc| replace:: Copies the HTML and PDF documentation over SSH to
..  |deploy-doc| replace:: Runs :ref:`scc deploy` to update
"""

# Edit on GitHub prefix
edit_on_github_prefix = 'contributing'

# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
target = 'OME-Contributing-Developer' + '.tex'
latex_documents = [
  (master_doc, target, title, author, 'manual'),
]

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '../common/images/ome-tight.pdf'

# -- Options for the linkcheck builder ----------------------------------------

# Regular expressions that match URIs that should not be checked when doing a linkcheck build
linkcheck_ignore += [r'http://localhost:\d+/?', 'http://localhost/',
    'http://www.hibernate.org',
    r'^https?://www\.openmicroscopy\.org/site/team/.*',
    r'.*[.]?example\.com/.*',
    r'^https?://www\.openmicroscopy\.org/site/support/faq.*',
    r'^https://spreadsheets.google.com/.*',
    r'^http://trac.openmicroscopy.org/ome/admin/.*']
