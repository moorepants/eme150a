:title: Plan for Friday, October 2, 2015
:status: hidden

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

- The Martian Movie
- Questions?
- Are office hours at good times?
- Review: Free Body Diagrams

  - Draw system bound in whatever way is useful for problem
  - Equilibrium: F = 0, M = 0
  - Basic maximum stress for axial, bending, and torsion

- Pin joint demo

Today's goals:

 - Review of transversely loaded beams
 - Be able to draw shear and bending moment diagrams
 - Utilize singularity functions to efficiently draw diagrams

9:10
====

Shear and Bending diagrams

- Relation of q, V, M

9:20
====

- Shear and bending question

9:25
====

- Singularity functions for beams
- Example with singularity functions

9:40
====

- Singularity question

9:45
====

Wrap up

- Beam shear and moment values are piecewise functions
- Load, shear, and bending are related by derivatives
- Complex loadings can be more easily calculated with singularity functions

9:50
====

Break

10:00
=====

- Description of the next step in the project: 5 more detailed designs are due
  next friday.

  - Answer more questions, more sketches, add calculations
  - Around 2 full notebook pages that are dense per design: ultimately will need
    3 pages of computer content for the final design
  - Focus on designs that will allow you to think about the loads, stresses,
    strength, motion
  - Describe lightning talks for next Friday

    - 2 minutes to describe to your group a design
    - 2 designs per member
    - practice before hand, make short script about main points (2 minutes
      doesn't give you time to flounder)
    - 2 minute review from groups

Questions?

10:10
=====

- Get in groups and work together on the homework or the provided examples
- Check on group sizes
- Have notebook out and ready for grading

10:45
=====

- Questions
- Collect feedback: feedback for the week will happen on Fridays
- positive, negative for the week and time spent outside of class
