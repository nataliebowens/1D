# Independent parameters using simple1d4's data files to graph the perturbations

from pylab import *
import pdb
import time
import pickle


print "Printing your graph"
# f is a file
f = open('pre_simple1d3.dat', 'r')
Fliq = pickle.load(f)
Nice = pickle.load(f)
x = pickle.load(f)
f.close()
print "loaded, now to dump!"

# Plot it
figurenumber = 1
figure(figurenumber)
clf()
plot(x, Nice, x, Fliq + Nice)
xlabel('x')
ylabel('Layer thickness')
stitle = 'Ntimes = '
stitle += "string"
stitle += ' 1d model'
title(stitle)


# Save it
f = open('d.dat', 'w')
pickle.dump(Fliq, f)
pickle.dump(Nice, f)
pickle.dump(x, f)
f.close()


