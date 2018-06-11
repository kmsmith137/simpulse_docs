Introduction and Installation
=============================

simpulse is a C++/python library for simulating FRB's and pulsars.  

It is not designed for speed, but simulates pulses very accurately, keeping track of 
effects such as dispersion smearing within frequency channels, or finite time sampling artifacts.

Currently, simpulse makes two-dimensional simulations of FRB's (where the axes are frequency and time),
and one-dimensional simulations of pulsars (where the axis is time).  Two-dimensional pulsar simulations
are coming soon!

Prerequisites
-------------

  - Standard prerequisites

    - a relatively recent C++ compiler

    - python, numpy

    - cmake

    - matplotlib is not required, but recommended in order to run example scripts

  - pybind11_, a C++ header-only library for C++/python interoperability.  I think
    the only option here is to build from source.  The following worked for me::

         git clone https://github.com/pybind/pybind11
         cd pybind11
         mkdir build
         cd build

         # !!! The -DPYBIND11_PYTHON_VERSION=2.7 flag is important here !!!
	 # This tells pybind11 that you will be using python 2 instead of python 3.

         cmake -DCMAKE_INSTALL_PREFIX=$HOME 
         make install


  - FFTW3_, a portable high-performance FFT library

    - Linux (Ubuntu): ``sudo apt-get install libfftw3-dev``

    - Linux (CentOS): ``sudo apt-get install fftw-devel``

    - OSX: ``brew install fftw``

    - Building from source.  The following worked for me::

         wget http://www.fftw.org/fftw-3.3.8.tar.gz  # latest version as of June 2018
         tar zxvf fftw-3.3.8.tar.gz
         cd fftw-3.3.8

         # You may as well use --enable-single here, to build both single-precision 
	 # and double-precision versions
         ./configure --prefix=$HOME --enable-shared --enable-single
         make
         make install


Installation
------------

Quick-and-dirty instructions::

  git clone https://github.com/kmsmith137/simpulse
  cd simpulse
  mkdir build
  cd build
  cmake -DCMAKE_INSTALL_PREFIX=$HOME ..
  make -j4    # -j4 uses four threads and is optional
  make install

In a little more detail:

  - This is a standard (I hope!) cmake build.  I recommend the "out-of-source" mode for building packages with
    cmake, where you create a separate ``build`` directory for compiling.

  - When you run `cmake` in the build directory, it should locate all of the necessary ingredients on your machine 
    (fftw3, python, pybind11, etc.) and create a Makefile.  

    After that, you shouldn't need need to run cmake again.  It should suffice to run `make` invocations such as::

      cd build
      make -j4       # build everything (-j4 uses four threads and is optional)
      make install   # install libraries to $HOME/lib, headers to $HOME/include, etc.
      make uninstall # undo 'make install': delete simpulse libraries from $HOME/lib, etc.
      make clean     # delete all build products, but don't undo 'make install'

    However, note that these `make` invocations *will only work in the build directory where you originally ran cmake*.

  - I usually run cmake with ``-DCMAKE_INSTALL_PREFIX=$HOME``.
    Then `make install` will install simpulse libraries in $HOME/lib, headers in $HOME/include, etc.
    This can be changed if you want to install simpulse elsewhere.  By default, cmake installs to /usr/local.

  - Here are some more influential cmake variables, which can be set with ``cmake -DVAR=VALUE``::


      CMAKE_CXX_FLAGS: compiler flags
      CMAKE_MODULE_PATH: look for cmake modules (ending in .cmake) in this directory
      CMAKE_INCLUDE_PATH: look for header files in this directory
      CMAKE_LIBRARY_PATH: look for libraries in this directory
      CMAKE_PREFIX_PATH: look for libraries in ${CMAKE_PREFIX_PATH}/lib,
                         header files in ${CMAKE_PREFIX_PATH}/include, etc.

  - Let me know if you have any trouble with cmake.  I am still getting used to it, so there may
    be bugs in the build scripts, or room for improvement.

.. _FFTW3: http://www.fftw.org/
.. _pybind11: https://github.com/pybind/pybind11
