Example 3: python phase model
=============================

*Note that the documentation is for the cmake_pybind11 branch of simpulse, not the master branch!*
The cmake_pybind11 simpulse branch will be merged to master soon.

Note: before running the example scripts, you will need to do ``make install`` in the build directory (``make`` is not enough).

This example shows how to define a new pulsar phase model in python, by subclassing
'class simpulse.phase_model_base'.  We implement a toy example: a five-parameter 
"sinusoidal" phase model in which the pulse frequency is a sinusoidal function of time.  

The plots below are similar to :ref:`Example 2: simulating a pulsar`: we show an example
of the phase model phi(t), and the associated pulsar simulation.

.. image:: example3_phase_model.png
   :width: 800px
   :height: 600px

.. image:: example3_pulses.png
   :width: 800px
   :height: 600px

Here is the script (simpulse/examples/python/03-python-phase-model.py).

.. literalinclude:: ../../simpulse/examples/python/03-python-phase-model.py
    :language: python
