# Import pyCAPS module
import pyCAPS

# Import matplotlib
from matplotlib import pyplot as plt

# Load geometry [.csm] file
filename = "naca_wing.csm"
print ("\n==> Loading geometry from file \""+filename+"\"...")
capsProblem = pyCAPS.Problem(problemName = "naca_wing",
                             capsFile = filename,
                             outLevel = 1)
#create geometry object to save outputs
naca_wing=capsProblem.geometry

# Create avl aim
print ("\n==> Create avlAIM")
avl = capsProblem.analysis.create(aim = "avlAIM",
                                  name = "avl")

# view the initial geometry with ESP
print ("\n==> Viewing wing...")
avl.geometry.view()


print ("\n==> Setting standard analysis values")
avl.input.Mach = 0.5
avl.input.Alpha = 2.0
Taper_ratio = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

# Set meshing parameters for each surface
wing = {"groupName" : "Wing",
	"numChord"     : 4,
        "numSpanTotal" : 24}

# Associate the surface parameters 
# with capsGroups defined on the geometry
avl.input.AVL_Surface = {"Wing" : wing} #multiple surfaces can be added in this dicitionary sort of format

#modelling of control surfaces
flap = {"controlGain" : 0.5,
	"deflectionAngle" : 10.0}
avl.input.AVL_Control = {"LeftFlap": flap, "RightFlap": flap}

# Create the figure with 2 axes and sent the axis labels
fig, ax = plt.subplots(1, 2, figsize=(20,10))
ax[0].set_xlabel("Taper Ratio")
ax[0].set_ylabel("Coefficients")
ax[1].set_xlabel("Taper Ratio")
ax[1].set_ylabel("Oswald efficiency")

Cl,Cd,CDi,e,sens=[],[],[],[],[]
trm=0#initialisation varaible 
r=0
for tr in Taper_ratio:
    print ("\n==> Analysis for taper ratio = ", tr)
    naca_wing.despmtr["wing:taper"].value = tr #testing for different analysis values
    
    try:
	    print ("\n==> Retrieve analysis results.")
	    Cl.append(avl.output.CLtot)
	    Cd.append(avl.output.CDtot)
	    CDi.append(avl.output.CDind)
	    e.append(avl.output.e)
	    sens.append(avl.output["CLtot"].deriv("Alpha"))
	  
	    #find angle of attack and camber for best lift/drag ratio
	    if avl.output.e>r:
	    	trm=tr		  	
	    	r=avl.output.e
	
    except:
    	     print("No calculation for this data value")
    	
ax[0].plot(Taper_ratio, Cl, '-o', label = "Cl")
ax[0].plot(Taper_ratio, Cd, '-o', label = "Cd")
ax[0].plot(Taper_ratio, CDi, '-o', label = "CDi")
ax[1].plot(Taper_ratio, e, '--')
	    
#saving egads file with best taper ratio
print()
print()
print("Highest Oswald efficiency achieved at taper ratio", trm)
print()
print()
naca_wing.despmtr["wing:taper"].value = trm
naca_wing.save("naca_wing.egads")

# Show the legend
ax[0].legend()

plt.title("Wing Analysis wrt Taper Ratio")

# Show the plot
print ("\n==> Plotting analysis results (close plot window to )")
plt.savefig('wing_analysis')
plt.show()


# Create the figure with 2 axes and sent the axis labels
fig, ax = plt.subplots(1, 2, figsize=(20,10))
ax[0].set_ylabel("Cl")
ax[0].set_xlabel("Cd")
ax[1].set_ylabel("Cl")
ax[1].set_xlabel("Sensisitvity")

ax[0].plot(Cd, Cl, '--')
ax[1].plot(Cl, sens, '-o',label='wrt Alpha')

plt.savefig('wing_sensitivity')
plt.show()


# Build and view the geometry with ESP
print ('\n==> Bulding and viewing geometry...')
avl.geometry.view()


