# Independent parameters using simple1d4's data files to graph the perturbations

from pylab import *
import pdb
import time
import pickle
import matplotlib.mlab
import matplotlib.pyplot
import numpy




print "Printing your graph"
# f is a file
f = open('d31000_normal.dat', 'r')
Fliq0 = pickle.load(f)
Nice0 = pickle.load(f)
x = pickle.load(f)
f.close()
print "The normal case is loaded"

gData= "d31000_ssp0.98.dat"
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
g= open(gData, 'r')
Fliq = pickle.load(g)
Nice = pickle.load(g)
x = pickle.load(g)
f.close()



# Plot it
figurenumber = 1
fig= figure(figurenumber)
clf()
#subplot(2,1,1)
plot(x, Nice0, x, Fliq0 + Nice0, x, Nice,x, Fliq+Nice)
xlabel('x')
ylabel('Layer thickness')
if pert1 == "diff":
    yo = 'Diffusivity'
    last= 0.05
elif pert1 == "ss":
    yo = 'Supersaturation'
    last= 0.04
elif pert1 == "aTerr":
    yo = 'Alpha Terrace '
    last= 0.2
elif pert1 == "aEdge":
    yo = 'Alpha Edge'
    last=1.0
elif pert1 == "ssp":
    yo = 'SupersaturationP factor'
    last= 0.9
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
