#------------------------------------------------------------------------------#
# Import pyCAPS module
import pyCAPS

# Import os
import os

#------------------------------------------------------------------------------#

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

# Enable only the wing and nacelle
transport.cfgpmtr.COMP.wing        = 1
transport.cfgpmtr.COMP.fuse        = 0
transport.cfgpmtr.COMP.htail       = 0
transport.cfgpmtr.COMP.vtail       = 0
transport.cfgpmtr.COMP.nacelle     = 0
transport.cfgpmtr.COMP.pylon       = 0
transport.cfgpmtr.COMP.payload     = 0
transport.cfgpmtr.COMP.controls    = 0

# Create AFLR4 AIM
aflr4 = capsProblem.analysis.create(aim = "aflr4AIM",
                                    name = "aflr4")

# Dump VTK files for visualization
aflr4.input.Proj_Name = "TransportWing"
aflr4.input.Mesh_Format = "VTK"

# Farfield growth factor
aflr4.input.ff_cdfr = 1.4

# Scaling factor to compute AFLR4 'ref_len' parameter via
# ref_len = capsMeshLength * Mesh_Length_Factor
aflr4.input.Mesh_Length_Factor = 5

# Edge mesh spacing discontinuity scaled interpolant and farfield BC
aflr4.input.Mesh_Sizing = {"riteWing": {"edgeWeight":1.0},
                           "leftWing": {"edgeWeight":1.0},
                           "Farfield": {"bcType":"Farfield"}}

# Run AIM
aflr4.runAnalysis()

# View the surface tessellation
aflr4.geometry.view()

#------------------------------------------------------------------------------#

# Create AFLR3 AIM to generate the volume mesh
aflr3 = capsProblem.analysis.create(aim  = "aflr3AIM",
                                    name = "aflr3")

# Link the aflr4 Surface_Mesh as input to aflr3
aflr3.input["Surface_Mesh"].link(aflr4.output["Surface_Mesh"])

# Dump VTK files for visualization
aflr3.input.Proj_Name   = "TransportWing"
aflr3.input.Mesh_Format = "VTK"

# Run AIM
aflr3.runAnalysis()
