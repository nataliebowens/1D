# Independent parameters using simple1d4's data files to graph the perturbations

from pylab import *
import pdb
import time
import pickle
import matplotlib.mlab
import matplotlib.pyplot
import numpy




print "Printing & Saving your graph"

# f is a file
f = open('predatabcf.dat', 'r')
Fliq0 = pickle.load(f)
Nice0 = pickle.load(f)
x = pickle.load(f)
diffperdt0 = pickle.load(f)
rainperdt0 = pickle.load(f)
Fliqmax0 = pickle.load(f)
oldtime0 = pickle.load(f)
Vgrowth_micrometerspersec0 = pickle.load(f)
f.close()



gData= "d130000_diff01.dat"
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
diffperdt = pickle.load(g)
rainperdt = pickle.load(g)
Fliqmax = pickle.load(g)
oldtime = pickle.load(g)
Vgrowth_micrometerspersec = pickle.load(g)
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
if pert1 == "FliqM":
    yo = 'FliqMax'
    last= 1.5992
    pert2=pert2+ " layers"
elif pert1 == "ssp":
    yo = 'SupersaturationP factor'
    last= 0.949
elif pert1 == "ss":
    yo = 'Supersaturation'
    last= 0.04
elif pert1 == "tEdge":
    yo = 'Edge Lifetime'
    last= 5000
elif pert1 == "normal":
    yo = 'erase'
    last= 0.0
else :
    print "Not working!"
stitle = 'Ntimes =' + str(Ntimes)+ ', '+ yo + ' changed from '+ str(last) +' to ' + str(pert2)
title(stitle)


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
