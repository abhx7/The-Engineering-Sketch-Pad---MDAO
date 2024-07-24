Engineering Sketch Pad
https://acdl.mit.edu/ESP/
Geometry in CFD
The current use of geometry in design processes is ad hoc and often consists of various tools. Conceptual Design tools
suggest the shape but do not realize 3D geometry. Some disciplines have early-stage specialized tools that build 3D
parametric models, but they do not consider the larger multidisciplinary design. Some disciplines remain "geometry free"
during design, resulting in errors and a different final realized geometry.
A single, multidisciplinary geometry modeling system is needed to support complex geometric requirements in later stages.
The system should generate geometries that do not need fixing or repair, and output the designed geometry seamlessly for
commercial CAD systems to import the model without loss of accuracy in the shapes represented.
Relegating commercial CAD to the end of the design process may be surprising, but its focus has been, and is,
manufacturing, not analysis. The current state of affairs is partly due to the focus on manufacturing rather than analysis.
Use of Geometry in Meshing
● A gap exists between creating geometry and analyzing geometry. This is due to the process first creating the geometry,
then transferring the geometry information from a CAD-based geometry to a meshing tool, and then finally to the
appropriate analysis tools.
● The usual connection between high-fidelity analysis codes and geometry is performed by a grid generator.
● 3D meshing software ultimately requires topological information to realize a closed “watertight” model.
● Each instance of the Master-Model/Feature tree is a BRep. Boundary Representations (BReps) are the standard data model
that holds both the geometric and topological entities that supports the concept of a “solid”.
● The topology is directly related to both the design intent of the Feature Tree and the construction methods of the
underlying CAD system.
● BReps have a tolerance that determines the meaning of “closure” for connected entities.
● To deal with gaps and overlaps without a program halt which then requires intervention, we can either “fix” the geometry
or the Breps created.
● Currently, most BRep-based applications “fix” the geometry by representing the the geometry definition in a different
manner. This causes various side effects like inconsistencies, errors, complexity and this process itself is not automatic,
hence it needs to be done manually and thus, is time consuming.
There has been tremendous progress since early CAD softwares but there are still some drawbacks for its usage in the MDAO environment.
File Formats
Each CAD system or geometry kernel uses a different mathematical formulation to represent the same types of surfaces, and also have different
tolerances for closure. Therefore, while transferring data it may be found that the model may be open now again and need patching.
- IGES file format contains data that is defined as disjoint and unconnected surfaces and curves, with no explicit notion of topology.
- STEP file format supports topology as well as geometry. This format is seldom used in practice as constructing a STEP reader is
complex and requires a complete solid modeling geometry kernel to deal with the data.
- STL combines a discretized view of the Brep as well as its geometry and topology can provide a complete, and easier to use, access
point. (Needs further study why its not used in flow analysis)
- EGADS
- NMB
A CAD-based Approach
Pros
● Defeaturing for design progression and multi disciplinary process
● Consistency in design process (using same suite of parameters)
● Ability to take feedback to make corrections due to parameterisation
Cons
● Expensive CAD licenses
● Geometry files incompatible with mesh generators and must undergo
tedious “CAD healing” during the meshing process
● Redesigned geometry alterations for different disciplinary analysis is
likely to conflict with the definitions of the original geometry
● Proprietary formats that are hard to generate and modify externally
● Specialized construction not available as primitives are pre-defined
(inability to create fully-parametric user-defined primitives)
● Incompatible parameterisation
● Very scarce training for using Parametric CAD in MDAO
Current methods to achieve these objectives is Constructive Solid Geometry (CSG) using Conceptual Design tools; this is the
natural foundation on which the modelling techniques are based, allowing flexibility in creating complex structures from
simple components.
Next, a combination of 2 approaches is used - CAD systems and their “feature” based view of construction, and Bottom-Up
methods which generate solid “components”.
To realise the MDAO objectives via the Bottom-Up approach, EGADS, a new software suite is built as well as entire ESP
architecture, which is explained next.
● To support the entire Multi-Disciplinary Analysis and Optimization (MDAO) process from
conceptual to detail design in a seamless manner, as well as multi fidelity analysis.
● To make the process user-friendly and support for automation to minimize unnecessary or
repetitive human effort.
Objectives
● OpenCASCADE
○ Fully functional Open-Source Solid modeling geometry kernel
○ Creates geometry primitives and generates BRep model
○ Performs Bottom-Up construction and CSG operations
○ Fully Object-Oriented C++ API
OpenCASCADE
ESP
Parts of ESP Architecture
OpenCASCADE
EGADS
ESP
● EGADS (Electronic Geometry Aircraft Design System)
○ Open source, object-Based software built on top of OpenCASCADE
○ procedural-based API reducing the level of programming complexity
and the huge suite of methods of OpenCASCADE
○ Full support for current platforms and can be driven by multiple user
applications
○ outputs STEP file as well as native EGADS format
Parts of ESP Architecture
OpenCASCADE
EGADS
OpenCSM
ESP
● OpenCSM is built on EGADS
○ Parameters each having unique names are all stored as two-dimensional arrays of
floating point numbers (parameters can either be external or internal)
○ Feature trees are defined in terms of a binary-like tree of branches. Each branch has
an associated type which describes the operation to be performed. Branches can
have zero to two parents.
○ While not strictly object-oriented, the API has been designed in an object-based
manner, making it directly interfacable with object-oriented systems
○ Extensible via user-defined primitives and directly provides sensitivities
Parts of ESP Architecture
ESP is a browser-based system at the top of the architecture which provides the user the ability to interact with
a configuration by building and/or modifying the design parameters and feature tree that define the
configuration.
● Captures the design intent in a simple, easy to read, nonproprietary text file (ASCII) that is easily
modifiable by any other component in an MDAO environment, viewed in a web-based GUI.
● Supports easy integration into a larger process by allowing geometry import/export using file standards
(either discrete or analytic) and direct connections to a number of 3D grid generators, preventing loss of
critical information when the standard does not support the data in the current available systems.
● The ability to easily add customized features to the system. (UDPs)
ESP
● Provides attribution at all levels, which is an essential capability when one wants to
connect (in a multi-disciplinary way) the various parts of the various representations.
● Supports the generation of multiple models from the same parameterization and
provides for Backward compatibility due to non-sequential design workflow (Phase).
● Open-source and is not encumbered with any licensing restrictions. CAPS libraries
through AIM plugins enables an MDAO environment freely.
● Provides analytic parameter sensitivity (for much of the build), making it suitable for
the gradient-based optimization processes that are frequently used in MDAO
environments. The sensitivity of any part of a configuration with respect to any design
parameter.
CAPS
ESP AIMs
pyCAPS: A Python Interface to the Computational Aircraft Prototype Syntheses
CAPS stands for "Computational
Aircraft Prototype Syntheses". It is
an infrastructure for multifidelity,
multidisciplinary modeling that can
be integrated within a framework.
CAPS enables physics-based
design by analysis and manages
the flow of information between
the geometry subsystem, various
analysis interface modules (AIMs),
and the environment driven by an
external design process.
CAPS API
● Enhances automation by tightly coupling analysis with geometry and allow interdisciplinary analysis with “field” data
transfer and also does not replacing optimization algorithms
● Provides the tools and techniques for generalizing analysis coupling like in multidisciplinary coupling and
multi-fidelity coupling
● Provides the tools for rigorously dealing with geometry (single and multi-fidelity) in a design process where
OpenCSM connects design parameters to geometry and CAPS itself connects geometry to analysis tools.
● It hides all of the individual analysis details but does not make analysis tool a “black box”
● Intends to input and attribution driven automated (not automatic) meshing
Analysis Interface Module (AIM) is used to interface between CAPS framework and analysis tools
Low Fidelity
- AWAVE
- FRICTION
- AVL
- XFoil
Structural Analysis
- Masstran
- MYSTRAN
- NASTRAN
- ASTROS
- TACS
Meshing
Surface
Native EGADS
AFLR4
Volume
TetGen
AFLR3
Pointwise
3D CFD
Cart3D
Fun3D
SU2
model is watertight after importing from
external sources
● Supports easy integration into a larger process by allowing geometry import/export using file standards (either
discrete or analytic) and direct connections to a number of 3D grid generators, preventing loss of critical information
when the standard does not support the data in the current available systems.
Step by Step Process of a Designing a Wing in ESP
Integrated Environment
Including CFD Simulation
Each step is a Phase.
Geometry Creation
using Low Fidelity Analysis tools
Attribution
I. Airfoil Section
Using Xfoil, to generate naca airfoil of appropriate characteristics optimised with respect to
Cl/Cd values
https://web.mit.edu/drela/Public/web/xfoil/
Camber Calculations
Maximum thickness Calculations
Location of Maximum
camber Calculations
MSES code could be used for shape
optimisation after Xfoil analysis.
II. Wing
Using AVL, to generate wing of appropriate characteristics optimised with respect to
taper ratio
https://web.mit.edu/drela/Public/web/avl/
Wing Optimisation
Structural Analysis
Various software analysis suites like masstran and MYSTRAN can
be used to optimise the material composition, integrity as well as
other structural characteristics of the model, especially the fuselage.
Sensitivities
What is sensitivity? Why is it important?
Sensitivity is the gradient of the objective and constraint functions with respect to variables of the environment
(like design).
It is important so that we can verify the accuracy our results (like to reduce spatial discretization errors).
One major goal is obtaining sensitivities of output functionals to CAD design parameters. Among the various
proposed methods, the Computational Aircraft Prototype Syntheses (CAPS), shipped with Engineering Sketch
Pad (ESP), caught the interest of the researches due to its demonstrated capability to construct solid geometry
from CAD-like parameters, calculate parametric sensitivities, and handle geometric constraints efficiently. In
addition, this framework includes APIs to flow solvers like SU2 and meshing packages, allowing efficient field
data communication among the geometry builder, meshing software, and SU2 solver to calculate parametric
sensitivities.
Mesh Generation
I. Surface Meshing
AFLR4
I. Volume Meshing
AFLR3
3D CFD Analysis
SU2
All ESP Publications are available at this site.
https://acdl.mit.edu/ESP/Publications/?C=D;O=A
Much of the Objectives established -
https://acdl.mit.edu/ESP/Publications/AIA
Apaper2012-0683.pdf
Research Paper topics which research deeply into specific kind of sketching tools
and design methods
● Conservative Fitting for Multi-Disciplinary Analysis
● Design Sensitivity Calculations Directly on CAD-based Geometry
● Generation of Parametric Aircraft Models from a Cloud of Points
● The Creation of a Static BRep Model Given a Cloud of Points
● Using Design-Parameter Sensitivities in Adjoint-Based Design Environments
● Flends: Generalized Fillets via B-splines
● Towards Fully Regular Quad Mesh Generation
● Extension of local cavity operators to 3d + t spacetime mesh adaptation
● Hybrid Shell Model for Aeroelastic Modeling
● Shape Continuum Sensitivity Analysis using ASTROS and CAPS
● Boundary Representation Tolerance Impacts on Mesh Generation and Adaptation
● Exploring Tie Constraints for Structural Analysis Problems
● Parallelization Strategies for Efficiently Computing CAD-based Sensitivities for Design
Optimization
● A Parametric G1-continuous Rounded Wing Tip Treatment for Preliminary Aircraft Design
● On Analysis Driven Shape Design Using B-Splines
Geometric Sketch Constraint Solving with User Feedback
- better than AutoCAD like systems
Using Design-Parameter Sensitivities in
Adjoint-Based Design Environments
All ESP Publications are available at this site
