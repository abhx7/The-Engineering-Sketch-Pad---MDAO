#

# Import pyCAPS module
import pyCAPS

#import os
#filename = os.path.join("..", "ESP","wing.csm")

# Load geometry [.csm] file
filename = "wing_farfield.csm"
print ("\n==> Loading geometry from file \""+filename+"\"...")
capsProblem = pyCAPS.Problem(problemName = "wing_mesh",
                             capsFile = filename,
                             outLevel = 0)

# Alias the geometry
#wing = capsProblem.geometry

# Create AFLR4 AIM
aflr4 = capsProblem.analysis.create(aim = "aflr4AIM",
                                    name = "aflr4")

# Farfield growth factor
aflr4.input.ff_cdfr = 1.4

# Scaling factor to compute AFLR4 'ref_len' parameter via
# ref_len = capsMeshLength * Mesh_Length_Factor
aflr4.input.Mesh_Length_Factor = 5

# Relative scale of maximum spacing bound relative to ref_len
# max_spacing = max_scale * ref_len
aflr4.input.max_scale = 0.1

# Relative scale of minimum spacing bound relative to ref_len
# min_spacing = min_scale * ref_len
aflr4.input.min_scale = 0.01

# Absolute scale of minimum spacing bound for proximity
# abs_min_spacing = abs_min_scale * ref_len
aflr4.input.abs_min_scale = 0.001

# Edge mesh spacing can be scaled on surfaces based on
# discontinuity level between adjacent surfaces on both sides of the edge.
# The level of discontinuity potentially reducing the edge spacing.
# The edgeWeight scale factor weight is used as an interpolation weight
# between the unmodified spacing and the modified spacing.
aflr4.input.Mesh_Sizing = {"leftWing": {"edgeWeight":1.0},
			   "riteWing": {"scaleFactor":2.0},
                           "leftWing": {"scaleFactor":0.5},
                           "Farfield": {"bcType":"Farfield"}}

# Dump SU2 files for visualization
#aflr4.input.Proj_Name   = "Wing_SurfaceMesh"
#aflr4.input.Mesh_Format = "AFLR3"

# Run AIM
aflr4.runAnalysis()

# View the surface tessellation
aflr4.geometry.view()


# Create AFLR3 AIM to generate the volume mesh
aflr3 = capsProblem.analysis.create(aim  = "aflr3AIM",
                                    name = "aflr3")

# Link the aflr4 Surface_Mesh as input to aflr3
aflr3.input["Surface_Mesh"].link(aflr4.output["Surface_Mesh"])

# Specify boundary layer maximum layers.
# Initial spacing and minimum thickness are scaled by capsMeshLength
aflr3.input.BL_Max_Layers      = 10
aflr3.input.BL_Initial_Spacing = 0.01
aflr3.input.BL_Thickness       = 0.1

# Specify prism boundary layer elements
aflr3.input.Mesh_Gen_Input_String = "-blc"

# Set mesh sizing parameters
aflr3.input.Mesh_Sizing = {"leftWing" : {"boundaryLayerSpacing":0.01, "boundaryLayerThickness":0.1},
                           "riteWing" : {"boundaryLayerSpacing":0.01, "boundaryLayerThickness":0.1}}

# Dump SU2 files for visualization
aflr3.input.Proj_Name   = "Wing_VolumeMesh"
aflr3.input.Mesh_Format = "SU2"

# Run AIM
aflr3.runAnalysis()

# View the surface tessellation
aflr3.geometry.view()

