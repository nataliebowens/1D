# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 12:33:26 2012

@author: Natalia
"""
from pylab import *

xmax=501
supersat0= 0.04
supersatpfactor0=0.9
supersatp0 = supersat0 * supersatpfactor0
c = (supersat0 - supersatp0) / xmax ** 2
rainperdt0 = x ** 2 * c + supersatp0

supersat= 0.01
supersatpfactor=0.9
supersatp = supersat * supersatpfactor
c = (supersat - supersatp) / xmax ** 2
rainperdt = x ** 2 * c + supersatp



p0=polyfit(x, Nice0, 2)
Nice0fit= p0[2] + x* p0[1] + x**2 *p0[0]
p=polyfit(x, Nice, 2)
Nicefit= p[2] + x* p[1] + x**2 *p[0]
figure(1)
clf()
plot(x,Nice0fit, x, Nice0, x,Nicefit, x, Nice)

Nice0p= p0[1] + 2*x* p0[0]
Nicep= p[1] + 2*x* p[0]
figure(2)
clf()
plot(x, Nice0p, x, Nicep)
quad0=polyfit(Nice0p, 1/rainperdt0,2)

quad=polyfit(Nicep, 1/rainperdt,2)

print "This is quad0", quad0
print "This is quad", quad

print "quad0[2]/quad0[1] (alphaNOT/betaNOT) =", quad0[2]/quad0[1]
print "quad[2]/quad[1]=", quad[2]/quad[1]

print "testinghow linear Q is"

Q0=rainperdt0*(quad0[2]+quad0[1]*Nice0p)
Q=rainperdt*(quad[2]+quad[1]*Nicep)

figure(4)
clf()
plot(x, Q0, x, Q)


figure(3)
clf()
plot(Nice0p, 1/rainperdt0, Nicep, 1/rainperdt)

print isinteractive()