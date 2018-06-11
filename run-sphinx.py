#!/usr/bin/env python
#
# This script will run 'sphinx-build' to generate static web pages in docs/,
# from the .rst and image files in sphinx/, by scraping docstrings in the
# simpulse python module, and by reading source files in the main simpulse repo.
#
#   - This script expects the main simpulse repo to be in ../simpulse.
#
#   - This script also expects the simpulse python module to be importable,
#     i.e. you'll need to do 'make install' in the main simpulse repository 
#     first.  (This also means that if you update a docstring and want it to
#     appear in the documentation, you need to do 'make install' in the main
#     simpulse repo, then run this script.)
#
#   - After the script has run, you can browse a local copy of the documentationm
#     by pointing your browser to docs/index.html.
#
#   - To publish your local copy to the web (https://kmsmith137.github.io/simpulse_docs/), 
#     just do git add/commit/push as usual.  I try not to do this too frequently, to avoid 
#     bloating the docs repo.  (For example, 'docs/search.js' basically gets rewritten 
#     every time the docs get updated.)


import os
import sys


####################################################################################################
#
# Sanity checks


# Check that we can import simpulse first (for docstring scraping)
import simpulse

script_dir = os.path.dirname(os.path.realpath(__file__))

if os.getcwd() != script_dir:
    print >>sys.stderr, "run-sphinx.py: to avoid confusion, the current working directory must be the same as the directory containing the script"
    print >>sys.stderr, "    (cwd='%s', script_dir='%s')" % (os.getcwd(), script_dir)
    sys.exit(1)

if not os.path.exists('../simpulse'):
    print >>sys.stderr, "run-sphinx.py: this script expects the 'simpulse' repository (https://github.com/kmsmith137/simpulse) to be in ../simpulse"
    sys.exit(1)

f = '../simpulse/examples/python/01-simulating-frb.py'
if not os.path.exists(f):
    print >>sys.stderr, "run-sphinx.py: directory ../simpulse exists, but not", f
    sys.exit(1)

for f in [ "sphinx/index.rst", "docs/index.html" ]:
    if not os.path.exists(f):
        print >>sys.stderr, "run-sphinx.py: file '%s' does not exist ?!"
        sys.exit(1)


####################################################################################################


def xsystem(cmd, show=True):
    if show:
        print '+', cmd

    if os.system(cmd):
        print >>sys.stderr, "Shell command failed:", cmd
        sys.exit(1)


# The -E flag forces 'sphinx-build' to reread all its input files, even if nothing
# appears to have changed.  This is necessary because 'sphinx-build' has no way of
# knowing if docstrings have been changed since last time.

xsystem("sphinx-build -E -b html sphinx docs")

print
print "The documentation uses docstrings obtained by importing the 'simpulse' python module."
print "If this is not up-to-date, the documentation will also be out of date.  In this case,"
print "you should do 'make install' in the main simpulse repo, then rerun the run-sphinx.py script."
print
print 'A local copy of the documentation has been built successfully!'
print 'To view it, point your web browser here:'
print
print '    file://%s' % os.path.join(os.getcwd(), 'docs/index.html')

