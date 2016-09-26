:title: Plan for Monday, September 26, 2016
:status: hidden

9:00 Introduction
=================

- Call me Jason
- A little about myself
- Show them the optimal design results from the BMD conference
- When you ask a question, start with your name.
- Any questions about syllabus, class, etc for me?

9:10 Learning Objectives
========================

- Be able to define strength
- Be able to distinguish "design factor" and "factor of safety"
- Be able to compute the factor of safety
- Be able to define codes and standards in engineering context

Intro Example 9:12
==================

https://en.wikipedia.org/wiki/Engineering_disasters#Hyatt_Regency_Hotel_walkway_collapse_.281981.29

http://commandsafety.com/wp-content/uploads/sites/10/2011/07/7-17-2011-10-48-46-AM.jpg

http://skywalk.kansascity.com/media/hyatt/img/articles/lobby_cropped_jpg_700x400_upscale_q85.jpg

- 1981
- 114 deaths, 200 injuries
- Numerous people standing on suspended walkways
- Alteration of original design
- Findings:

   - The maximum load capacity of the fourth floor walkway was only 53% the
     maximum load capacity of Kansas City Building Code standards
   - The fabrication alterations from the original design doubled the load that
     was received by the fourth floor walkway
   - The deformation and distortion of the fourth floor hanger rods support the
     notion that the collapse began at that point
   - No evidence that the quality of construction or material selection played
     a role in the walkway collapse.

Key concepts: Standards, Strength, Lack of quality control

Mecca Crane Collapse 2015
-------------------------

- 111 people killed, 394 injured
- Their report stated that the crane's 190 meter long boom was not sufficiently
  secured by its operators so as to withstand the high winds present on the day
  of the collapse, and that use of that crane in those 80–105 km/h winds was
  well outside the manufacturer's recommended operating parameters.
- http://www.aljazeera.com/mritems/Images/2015/9/12/da765cc303a64c18a03ee9755582b530_18.jpg
- https://en.wikipedia.org/wiki/Mecca_crane_collapse
- An engineer for the group said that the crane was erected in "an extremely
  professional way", and the accident was an "act of God"
  https://thenypost.files.wordpress.com/2015/09/crane.jpg?w=840

Strength 9:16
=============

- Max stress of any part must be < strength
- strength: property of the component/part/element
- :math:`S` typically denotes strength
- stress: a property of the component's state at a specific point
- :math:`\sigma` normal stress and :math:`\tau` shear stress
- Needs margin to ensure failure rate or improbable
- Focus on areas of the part that are critical stress areas

Class Question
--------------

If you are designing a diving board and you want to guarantee that it will
never break during use which of these would likely be the best to do:

A. Compute the maximum possible stress at every point in the diving board and
   make sure the yield strength of the material is not exceeded.
B. Make sure the maximum load applied to diving board when jumping never
   exceeds the tensile strength load.
C. Compute the maximum possible stress at points that are likely to have the
   highest stress and make sure the yield strength of the material is not
   exceeded.
D. Draw a moment diagram of the cantilever beam and find the highest stress due
   to the moment to ensure it never exceeds the yield strength.

Design Factor and Factor of safety 9:22
=======================================

Design Factor
   The pre-design target safety margin, i.e. the desired factor of strength
   over max ??
Factor of Safety
   The post design, actual, minimum factor of strength.

FoS should always be > than the DF!

Why would the Factor of Safety be different than the design factor?

Factor of Safety Method

- Analyze all loss of function modes
- Choose mode that leads to smallest design factor to govern decisions

This is most typically:

.. math::

   n_d = \frac{S}{\sigma \textrm{ or } \tau}

because stress may not vary linearly with load.

Aluminum Can Demo
-----------------

- cold formed
- 92.5% to 97% aluminum, <5.5% magnesium, <1.6% manganese, <0.15% chromium
- one of the most optimized designs you can find
- their goal is to reduce material
- 13.5 g (0.5 oz) or 30 cans per pound
- one failure mode is internal pressure: pressure vessel design problem
- one half trillion are made per year
- excellent packing factor: 91%
- small design changes can save millions of kg of aluminum
- pressure in can gives strength: stand on full can but maybe not on empty one
- video: http://thekidshouldseethis.com/post/the-ingenious-design-of-the-aluminum-beverage-can

Sample Problem
--------------

A square cross section rod is loaded axially with a static load of 1000+/-10
lbs. The strength of the material is 25 kpsi and the desired design factor is
4. Determine the minimum width of the square cross section. Then select a
preferred fractional inch size from Table A-17 and report the factor of
safety.

Why do we have factor of saftey? 9:35
=====================================

What's wrong with this?:

   The yield strength of hot rolled mild steel is 220 MPa.

Design factor
   deterministic based on absolutes

.. math::

   n_d = \frac{loss of function parameter}{maximum allowable parameter}

Class Question
--------------

If the load that will cause failure is between 90 and 110 lbs and you'd like a
design factor of 2, what is the max allowable load?

.. math::

   P_{max} = \frac{P_{fail}}{n_d} = \frac{90 \textrm{ lbs}}{2} = 45 \textrm{ lbs}

Uncertainty

- Gaussian distributions can model many real world observations
- We can make predictions of quality, strenght, loads, etc in a stochastic
  manner.
- Probabilities are the area under the Gaussian probaility density curve and
  are found by integration.
- The book provides a table of probabilities for a nominal Gaussian curve.

Standards/Codes 9:45
====================

standard
   set of specifications to achieve uniformity, efficiency, quality
code
   specs to control saftey, efficiency, performance

Wrap Up 9:47
============

- Homework 1 will be posted after class
- 30 designs are due Friday in class: bring notebook
- Questions
