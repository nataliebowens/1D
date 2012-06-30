

# Independent parameters controlling operation of simple1d3

from pylab import *
import pdb
import time
import pickle
import simple1d3
reload(simple1d3)


#  Don't Change!!
Nx = 500
xmax = 501
Fliqstart = 0.1
alpha_terr = 0.1
layer = 0.30 #size of layer in nanometers
Tau = 1.20E-6 # in seconds
tNot= -Tau*(log(alpha_terr))

#Choose these!
Ntimes = 30000
diffCofact= 0.1 #in cm^2/s
supersat = 0.04
supersatpfactor = 0.9
alpha_edge = 1.0
Fliqmax = 1.5
#1000* x_0=100(microm)
x_0= 0.1 #in micrometer

diffCo= diffCofact*1E-5
diffperdt=diffCo*((1E4)**2)*((1/x_0)**2)*tNot
print "diffperdt = ",diffperdt 

x = linspace(0, xmax, Nx)
Fliq0 = ones(size(x)) * Fliqstart
Nice0 = zeros(size(x))
supersatp = supersat * supersatpfactor
c = (supersat - supersatp) / xmax ** 2
rainperdt = x ** 2 * c + supersatp
rainperdt_terr = rainperdt * alpha_terr
rainperdt_edge = rainperdt * alpha_edge
            

# Call to simple1d3
[Fliq, Nice] = simple1d3.simple1d3(x, Fliq0, Nice0, Ntimes, diffperdt, rainperdt_terr, rainperdt_edge, Fliqmax)


#new paraa meters
rSizeNice=Nice[499]
mSizeNice=Nice[249]
lSizeNice=Nice[0]
velMod = rSizeNice/Ntimes #velocity of simulation in layers per t(0)
velMod =velMod/tNot #velocity of sim in layers per second
growthRate= velMod/ (1E3 *(1/layer))
velExp= growthRate*1E3*(1/layer)
print "This corresponds to a growth rate of ", round(growthRate, 5), " microm/sec. (calc)"

 

# Save it

#savedFN = raw_input("What was changed? /n (example: ssp or diff) /n No spaces. ")
#savedFileName ='d31000_' + savedFN + '.dat'
savedFileName= 'd'+ str(Ntimes)+ 'predata.dat'
print "SavedFileName: ",savedFileName
f = open(savedFileName, 'w')
pickle.dump(Fliq, f)
pickle.dump(Nice, f)
pickle.dump(x, f)
pickle.dump(diffperdt, f)
pickle.dump(diffCofact,f)
pickle.dump(rainperdt_terr, f)
pickle.dump(rainperdt_edge, f)
pickle.dump(Fliqmax, f)
pickle.dump(growthRate,f)
f.close()

# Plot it
figurenumber = 1
figure(figurenumber)
clf()
plot(x, Nice, x, Fliq + Nice)
xlabel('x')
ylab= "Layer thickness (1= " + str(layer) + "nm)"
ylabel(ylab)
stitle = 'Ntimes = '
stitle += str(Ntimes)
stitle += ' 1d model'
title(stitle)

