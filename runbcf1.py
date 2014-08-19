

# Independent parameters controlling operation of simple1d3

from pylab import *
import pickle
import bcf1
reload(bcf1)


#ans = raw_input("Reloading input data? \n (y or n) :")


<<<<<<< HEAD
Nx = 501 #Changed this to half
x0 = .025 #microns
xmax = Nx*x0
x_microns = arange(0,xmax,x0)
showcode = 200
xmax = max(x_microns)
Fliqstart = .1
Ntimes = 10000


tau_terr_sec = 10.0e-6
tau_terr = 40
D_cm2persec = .1e-5
t0 = tau_terr_sec/tau_terr # seconds
=======
Nx = 500 #Changed this to half
showcode = 2000
xmax = 501
Fliqstart = .1
Ntimes = 20000


tau_terr_sec = 20.0e-6
tau_terr = 40
D_cm2persec = 0.5e-5
t0 = tau_terr_sec/tau_terr # seconds
x0 = .025 #microns
>>>>>>> FETCH_HEAD
diffperdt = D_cm2persec/x0**2*t0*1e8

print "Conventional units"
print "D =", D_cm2persec, "cm^2/s"
print "tau =", tau_terr_sec*1e6, "microseconds"
print "Model width =", Nx*2*x0, "micrometers"

print "Internal units"
print "D =", diffperdt, "x0^2/t0"
print "tau =", tau_terr, "t0"
print "Model width =", Nx*2, "x0"

supersat = 0.04
<<<<<<< HEAD
supersatpfactor = .99
tau_edge = 10*tau_terr
Fliqmax = 1.5
Fliq0 = ones(size(x_microns)) * Fliqstart
Fliq0[200:300]+=.2
Nice0 = zeros(size(x_microns))
supersatp = supersat * supersatpfactor
c = (supersat - supersatp) / xmax ** 2
rainperdt = x_microns ** 2 * c + supersatp
      
# Call to bcf code
[Fliq, Nice] = bcf1.bcf1(x_microns, Fliq0, Nice0, Ntimes, rainperdt, diffperdt, tau_terr, tau_edge, Fliqmax, showcode)
=======
supersatpfactor = 0.949
tau_edge = 5000
Fliqmax = 1.5992
x = linspace(0, xmax, Nx)
Fliq0 = ones(size(x)) * Fliqstart
Nice0 = zeros(size(x))
supersatp = supersat * supersatpfactor
c = (supersat - supersatp) / xmax ** 2
rainperdt = x ** 2 * c + supersatp
      
      
# Call to bcf code
[Fliq, Nice] = bcf1.bcf1(x, Fliq0, Nice0, Ntimes, rainperdt, diffperdt, tau_terr, tau_edge, Fliqmax, showcode)

>>>>>>> FETCH_HEAD

# Calculate a growth rate
Vgrowth_layerspersec = (Nice[Nx-1]-Nice0[Nx-1])/Ntimes/t0
Vgrowth_micrometerspersec = Vgrowth_layerspersec*.3/1000
print "Vgrowth =", Vgrowth_micrometerspersec, "microns/second"

<<<<<<< HEAD
# Save it
f = open('simple1d3_normal.dat', 'w')
pickle.dump(Fliq, f)
pickle.dump(Nice, f)
pickle.dump(x_microns, f)
pickle.dump(diffperdt, f)
pickle.dump(rainperdt, f)
pickle.dump(Fliqmax, f)
f.close()
'''
=======

oldtime= Ntimes
# Save it
f = open('predatabcf.dat', 'w')
pickle.dump(Fliq, f)
pickle.dump(Nice, f)
pickle.dump(x, f)
pickle.dump(diffperdt, f)
pickle.dump(rainperdt, f)
pickle.dump(Fliqmax, f)
pickle.dump(oldtime,f)
pickle.dump(Vgrowth_micrometerspersec ,f)
f.close()


>>>>>>> FETCH_HEAD
# Plot it
figurenumber = 1
figure(figurenumber)
clf()
<<<<<<< HEAD
subplot(2,1,1)
plot(x_microns, Nice, x_microns, Fliq + Nice)
=======
plot(x, Nice, x, Fliq + Nice)
>>>>>>> FETCH_HEAD
xlabel('x')
ylabel('Layer thickness')
stitle = 'Ntimes = '
stitle += str(Ntimes)
stitle += ' 1d model'
title(stitle)
grid()
<<<<<<< HEAD
subplot(2,1,2)
plot(x_microns, rainperdt)
xlabel('x')
ylabel('supersat. (arb. units')
show()
'''
=======
>>>>>>> FETCH_HEAD

