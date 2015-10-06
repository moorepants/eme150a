:title: Plan for Friday, September 25, 2015
:status: hidden

Class Activities
================

=========== ====================================================================
9:00-9:10   Introduction, meet your neighbors
9:10-9:15   Questions about syllabus, about class, etc.
9:15-9:25   What is mechanical engineering design? Team up with your three
            nearest neighbors and come up with a definition of mechanical
            design in your own words.
9:25-9:30   Discuss answers, write key words on the board
9:30-9:40   Stress/Strength
9:40-9:45   Stress/Strength question
9:45-9:55   Factor of Safety
9:55-10:00  Factor of Safety question
10:00-10:05 Break
10:05-10:10 Project One intro activity
10:10-10:20 Break up into CATME groups
10:20-10:25 Team introductions
10:25-10:45 Reverse engineering
10:45-10:50 Discuss
=========== ====================================================================

Intro 9:00
==========

- Jason and Matt
- Lecturer
  - teach and improve engineering education
  - mention that we will try out new things in class and that i want feedback
- Group into groups of 4
  - Your name
  - What machines you hope to design in the future
- Any syllabus questions?
  - Lecture topics will change, hw and project dates are fixed, check
  - Lecture prep guides: you will be tested on these things
  - Ask questions on piazza
- Poll students about devices in class:
  - Laptop to class? On Fridays?
  - Laptop or tablet?
  - Laptop, tablet, or smart phone?

Mechanical Design 9:15
======================

- Group into groups of 4.
- Goal: definition of mechanical engineering design in 1-2 sentences.
- 10 minutes, ends at 9:25
- Use previous experience and chapter 1

My definition
-------------

The process of creating a solution to a problem or need utilizing mechanical
systems and principles under constraints such as limited resources, limited
knowledge, or codes and standards. The process involves creativity, ideation,
ingenuity, and analysis that may need to guarantee safety, maintainability,
sustainability, ethical standards, etc.

difference in need (beginning) and problem (specifications required)

In the news
-----------

Ethics: Volkswagen scandal:
https://en.wikipedia.org/wiki/Volkswagen_emissions_violations

Saftey: Mecca crane collapse:
https://en.wikipedia.org/wiki/Mecca_crane_collapse
An engineer for the group said that the crane was erected in "an extremely
professional way", and the accident was an "act of God"
https://thenypost.files.wordpress.com/2015/09/crane.jpg?w=840

Typical process
---------------

- understand the problem
- identify the knowns
- id the unknowns and formulate solution strategy
- state all assumptions and decisions
- analyze the problem
- eval solution
- present

Standards/Codes
===============

standard
   set of specifications to achieve uniformity, efficiency, quality
code
   specs to control saftey, efficiency, performance

Strength 9:30
=============

- Max stress < strength
- strength: property of the component/part/element
- :math:`S` typically deontes strength
- stress: a property of the component's state at a specific point
- :math:`\sigma` normal stress and :math:`\tau` shear stress
- Needs margin to ensure failure rare or improbable
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

Uncertainty 9:45
================

What's wrong with this?:

   The yield strength of hot rolled mild steel is 220 MPa.

Design factor
   deterministic based on absolutes

.. math::

   n_d = \frac{loss of function paramter}{maximum allowable parameter}

Class Question
--------------

If the load that will cause failure is between 90 and 110 lbs and you'd like a
design factor of 2, what is the max allowable load?

.. math::

   P_{max} = \frac{P_{fail}}{n_d} = \frac{90 \textrm{ lbs}}{2} = 45 \textrm{ lbs}

Factor of safety
================

Factor of Safety Method

- Analyze all loss of function modes
- Choose mode that leads to smallest design factor to govern decisions

Factor of Safety
   The actual design factor after the part is fully designed.

Why would the Factor of Safety be different than the design factor?

This is most typically:

.. math::

   n_d = \frac{S}{\sigma \textrm{ or } \tau}

because stress may not vary linearly with load.

Sample Problem
--------------

A square cross section rod is loaded axially with a static load of 1000+/-10
lbs. The strength of the material is 25 kpsi and the desired design factor is
4. Determine the minimum width of the square cross section. Then select a
preferred fractional inch size from Table A-17 and report the factor of
safety.
