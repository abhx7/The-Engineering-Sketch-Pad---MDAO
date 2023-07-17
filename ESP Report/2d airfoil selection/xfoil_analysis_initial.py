#analysis done to find best possible camber & thickness and angle of attack

# Import os
import os

# Import matplotlib
from matplotlib import pyplot as plt

# Import pyCAPS module
import pyCAPS

# Load geometry [.csm] file
filename = "naca.csm"
print ("\n==> Loading geometry from file \""+filename+"\"...")
capsProblem = pyCAPS.Problem(problemName = "design_naca",
                             capsFile = filename,
                             outLevel = 1)

# Create xfoil aim
print ("\n==> Creating xfoilAIM")
xfoil = capsProblem.analysis.create(aim = "xfoilAIM",
                                    name = "xfoil",
                                    autoExec = True)
# Run analysis (optional)
#xfoil.runAnalysis()

naca=capsProblem.geometry
# Build and view the geometry with ESP
print ('\n==> Bulding and viewing geometry...')
naca.view()


print ("\n==> Setting analysis values")
# Set Mach and Reynolds number
xfoil.input.Mach = 0.5
xfoil.input.Re   = 1.0e6

# Set list of Alpha
xfoil.input.Alpha = [-4.0, -2.0, 0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0]

#-------------------------------------------------------------------------------------------------
#max camber
#------------------------------------------------------------------------------------------------

# List of cambers to analyze
Cambers = [0.00, 0.10, 0.15, 0.20,0.25]

# Crete the figure with 2 axes and sent the axis labels
fig, ax = plt.subplots(1, 2, figsize=(12,6))
ax[0].set_xlabel("Alpha")
ax[0].set_ylabel("Cl")
ax[1].set_xlabel("Cl")
ax[1].set_ylabel("Cd")

r=0#initialisation varaible for ratio of Cl and Cd
for camber in Cambers:
    # Modify the camber
    naca.despmtr.mc = camber
  
    # Retrieve and plot Alpha, Cl and Cd
    print ("\n==> Retrieve analysis results. camber = ", naca.despmtr.mc)
    Alpha = xfoil.output.Alpha
    Cl = xfoil.output.CL
    Cd = xfoil.output.CD
    
    #find angle of attack and camber for best lift/drag ratio
    for i in range(len(Alpha)):
    	if Cl[i]/Cd[i]>r:
    		mc=camber
    		aoa=Alpha[i]		
    		#naca.outpmtr["aoa"].value=aoa    	
    		r=Cl[i]/Cd[i]
    ax[0].plot(Alpha, Cl, '-o', label = "Camber = " + str(camber))
    ax[1].plot(Cl, Cd, '-o', label = "Camber = " + str(camber))

#saving egads file with best camber
naca.despmtr.mc=mc 
print()
print()
print("Highest Cl/Cd ratio achieved at camber of ", mc, "at angle of attack", aoa)
print()
print()
naca.save("naca_1a.egads")

# Show the legend on the 2nd axes
ax[1].legend()

plt.title("Airfoil Analysis 1a")

# Show the plot
print ("\n==> Plotting analysis results (close plot window to )")
plt.savefig('analysis1a')
plt.show()

# Build and view the geometry with ESP
print ('\n==> Bulding and viewing geometry...')
naca.view()

#-------------------------------------------------------------------------------------------------
#max thickness
#------------------------------------------------------------------------------------------------

# List of thickness to analyze
Thickness = [0.10, 0.20, 0.30]

# Crete the figure with 2 axes and sent the axis labels
fig, ax = plt.subplots(1, 2, figsize=(12,6))
ax[0].set_xlabel("Alpha")
ax[0].set_ylabel("Cl")
ax[1].set_xlabel("Cl")
ax[1].set_ylabel("Cd")

r=0#initialisation varaible for ratio of Cl and Cd
for thick in Thickness:
    # Modify the thickness
    naca.despmtr.t = thick
  
    # Retrieve and plot Alpha, Cl and Cd
    print ("\n==> Retrieve analysis results. camber = ", naca.despmtr.t)
    Alpha = xfoil.output.Alpha
    Cl = xfoil.output.CL
    Cd = xfoil.output.CD
    
    #find angle of attack and thickness for best lift/drag ratio
    for i in range(len(Alpha)):
    	if Cl[i]/Cd[i]>r:
    		mt=thick
    		aoa=Alpha[i]		
    		#naca.outpmtr["aoa"].value=aoa    	
    		r=Cl[i]/Cd[i]
    ax[0].plot(Alpha, Cl, '-o', label = "Thickness = " + str(thick))
    ax[1].plot(Cl, Cd, '-o', label = "Thickness = " + str(thick))

#saving egads file with best camber
naca.despmtr.t=mt 
print()
print()
print("Highest Cl/Cd ratio achieved at thickness of ", mt, "at angle of attack", aoa)
print()
print()
naca.save("naca_1b.egads")

# Show the legend on the 2nd axes
ax[1].legend()

plt.title("Airfoil Analysis 1b")

# Show the plot
print ("\n==> Plotting analysis results (close plot window to )")
plt.savefig('analysis1b')
plt.show()


# Build and view the geometry with ESP
print ('\n==> Bulding and viewing geometry...')
naca.view()

#-------------------------------------------------------------------------------------------------
#location of maximum camber
#------------------------------------------------------------------------------------------------

# List of location of max camber to analyze
Location_cambers = [0.30, 0.40]

# Crete the figure with 2 axes and sent the axis labels
fig, ax = plt.subplots(1, 2, figsize=(12,6))
ax[0].set_xlabel("Alpha")
ax[0].set_ylabel("Cl")
ax[1].set_xlabel("Cl")
ax[1].set_ylabel("Cd")

r=0#initialisation varaible for ratio of Cl and Cd
for loc in Location_cambers:
    # Modify the thickness
    naca.despmtr.lmc = loc
  
    # Retrieve and plot Alpha, Cl and Cd
    print ("\n==> Retrieve analysis results. Location of max camber = ", naca.despmtr.lmc)
    Alpha = xfoil.output.Alpha
    Cl = xfoil.output.CL
    Cd = xfoil.output.CD
    
    #find angle of attack and thickness for best lift/drag ratio
    for i in range(len(Alpha)):
    	if Cl[i]/Cd[i]>r:
    		lmc=loc
    		aoa=Alpha[i]		
    		#naca.outpmtr["aoa"].value=aoa    	
    		r=Cl[i]/Cd[i]
    ax[0].plot(Alpha, Cl, '-o', label = "Location = " + str(loc))
    ax[1].plot(Cl, Cd, '-o', label = "Location = " + str(loc))

#saving egads file with best camber
naca.despmtr.lmc=lmc
print()
print()
print("Highest Cl/Cd ratio achieved with maximum camber at location of ", lmc, "at angle of attack", aoa)
print()
print()
naca.save("naca_camber1c.egads")

# Show the legend on the 2nd axes
ax[1].legend()

plt.title("Airfoil Analysis 1c")

# Show the plot
print ("\n==> Plotting analysis results (close plot window to finish script")
plt.savefig('analysis1c')
plt.show()


# Build and view the geometry with ESP
print ('\n==> Bulding and viewing geometry...')
naca.view()

