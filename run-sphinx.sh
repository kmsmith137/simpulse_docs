#!/bin/sh
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
#   - To publish your local copy to the web, just do git add/commit/push as usual.
#     I try not to do this too frequently, to avoid bloating the docs repo.  (For
#     example, 'search.js' basically gets rewritten every time the docs get updated.)

set -e
set -x

rm -rf doctrees html

sphinx-build -M html sphinx .
cp -r html/* docs/

rm -rf doctrees html
