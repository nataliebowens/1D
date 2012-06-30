# Independent parameters using simple1d4's data files to graph the perturbations

from pylab import *
import pdb
import time
import pickle
import matplotlib.mlab
import matplotlib.pyplot
import numpy




print "Printing & Saving your graph"

#Don't Change!
Nx = 500
xmax = 501
Fliqstart = 0.1
alpha_terr = 0.1
layer = 0.30 #size of layer in nanometers
Tau = 1.20E-6 # in seconds
tNot= -Tau*(log(alpha_terr))

# f is a file
f = open('d32000_normal.dat', 'r')
Fliq0 = pickle.load(f)
Nice0 = pickle.load(f)
x = pickle.load(f)
diffperdt0= pickle.load(f)
diffCofact0=pickle.load(f)                
rainperdt_terr0 = pickle.load(f)
rainperdt_edge0 = pickle.load(f)
Fliqmax0 = pickle.load (f)
growthRate0= pickle.load(f)
f.close()

gData= "d32000_ssp0.2.dat"
gIndex= gData.find("_")
pert= gData[1+gIndex:]
pert= pert.replace('.dat', '')
gD= pert.find("0") 
pert1=pert[:gD]
pert2=pert[gD:]

print "Pert1 is", pert1
print "Pert2 is", pert2
print "Pert is", pert
gI= gData.find("_")
Ntimes= gData[:gI]
Ntimes= Ntimes.replace('d','')
Ntimes= int(Ntimes)
print "Ntimes equals ", Ntimes 

#Loading in the pertibation
g= open(gData, 'r')
Fliq = pickle.load(g)
Nice = pickle.load(g)
x = pickle.load(g)
diffperdt= pickle.load(g)
diffCofact=pickle.load(g)                
rainperdt_terr = pickle.load(g)
rainperdt_edge = pickle.load(g)
Fliqmax = pickle.load (g)
growthRate= pickle.load(g)
f.close()



# Plot it
figurenumber = 1
fig= figure(figurenumber)
clf()
#subplot(2,1,1)
plot(x, Nice0, x, Fliq0 + Nice0, x, Nice,x, Fliq+Nice)
xlim([0,500])
xlabel('x')
grid()
ylab= "Layer thickness (1= " + str(layer) + "nm)"
ylabel(ylab)
difference= growthRate-growthRate0
lab1= "oGR: "+ str(round(growthRate0,4)) +" \nnGR: "+ str(round(growthRate,4)) +"\ndiff: "+ str(round(difference,4)) 
text(400, Nice0[150], lab1)
if pert1 == "diff":
    yo = 'Diffusivity'
    last= 0.1
    pert2=pert2+ " (E-5 cm^2/s)"
elif pert1 == "ss":
    yo = 'Supersaturation'
    last= 0.04
elif pert1 == "aEdge":
    yo = 'Alpha Edge'
    last= 1.0
elif pert1 == "ssp":
    yo = 'SupersaturationP factor'
    last= 0.9
elif pert1 == "FliqM":
    yo = 'FliqMax'
    last= 1.5
else :
    print "Not working!"
stitle = 'Ntimes =' + str(Ntimes)+ ', '+ yo + ' changed from '+ str(last) +' to ' + str(pert2)
title(stitle)
#saveas(h, pert, 'png' )
#imsave(figure(1),'png')
fig.savefig(pert + '.png')



#subplot(2,1,2)
#plot(x, Nice, x, Fliq + Nice)
#xlabel('x')
#ylabel('Layer thickness')
#stitle = 'Ntimes = 1000 '
#stitle += "string"
#stitle += ' Perturbed 1d model'
#title(stitle)

# Save it
#f = open('d.dat', 'w')
#pickle.dump(Fliq, f)
#pickle.dump(Nice, f)
#pickle.dump(x, f)
#f.close()

print isinteractive()

#Should research netCDF for python
