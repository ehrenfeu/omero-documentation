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
sys.path.insert(1, os.path.abspath('../omero'))
import conf_autogen


# -- General configuration -----------------------------------------------------

# General information about the project.
project = u'OMERO'
title = project + u' Documentation'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
if "OMERO_RELEASE" in os.environ and len(os.environ.get('OMERO_RELEASE')) > 0:
    release = os.environ.get('OMERO_RELEASE')
    [majornumber, minornumber, patchnumber] = split_release(release)

    # Define Sphinx version and release variables and development branch
    version = ".".join(str(x) for x in (majornumber, minornumber))

    if patchnumber > 0:
        tags.add('point_release')
    previousversion = get_previous_version(majornumber, minornumber)
else:
    version = 'UNKNOWN'
    previousversion = 'UNKNOWN'
    release = 'UNKNOWN'

rst_prolog = """
"""

rst_epilog += """
.. |OmeroPy| replace:: :doc:`/developers/Python`
.. |OmeroCpp| replace:: :doc:`/developers/Cpp`
.. |OmeroJava| replace:: :doc:`/developers/Java`
.. |OmeroMatlab| replace:: :doc:`/developers/Matlab`
.. |OmeroApi| replace:: :doc:`/developers/Modules/Api`
.. |OmeroWeb| replace:: :doc:`/developers/Web`
.. |OmeroClients| replace:: :doc:`/developers/GettingStarted`
.. |OmeroGrid| replace:: :doc:`/sysadmins/grid`
.. |OmeroSessions| replace:: :doc:`/developers/Server/Sessions`
.. |OmeroModel| replace:: :doc:`/developers/Model`
.. |ExtendingOmero| replace:: :doc:`/developers/Server/ExtendingOmero`
.. |BlitzGateway| replace:: :doc:`/developers/Python`
.. |DevelopingOmeroClients| replace:: :doc:`/developers/GettingStarted/AdvancedClientDevelopment`
.. _Spring: https://spring.io
.. |previousversion| replace:: %s
.. |current_dbver|  replace:: %s
.. |previous_dbver|  replace:: %s
.. |iceversion| replace:: 3.6.4
.. |postgresversion| replace:: 10
.. |javaversion| replace:: 1.8

.. |Broken| image:: /images/broken.png
             :alt: Broken
.. |Deprecated| image:: /images/deprecated.png
                 :alt: Deprecated
.. |Dropped| image:: /images/dropped.png
              :alt: Dropped
.. |Recommended| image:: /images/recommended.png
                  :alt: Recommended
.. |Supported| image:: /images/supported.png
                :alt: Supported
.. |Unsupported| image:: /images/unsupported.png
                  :alt: Unsupported
.. |Upcoming| image:: /images/upcoming.png
               :alt: Upcoming
""" % (previousversion, conf_autogen.current_dbver,
       conf_autogen.previous_dbver)

omero_subs_github_root = github_root + 'ome/{}/{}/{}/%s'

