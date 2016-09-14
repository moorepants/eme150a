The course website for Jason K. Moore's University of California, Davis
Mechanical Design course (EME 150A). The rendered version can be viewed at:

http://moorepants.github.io/eme150a

This site is generated with Pelican_.

.. _Pelican: getpelican.com

Build Instructions
==================

Install miniconda_. Create an environment for Pelican sites::

   $ conda create -n pelican python=2 pygments pip jinja2 docutils markupsafe python-dateutil pytz six unidecode fabric
   $ source activate pelican
   (pelican)$ pip install pelican ghp-import

Clone the plugin repository (for the render_math plugin)::

   $ mkdir ~/src
   $ git clone git@github.com:getpelican/pelican-plugins.git ~/src/

Rebuild and serve the site locally::

   (pelican)$ fab reserve

Push the site to Github pages::

   (pelican)$ fab gh_pages

.. _miniconda: http://conda.pydata.org/miniconda.html

License
=======

Creative Commons CC0

   To the extent possible under law, Jason K. Moore has waived all copyright
   and related or neighboring rights to EME150A Mechanical Design Course
   Website. This work is published from: United States.
