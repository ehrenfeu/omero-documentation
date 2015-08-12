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
project = u'OME Model and Formats'
title = project + u' Documentation'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
if "FORMATS_RELEASE" in os.environ and len(os.environ.get('FORMATS_RELEASE')) > 0:
    release = os.environ.get('FORMATS_RELEASE')
    version = release
else:
    version = 'UNKNOWN'
    release = 'UNKNOWN'

# OME model-specific extlinks
model_extlinks = {
    # Github links
    'source' : (bf_github_root + 'blob/'+ branch + '/%s', ''),
    'sourcedir' : (bf_github_root + 'tree/'+ branch + '/%s', ''),
    'omero_source' : (omero_github_root + 'blob/'+ branch + '/%s', ''),
    # API
    'javadoc' : (downloads_root + '/latest/bio-formats5.1/api/%s', ''),
    # Doc links
    'omero_doc' : (oo_site_root + '/support/omero5.1/%s', ''),
    'bf_doc' : (oo_site_root + '/support/bio-formats5.1/%s', ''),
    # Downloads
    'bf_downloads' : (downloads_root + '/latest/bio-formats5.1/%s', ''),
    }
extlinks.update(model_extlinks)


# Edit on GitHub prefix
edit_on_github_prefix = 'formats'

# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
target = 'OME-Model-' + release + '.tex'
latex_documents = [
  (master_doc, target, title, author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '../common/images/ome-tight.pdf'
