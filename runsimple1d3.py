

# Independent parameters controlling operation of simple1d3

from pylab import *
import pdb
import time
import pickle
import simple1d3
reload (simple1d3)

Nx = 500 #Changed this to half
xmax = 501
Fliqstart = .1
Ntimes = 30000
diffperdt = 0.05
supersat = 0.04
supersatpfactor = .9
alpha_terr = .2
alpha_edge = 1.0
Fliqmax = 2

# Dependent parameters needed for simple1d3
x = linspace(0, xmax, Nx)
Fliq0 = ones(size(x)) * Fliqstart
Nice0 = zeros(size(x))
supersatp = supersat * supersatpfactor
c = (supersat - supersatp) / xmax ** 2
rainperdt = x**2 * c + supersatp
rainperdt_terr = rainperdt * alpha_terr
rainperdt_edge = rainperdt * alpha_edge

# Call to simple1d3
[Fliq, Nice] = simple1d3.simple1d3(x, Fliq0, Nice0, Ntimes, diffperdt, rainperdt_terr, rainperdt_edge, Fliqmax)

# Save it
f = open('simple1d3.dat', 'w')
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

