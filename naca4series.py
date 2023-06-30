# Equations used from Google/Stanford Paper
#---------------------------------------------------------------------------------------------------------------#
# Nomenclature of NACA Airfoils (4 series)
# 
# for example, let us consider naca2310
#   Digit     Parameters 
#   2     -   maximum camber (in hundredths of chord) 
#   3     -   location of maximum camber (in tenths of a chord)
#   10    -   maximum thickness (in hundredths of chord)
#
#---------------------------------------------------------------------------------------------------------------#
# Variables used in defining the equations of camber line and forward and aft thickness proflies of the airfoil  (measured from the location of maximum thickness)
#  
#   Variable    Description
#   m           maximum camber (scaled to one tenth of original value) 
#   xm          location of maximum camber
#   t			maximum thickness
#   alpha       angle of attack (scaled to one tenth of original value) 
#--------------------------------------------------------------------------------------------------------------

import numpy as np
import math
import matplotlib.pyplot as plt
#import matplotlib

#naca2310-65  
# inside (), conversion from representation in nomenclature to original value
chord = 1 #unit chord length
m =  (2/100 * chord)
xm = (30/100 * chord)
t = (10/100 * chord)
         
alpha = 0
precision=0.001
#--------------------------------------------------------------------------------------------------------------
# Mean camber line equation
# 
# for x < xm
#   zc= (2*xm - x)*m*x/(xm^2) 
# for x > xm
#   zc= (x + 1 - 2*xm)*(1-x)*m/(1-xm)^2 
#--------------------------------------------------------------------------------
#(1+1/precison) number of coordinates of camber line generated

yc=[]
for x in np.arange(0,chord+chord*precision,chord*precision):
	if x < xm:
		yc.append(((2*xm - x)*m*x)/math.pow(xm,2)) 
	else:
		yc.append((x + 1 - 2*xm)*(1-x)*m/math.pow((1-xm),2))

#list of inclination angle along camber line
theta=[]
for x in np.arange(0,chord+chord*precision,precision):
    if x < xm:
        theta.append(math.atan((2*xm - 2*x)*m/math.pow(xm,2)))
    else:
	    theta.append(math.atan((2*xm - 2*x)*m/math.pow(1-xm,2)))


#--------------------------------------------------------------------------------------------------------------
# Thickness profile
#   yt(x) = t/0.2 * ( 0.2969*sqrt(x) - 0.1260*x - 0.3516*x^2 + 0.2843*x^3 - 0.1036*x^4 ) ) 
#-------------------------------------------------------------------------------------------------------------

#airfoil coordinates and thickness profile
thickness=[]
coordinates=[]
for x in np.arange(chord,0,-chord*precision):
#upper half
	coordinates.append([x - abs(math.sin(theta[int(x/precision)]) * (t/0.2)*(0.2969*math.sqrt(x) - 0.1260*x - 0.3516*math.pow(x,2) + 0.2843*math.pow(x,3) - 0.1036*math.pow(x,4))), yc[int(x*precision)] + abs(math.cos(theta[int(x/precision)])*(t/0.2)*(0.2969*math.sqrt(x) - 0.1260*x - 0.3516*math.pow(x,2) + 0.2843*math.pow(x,3) - 0.1036*math.pow(x,4)))])
for x in np.arange(0,chord+chord*precision,chord*precision):
#lower half	
	coordinates.append([x + abs(math.sin(theta[int(x/precision)]) * (t/0.2)*(0.2969*math.sqrt(x) - 0.1260*x - 0.3516*math.pow(x,2) + 0.2843*math.pow(x,3) - 0.1036*math.pow(x,4))), yc[int(x*precision)] - abs(math.cos(theta[int(x/precision)])*(t/0.2)*(0.2969*math.sqrt(x) - 0.1260*x - 0.3516*math.pow(x,2) + 0.2843*math.pow(x,3) - 0.1036*math.pow(x,4)))])
	thickness.append(abs((t/0.2)*(0.2969*math.sqrt(x) - 0.1260*x - 0.3516*math.pow(x,2) + 0.2843*math.pow(x,3) - 0.1036*math.pow(x,4))))
#print(coordinates)

#plot of camber line and airfoil profile for zero camber
plt.figure(1)
plt.plot(np.arange(0,chord+chord*precision,chord*precision),yc,np.arange(0,chord+chord*precision,chord*precision),thickness)
plt.legend(["Camber line","Thickness profile if zero camber"])

#plot of airfoil section
plt.figure(2)
x1,y1=[],[]
for i in coordinates:
	x1.append(i[0])
	y1.append(i[1])
plt.plot(x1,y1)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Airfoil")
plt.show()

	
points = open("naca2310.txt","w");  #convert it so u can customize filename		
points.write("\t\t\n") #write details of airfoil instead of blank space
for xy in coordinates[:200]:
	points.write(str(xy[0]))
	points.write("\t\t")
	points.write(str(xy[1]))
	points.write("\n")
points.close()