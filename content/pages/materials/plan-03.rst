:title: Plan for Wednesday, September 29, 2015
:status: hidden


- Poll students about devices in class:
  - Laptop to class? On Fridays?
  - Laptop or tablet?
  - Laptop, tablet, or smart phone?

9:55-10:00  Factor of Safety question
10:00-10:05 Break
10:05-10:10 Project One intro activity
10:10-10:20 Break up into CATME groups
10:20-10:25 Team introductions
10:25-10:45 Reverse engineering
10:45-10:50 Discuss

In the news
-----------

Ethics: Volkswagen scandal:
https://en.wikipedia.org/wiki/Volkswagen_emissions_violations

Saftey: Mecca crane collapse:
https://en.wikipedia.org/wiki/Mecca_crane_collapse
An engineer for the group said that the crane was erected in "an extremely
professional way", and the accident was an "act of God"
https://thenypost.files.wordpress.com/2015/09/crane.jpg?w=840

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

9:00
====

- Questions?

- Feedback

  - How many drawings have you done?
  - Work on handwriting and removing the notes too quickly.

- Review of uncertainty

  - Gaussian distributions can model many real world observations
  - We can make predictions of quality, strenght, loads, etc in a stochastic
    manner.
  - Probabilities are the area under the Gaussian probaility density curve and
    are found by integration.
  - The book provides a table of probabilities for a nominal Gaussian curve.

9:05
====

Free Body Diagrams

- system: any isolated part or portion of a machine or structure
- used to isolate and identify both internal and external loads on a design
  element
- defines:

  - coordinate systems
  - known and unknown forces

:math:`\sum F = \frac{dp}{dt}` and :math:`\sum M = \frac{dH}{dt}`

Static Equilibrium (no velocity)

F = 0 and M = 0

9:15
====

Exercise: FBD Question

9:20
====

Example FBD

9:35
====

Question: FBD diagram question

9:45
====

- Questions?
- HW Questions?
- 50 designs due


TODO
====

- Print Table A-10

9:00
====

Rocklin mini maker faire: http://makerfairerocklin.com/ Oct 3

Questions?

Review mechanical design

Review uncertainty
   Every number has an uncertainity associated with it and you must take this
   into account in design.
Review design factor and factory of saftey
   Design factors help account for uncertainity. The design factor is the
   desired value and the factor of the safety is the actual value.

9:05
====

Stochastic failure criteria and reliability

Goals
-----
- Understand that uncertainty is more realistically modeled by statisical
  models.
- Be able to compute Gaussian probablities using a transform table.

9:15
====

Exercise

9:20
====

Dimensions, units, sig figs

Tolerances
----------

- Nominal sizes are note exact sizes
- Tolerance limits are specified as absolutes
- Tight tolerances = higher costs
- Dimensioning should include the minimum non-redudant info
- Dimensions should be chosen based on part functionality
- Tolerance stackup

Units
-----

- We will be using two unit system: International System of Units and U.S.
  Customary Units
- US, Liberia, Burma only countries that use the U.S. system.
- F = MLT^{-2}

M = FT^2 / L = (pound-force) (second)^2 = lbf * s^2 / ft = slug

- lbf: pound force
- kip : kilo pounds force

F = ML / T^2 = (kilogram) (meter) / (second)^2 = kg m / s^2 = N

W = mg

g = 9.81 m/s^2 = 32.2 ft/s^2

- Mars climate orbiter: https://en.wikipedia.org/wiki/Mars_Climate_Orbiter
- Cost about $600 million
- output lbf s instead of N s

Sig figs
--------

- sig figs are inferred by shown digits (except leading): 0.700"
- scientific notation: 706.0, 7.060x10^2, 0.7060x10^3, 7.060E2
- the smallest sig figs in a calc fix the number of sig figs you should report
- do all calcs at greatest accuracy possible and round at the end

9:30
====

Tolerance stack up exercise.

9:35
====

Free body diagrams

- used to isolate and identify internal and external loads on a design element
- includes coordinate system(s)
- lists known and unknown forces acting on the element(s)
- loads are required to determine stress in the member

Static equilibrium:

Sum F = 0
Sum M = 0

9:45
====

Exercise

Collect feedback

What we will go over next time: shear and moment diagrams for beams

Homework will be posted after class.
