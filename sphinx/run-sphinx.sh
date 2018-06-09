#!/bin/sh
#
# This script will run 'sphinx-build' to generate static HTML files in ../docs,
# from the .rst source files in this directory.
#
# Note that you need to do 'make install' in the cmake build directory first (doing 'make' is not enough).
#
# (This is the reason for doing documentation generation in this standalone script, rather than integrating
#  it with the rest of the build process.  Some day this will be fixed!)

set -e
set -x

# !!! Without this, 'sphinx-build' sometimes incorrectly concludes that it doesn't need to rebuild !!!
rm -rf doctrees html

sphinx-build -M html . .
cp -r html/* ../docs/
