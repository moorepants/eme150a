:title: Resources
:sortorder: 4

Exam Review
===========

- `Final Exam Study Guide <{filename}/pages/final-exam-study-guide.rst>`_

Tables
======

- `Standard Normal Table`_ (Table A-10 in [1]_)
- `Preferred Sizes`_ (Table A-15 in [1]_) [2]_
- `Second moment of area for various shapes`_ (Table A-18 in the [1]_)

.. _Standard Normal Table: https://en.wikipedia.org/wiki/Standard_normal_table
.. _Preferred Sizes: https://en.wikipedia.org/wiki/Preferred_number
.. _Second moment of area for various shapes: https://en.wikipedia.org/wiki/List_of_area_moments_of_inertia

.. [1] *Shigley's Mechanical Engineering Design*, Budynas and Nisbett, 10th Edition,
   McGraw Hill Education. ISBN 978-0-07-339820-4
.. [2] I'm looking for a better table for this. Something more like the book.
   Let me know if you find one (or make one). *-- Jason*

Python for Mechanics
====================

We will be using Python in this class for our computations. Python is a general
purpose high level programming language that has thousands of packages. We will
primarily make use of SymPy_ to solve mechanical design problems. You will need
to download and install the Anaconda Distribution of Python (Python 3.5
version) from:

https://www.continuum.io/downloads

Anaconda is also be available in the CAE lab in Bainer.

Alternatively, you can create Jupyter notebooks using the SageMathCloud_ or
Wakari_ web applications without having to install any software.

.. _SageMathCloud: https://cloud.sagemath.com
.. _Wakari: https://wakari.io
.. _SymPy: http://sympy.org

Development Version of SymPy
----------------------------

The next release of SymPy will include a singularity function module and a beam
module for solving 2D beams, much like what we do in class. If you'd like to
try this out pre-release, you'll need to install the development version of
SymPy. It is recommended to make a new conda environment for this. If you open
a terminal (OSX/Linux) or the Anaconda command prompt (Windows) you can enter
these commands to set things up::

   $ conda create -n sympy-dev python=3.5 anaconda
   $ source activate sympy-dev  # this is simply "activate sympy-dev" on Windows
   (sympy-dev)$ conda uninstall sympy

Now download the development version of SymPy from:

https://github.com/sympy/sympy/archive/master.zip

and unzip the file in a known location, e.g.
``/home/jason/Downloads/sympy-master``. Finally install with::

   (sympy-dev)$ conda develop /home/jason/Downloads/sympy-master

Now, when you have this environment activated you will be using the development
version. You can activate the environment from the Anaconda Navigator, Jupyter
Notebook, or the command line. You can learn about using the two modules in the
development documentation:

- `Singularity Functions <http://docs.sympy.org/dev/modules/functions/special.html#module-sympy.functions.special.singularity_functions>`_
- `Beams <http://docs.sympy.org/dev/modules/physics/continuum_mechanics/index.html>`_

Contact Stress Failures
=======================

- `Contact stress visualization from photoelasticity
  <https://upload.wikimedia.org/wikipedia/commons/1/18/Kontakt_Spannungsoptik.JPG>`_
- `Gear teeth spalling <http://www.rttech.com.au/wp-content/uploads/2010/06/mt6.jpg>`_
- `Bearing Brinelling <http://www.linearmotiontips.com/wp-content/uploads/2013/04/False-brinelling-300x300.jpg>`_
- Pitting:

  - http://www.differentials.com/wp-content/uploads/2011/12/Pitted-Bearing_0159.jpg
  - http://www.knowyourparts.com/public/uploads/2013/06/61274DiagSolnsp_00000022462.jpg
  - http://thereliabilityroadmap.com/assets/images/pitting3.png
  - http://thebiketube.com/sites/all/files/tutorials/pitted-ball-bearing-races.jpg

Fatigue Failures
================

- `R. R. Moore Fatigue Test of AL 6061-T6 [Video] <https://youtu.be/93I6Wk7GZhI>`_
- `FATIMAT Rotating Bending Machine Prototype [Video] <https://youtu.be/52knsY5AWIc>`_
- `Notable Fatigue Failures <https://en.wikipedia.org/wiki/Fatigue_%28material%29#Notable_fatigue_failures>`_
- `Xcelerator Cable Snap Accident <https://youtu.be/VFL2ybuxeUY>`_
