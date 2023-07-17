# Import pyCAPS module
import pyCAPS
# Import os module
import os
# Import SU2 python environment
from parallel_computation import parallel_computation as su2Run
#------------------------------------------------------------------------------#
#Importing geometry

# Load CSM file
filename = os.path.join("data","transport.csm")
capsProblem = pyCAPS.Problem(problemName = "design_Transport",
                             capsFile = filename,
                             outLevel = 0)

# Alias the geometry
transport = capsProblem.geometry

# Change to Inviscid CFD view
transport.cfgpmtr.VIEW.Concept     = 0
transport.cfgpmtr.VIEW.CfdInviscid = 1

# Enable just wing
transport.cfgpmtr.COMP.wing        = 1
transport.cfgpmtr.COMP.fuse        = 0
transport.cfgpmtr.COMP.htail       = 0
transport.cfgpmtr.COMP.vtail       = 0
transport.cfgpmtr.COMP.nacelle     = 0
transport.cfgpmtr.COMP.pylon       = 0
transport.cfgpmtr.COMP.payload     = 0
transport.cfgpmtr.COMP.controls    = 0

#------------------------------------------------------------------------------#
#Mesh Generation
#------------------------------------------------------------------------------#

# Create aflr4 AIM
aflr4 = capsProblem.analysis.create(aim  = "aflr4AIM",
                                  name = "aflr4")

# Farfield growth factor
aflr4.input.ff_cdfr = 1.4

# Scaling factor to compute AFLR4 'ref_len' parameter
# ref_len = capsMeshLength * Mesh_Length_Factor
aflr4.input.Mesh_Length_Factor = 0.5

# Edge mesh spacing discontinuity scaled interpolant and farfield meshing BC
aflr4.input.Mesh_Sizing = {"leftWing": {"edgeWeight":1.0},
                           "riteWing": {"edgeWeight":1.0},
                           "Farfield": {"bcType":"Farfield"}}

#------------------------------------------------------------------------------#

# Create AFLR3 AIM to generate the volume mesh
aflr3 = capsProblem.analysis.create(aim  = "aflr3AIM",
                                  name = "aflr3")

# Link the aflr4 Surface_Mesh as input to aflr3
aflr3.input["Surface_Mesh"].link(aflr4.output["Surface_Mesh"])

#------------------------------------------------------------------------------#
#Flow Analysis/Solving
#------------------------------------------------------------------------------#

# Create SU2 AIM
su2 = capsProblem.analysis.create(aim  = "su2AIM",
                                  name = "su2")

# Link the aflr3 Volume_Mesh as input to su2
su2.input["Mesh"].link(aflr3.output["Volume_Mesh"])

# Set project name. Files written to analysisDir will have this name
su2.input.Proj_Name = "inviscidWing"

#Problem definition
su2.input.Math_Problem="Direct"
su2.input.Physical_Problem="Euler"
#restart files if necessary

# free stream definition
su2.input.Alpha = 2.0                    # AoA
su2.input.Mach = 0.5                     # Mach number
su2.input.Equation_Type = "Compressible" # Equation type
su2.input.Freestream_Pressure=101325.0
su2.input.Freestream_Temperature=288.15

#reference value definition
su2.input.Moment_Center=[0.25,0.00,0.00]
#su2.input.Moment_Length= NULL
su2.input.Reference_Area=0
su2.input.Reference_Dimensionalization="FREESTREAM_VEL_EQ_ONE"

#Boundary Condition definition
# Set boundary conditions via capsGroup
inviscidBC = {"bcType" : "Inviscid"}
su2.input.Boundary_Condition = {"Wing"    : inviscidBC,
                                "Farfield": "farfield"}

# Specifcy the boundares used to compute forces
su2.input.Surface_Monitor = ["Wing"]

#Common parameters to definenumerical methods
su2.input.CFL_Number=5.0
su2.input.Num_Iter = 1000                   # Number of iterations
su2.input.Input_String = ["LINEAR_SOLVER= FGMRES",
                          "LINEAR_SOLVER_PREC= LU_SGS",
                          "LINEAR_SOLVER_ERROR= 1E-6",
                          "LINEAR_SOLVER_ITER= 2"]

#slope limiter definition
#su2.input.Input_String = ["",]

#multigrid parameters
su2.input.MultiGrid_Level=2

#FLOW NUMERICAL METHOD DEFINITION 
#su2.input.Input_String = ["",]

#ADJOINT-FLOW NUMERICAL METHOD DEFINITION 
#su2.input.Input_String = ["",]


#Convergence Parameters
su2.input.Input_String = ["CONV_RESIDUAL_MINVAL= -12",
                          "CONV_STARTITER= 25",
                          "CONV_FIELD= RMS_DENSITY",            
                          "CONV_CAUCHY_EPS= 1E-10"]

# Set SU2 Version
su2.input.SU2_Version = "Blackbird"

# Run AIM pre-analysis
su2.preAnalysis()

####### Run SU2 #######################
print ("\n\nRunning SU2......")
currentDirectory = os.getcwd() # Get our current working directory

os.chdir(su2.analysisDir) # Move into test directory

# Run SU2 with specified number of partitions
su2Run(su2.input.Proj_Name + ".cfg", partitions = 1)

os.chdir(currentDirectory) # Move back to top directory
#######################################

# Run AIM post-analysis
su2.postAnalysis()

print ("\n==> Total Forces and Moments")
# Get Lift and Drag coefficients
print ("--> Cl = ", su2.output.CLtot,
           "Cd = ", su2.output.CDtot)

# Get Cmx, Cmy, and Cmz coefficients
print ("--> Cmx = ", su2.output.CMXtot,
           "Cmy = ", su2.output.CMYtot,
           "Cmz = ", su2.output.CMZtot)

# Get Cx, Cy, Cz coefficients
print ("--> Cx = ", su2.output.CXtot,
           "Cy = ", su2.output.CYtot,
           "Cz = ", su2.output.CZtot)