# OMERO-specific extlinks
omero_extlinks = {
    # GitHub links
    'source' : (omero_github_root + 'blob/'+ branch + '/%s', ''),
    'sourcedir' : (omero_github_root + 'tree/'+ branch + '/%s', ''),
    'commit' : (omero_github_root + 'commit/%s', ''),
    'omedocs' : (doc_github_root + '%s', ''),
    # GitHub decoupled subcomponents
    'dsl_plugin_source' : (omero_subs_github_root.format('omero-dsl-plugin', 'blob', 'v'+conf_autogen.version_dsl_plugin), ''),
    'dsl_plugin_sourcedir' : (omero_subs_github_root.format('omero-dsl-plugin', 'tree', 'v'+conf_autogen.version_dsl_plugin), ''),
    'blitz_plugin_source' : (omero_subs_github_root.format('omero-blitz-plugin', 'blob', 'v'+conf_autogen.version_blitz_plugin), ''),
    'blitz_plugin_sourcedir' : (omero_subs_github_root.format('omero-blitz-plugin', 'tree', 'v'+conf_autogen.version_blitz_plugin), ''),
    'ice_builder_source' : (omero_subs_github_root.format('ice-builder-gradle', 'blob', 'v'+conf_autogen.version_ice_builder), ''),
    'ice_builder_sourcedir' : (omero_subs_github_root.format('ice-builder-gradle', 'tree', 'v'+conf_autogen.version_ice_builder), ''),
    'model_source' : (omero_subs_github_root.format('omero-model', 'blob', 'v'+conf_autogen.version_model), ''),
    'model_sourcedir' : (omero_subs_github_root.format('omero-model', 'tree', 'v'+conf_autogen.version_model), ''),
    'common_source' : (omero_subs_github_root.format('omero-common', 'blob', 'v'+conf_autogen.version_common), ''),
    'common_sourcedir' : (omero_subs_github_root.format('omero-common', 'tree', 'v'+conf_autogen.version_common), ''),
    'romio_source' : (omero_subs_github_root.format('omero-romio', 'blob', 'v'+conf_autogen.version_romio), ''),
    'romio_sourcedir' : (omero_subs_github_root.format('omero-romio', 'tree', 'v'+conf_autogen.version_romio), ''),
    'renderer_source' : (omero_subs_github_root.format('omero-renderer', 'blob', 'v'+conf_autogen.version_renderer), ''),
    'renderer_sourcedir' : (omero_subs_github_root.format('omero-renderer', 'tree', 'v'+conf_autogen.version_renderer), ''),
    'server_source' : (omero_subs_github_root.format('omero-server', 'blob', 'v'+conf_autogen.version_server), ''),
    'server_sourcedir' : (omero_subs_github_root.format('omero-server', 'tree', 'v'+conf_autogen.version_server), ''),
    'blitz_source' : (omero_subs_github_root.format('omero-blitz', 'blob', 'v'+conf_autogen.version_blitz), ''),
    'blitz_sourcedir' : (omero_subs_github_root.format('omero-blitz', 'tree', 'v'+conf_autogen.version_blitz), ''),
    'java_gateway_source' : (omero_subs_github_root.format('omero-java-gateway', 'blob', 'v'+conf_autogen.version_gateway), ''),
    'java_gateway_sourcedir' : (omero_subs_github_root.format('omero-java-gateway', 'tree', 'v'+conf_autogen.version_gateway), ''),
    'matlab_source' : (omero_subs_github_root.format('omero-matlab', 'blob', 'v'+conf_autogen.version_matlab), ''),
    'matlab_sourcedir' : (omero_subs_github_root.format('omero-matlab', 'tree', 'v'+conf_autogen.version_matlab), ''),
    'insight_source' : (omero_subs_github_root.format('omero-insight', 'blob', 'v'+conf_autogen.version_matlab), ''),
    'insight_sourcedir' : (omero_subs_github_root.format('omero-insight', 'tree', 'v'+conf_autogen.version_matlab), ''),
    # API links
    'javadoc' : (downloads_root + '/latest/omero5.4/api/%s', ''),
    'javadoc_gateway_java' : (docs_root + '/omero-java-gateway/' + conf_autogen.version_gateway + '/javadoc/%s', ''),
    'javadoc_blitz' : (docs_root + '/omero-blitz/' + conf_autogen.version_blitz + '/javadoc/%s', ''),
    'javadoc_server' : (docs_root + '/omero-server/' + conf_autogen.version_server + '/javadoc/%s', ''),
    'javadoc_renderer' : (docs_root + '/omero-renderer/' + conf_autogen.version_renderer + '/javadoc/%s', ''),
    'javadoc_romio' : (docs_root + '/omero-romio/' + conf_autogen.version_romio + '/javadoc/%s', ''),
    'javadoc_common' : (docs_root + '/omero-common/' + conf_autogen.version_common + '/javadoc/%s', ''),
    'javadoc_model' : (docs_root + '/omero-model/' + conf_autogen.version_model + '/javadoc/%s', ''),
    'slicedoc_blitz' : (docs_root + '/omero-blitz/' + conf_autogen.version_blitz + '/slice2html/%s', ''),
    'slicedoc_server' : (docs_root + '/omero-server/' + conf_autogen.version_server + '/slice2html/%s', ''),

    'pythondoc' : (downloads_root + '/latest/omero5.4/api/python/%s', ''),
    # Downloads
    'downloads' : (downloads_root + '/latest/omero5.4/%s', ''),
    # Versioned Bio-Formats doc link
    'bf_v_doc' : (docs_root + '/bio-formats/' + conf_autogen.versions_bioformats + '/' + '%s', ''),
    # Miscellaneous links
    'springdoc' : ('https://docs.spring.io/spring/docs/%s', ''),
    'ivydoc' : ('https://ant.apache.org/ivy/history/2.3.0/%s', ''),
    }
extlinks.update(omero_extlinks)

# Edit on GitHub prefix
edit_on_github_prefix = 'omero'

# -- Options for HTML output ---------------------------------------------------

# Custom sidebar templates, maps document names to template names.
html_sidebars['**'].insert(1, 'globalomerotoc.html')

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path.extend(['themes'])

# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
#target = project + '-' + release + '.tex'
#latex_documents = [
#  (master_doc, target, title, author, 'manual'),
#]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = 'images/omero-logo.pdf'

# -- Options for the linkcheck builder ----------------------------------------

# Regular expressions that match URIs that should not be checked when doing a linkcheck build
linkcheck_ignore += [r'http://localhost:\d+/?', 'http://localhost/',
    'http://www.hibernate.org',
    'https://www.jboss.org',
    'https://code.google.com/archive/p/luke/',
    'https://www.youtube.com/channel/UCyySB9ZzNi8aBGYqcxSrauQ',
    'https://httpd.apache.org/docs/current/mod/mod_proxy.html',
    'https://access.redhat.com/articles/3078',
    r'.*[.]sourceforge.net',
    r'https?://www\.openmicroscopy\.org/site/team/.*',
    r'.*[.]?example\.com/.*',
    r'https://spreadsheets.google.com/.*',
    'https://msdn.microsoft.com/en-us/library/aa362244\(v=vs.85\).aspx'
]

exclude_patterns = ['sysadmins/unix/walkthrough/requirements*',
                    'downloads/inplace', 'downloads/cli',
                    'changelog.rst']
