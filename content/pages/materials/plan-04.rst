:title: Plan for Wednesday, September 28, 2016
:status: hidden

9:00
====

Review design factor and factor of safety
   Design factors help account for uncertainity. The design factor is the
   target specification and the factor of the safety is the actual value.

Objectives
----------

- be able to calculate factors of safety
- be able to use preferred size choices
- understand that uncertainty is more realistically modeled by statisical
  models
- be able to compute Gaussian probablities using a transform table

9:10 Example: Factor of Saftey Calculation
==========================================

A square cross section rod is loaded axially with a static load of 1000+/-10
lbs. The strength of the material is 25 kpsi and the desired design factor is
4. Determine the minimum width of the square cross section. Then select a
preferred fractional inch size from Table A-17 and report the factor of
safety.

9:20 Uncertainty
================

Selection of Design Factor

- subjective
- follow industry standards and codes

standard
   set of specifications to achieve uniformity, efficiency, quality
code
   specs to control saftey, efficiency, performance

Depends on:

- degree of uncertainty about loading
- degreee of uncertainty about material strength and structure
- consequences of failure > human safety, economics
- cost of providing a high factor of safety

FoS is deterministic based on absolutes

Boils down to the probability of failure.

What's wrong with this?:

   The yield strength of hot rolled mild steel is 220 MPa.

Uncertainty

- Gaussian distributions can model many real world observations
- We can make predictions of quality, strenght, loads, etc in a stochastic
  manner.
- Probabilities are the area under the Gaussian probaility density curve and
  are found by integration.
- The book provides a table of probabilities for a nominal Gaussian curve.

Stochastic failure criteria and reliability

Gaussian, table a-17 etc

Exercise

9:35
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

9:40
====

Tolerance stack up exercise.

9:45
====

- Questions?
- HW Questions?
- 30 designs due Friday
- HW 1 due Monday
- Read sections on free body diagrams and beam bending. 3-1 to 3-3
- Bring laptop to class with Anaconda Python 3.5 installed.
