


# Independent parameters controlling operation of simple1d3

from pylab import *
import pdb
import time
import pickle 
import simple1d3

# Setup with intial condition == to final condition of previous run


# Load it
f = open('simple1d3.dat', 'r')
Fliq0= pickle.load(f) 
Nice0= pickle.load(f)
x= pickle.load(f)
diffperdt= pickle.load(f)
rainperdt_terr= pickle.load(f)
rainperdt_edge= pickle.load(f)
Fliqmax= pickle.load(f)
f.close()


# Call to simple1d3
Ntimes=30000;

[Fliq, Nice] = simple1d3.simple1d3(x, Fliq0, Nice0, Ntimes, diffperdt, rainperdt_terr, rainperdt_edge, Fliqmax)

# Save it
f = open('simple1d4.dat', 'w')
pickle.dump(Fliq, f)
pickle.dump(Nice, f)
pickle.dump(x,f)
pickle.dump(diffperdt,f)
pickle.dump(rainperdt_terr,f)
pickle.dump(rainperdt_edge,f)
pickle.dump(Fliqmax,f)
f.close()

# Plot it
figurenumber = 1
figure(figurenumber)
clf()
plot(x, Nice, x, Fliq + Nice)
xlabel('x')
ylabel('Layer thickness')
stitle = 'Ntimes = '
stitle += str(Ntimes)
stitle += ' 1d model'
title(stitle)

