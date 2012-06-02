

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
Ntimes = 50000
diffperdt = 0.05
supersat = 0.04
supersatpfactor = .8
alpha_terr = .2
alpha_edge = 1.0
Fliqmax = 2

##Ask: "Default OR input parameters?"
inParm= raw_input("Default or input parameters? \n(d or i)")

##Input the parameters. If press enter, then they will be defaulted.
if inParm== 'i':
    nx= raw_input("Nx(int):")
    if nx== '':
        pass
    else:
        Nx= int(nx)
    print Nx
    
    
    ntimes= raw_input("Ntimes(int):")
    if ntimes== '':
        pass
    else:
        Ntimes= int(ntimes)
    print Ntimes
    
    
    raindt= raw_input("Diffusitivity(float):")
    if raindt== '':
        pass
    else:
        diffperdt = float(raindt)
    print diffperdt
    
    
    supasat= raw_input("Supersat(float):")
    if raindt== '':
        pass
    else:
        diffperdt = float(raindt)
    print diffperdt
    
    
    deltasupsat= raw_input("Difference in supersat btw middle & edge(between 0-1):")
    if deltasupsat== '':
        pass
    else:
        deltasupsat = float(supersatpfactor)
    print supersatpfactor
    
    
    alpha_terr0= raw_input("Alpha terrace(btw 0-1): ")
    if alpha_terr0== '':
        pass
    else:
        alpha_terr= float(alpha_terr0)
    print alpha_terr
    
        

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

