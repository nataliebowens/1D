

# Independent parameters controlling operation of simple1d3

# This code reloads the pre_data(data at steady state), it 
# has you change something and then it saves the changed data
# file under another name that depends on the changed variable.

from pylab import *
import pdb
import time
import pickle
import simple1d3
reload(simple1d3)

print "Reloading input data"

f = open('pre_simple1d3.dat', 'r')
Fliq0 = pickle.load(f)
Nice0 = pickle.load(f)
x = pickle.load(f)
diffperdt= pickle.load(f)                
rainperdt_terr = pickle.load(f)
rainperdt_edge = pickle.load(f)
Fliqmax = pickle.load (f)
f.close()
Ntimes = 1000
ntimes= raw_input("How many extra steps:")
if ntimes=='':
    print Ntimes
else:
    Ntimes = int(ntimes)
    print Ntimes
#Fliq0 = Fliq0 + 3*exp(-(x-250)**2/(2*100^2))

supersat = 0.04                
supersatpfactor = 0.9
alpha_terr = 0.2
alpha_edge = 1.0
diffperdt=0.05
an= raw_input("\n1.supersat \n2.supersatpfactor \n3.alpha_terr \n4.alpha_edge \n5.diffperdt \n# of variable you would like to change:")
if an.isdigit():
    if int(an)== 1:
        var= raw_input("Change from "+ str(supersat) +" to:")
        supersat= float(var)
        savedFN = "ss"
    elif int(an) ==2:
        var= raw_input("Change from "+ str(supersatpfactor) +" to:")
        supersatpfactor= float(var)
        savedFN = "ssp"
    elif int(an) ==3:
        var= raw_input("Change from "+ str(alpha_terr) +" to:")
        alpha_terr= float(var)
        savedFN = "aTerr"
    elif int(an) ==4:
        var= raw_input("Change from "+ str(alpha_edge) +" to:")
        alpha_edge= float(var)
        savedFN = "aEdge"
    elif int(an) ==5:
        var= raw_input("Change from "+ str(diffperdt) +" to:")
        diffperdt= float(var)
        savedFN = "diff"
    else :
        print "Nothing was changed! Label saved file 'erase'\n"
        savedFN = "erase"
        var=''
else:
    print "Nothing was changed! Label saved file 'erase'\n"
    savedFN = "erase"
    var= ''


supersatp = supersat * supersatpfactor
c = (supersat - supersatp) / xmax ** 2
rainperdt = x ** 2 * c + supersatp
rainperdt_terr = rainperdt * alpha_terr
rainperdt_edge = rainperdt * alpha_edge
    
#else:
#
#    Nx = 500 #Changed this to half
#    xmax = 501
#    Fliqstart = 0.1
#    Ntimes = 30000
#    diffperdt = 0.05
#    supersat = 0.04
#    supersatpfactor = 0.9
#    alpha_terr = 0.2
#    alpha_edge = 1.0
#    Fliqmax = 1.5
#    x = linspace(0, xmax, Nx)
#    Fliq0 = ones(size(x)) * Fliqstart
#    Nice0 = zeros(size(x))
#    supersatp = supersat * supersatpfactor
#    c = (supersat - supersatp) / xmax ** 2
#    rainperdt = x ** 2 * c + supersatp
#    rainperdt_terr = rainperdt * alpha_terr
#    rainperdt_edge = rainperdt * alpha_edge


    ##Ask: "Default OR input parameters?"
#    inParm= raw_input("Default or input parameters? \n(d or i)")
    
    ##Input the parameters. If press enter, then they will be defaulted.
#   if inParm== 'i':
#        nx= raw_input("Nx(int):")
#        if nx== '':
#            pass
#        else:
#            Nx= int(nx)
#        print Nx
#        
#        
#        ntimes= raw_input("Ntimes(int):")
#        if ntimes== '':
#            pass
#        else:
#            Ntimes= int(ntimes)
#        print Ntimes
#        
#        
#        raindt= raw_input("Diffusitivity(float):")
#        if raindt== '':
#            pass
#        else:
#            diffperdt = float(raindt)
#        print diffperdt
#        
#        
#        supasat= raw_input("Supersat(float):")
#        if raindt== '':
#            pass
#        else:
#            diffperdt = float(raindt)
#        print diffperdt
#        
#        
#        deltasupsat= raw_input("Difference in supersat btw middle & edge(between 0-1):")
#        if deltasupsat== '':
#            pass
#        else:
#            deltasupsat = float(supersatpfactor)
#        print supersatpfactor
#        
#        
#        alpha_terr0= raw_input("Alpha terrace(btw 0-1): ")
#        if alpha_terr0== '':
#            pass
#        else:
#            alpha_terr= float(alpha_terr0)
#        print alpha_terr
#        
#            


# Call to simple1d3
[Fliq, Nice] = simple1d3.simple1d3(x, Fliq0, Nice0, Ntimes, diffperdt, rainperdt_terr, rainperdt_edge, Fliqmax)

# Save it
# This asks user what he/she would like to save the file as 
       #>> savedFN = raw_input("\n\n\nWhat was changed? \n (example: ssp or diff)\n")

savedFileName ='d3' + str(Ntimes) + '_' + str(savedFN) + str(var) + '.dat'
print savedFileName
f = open(savedFileName, 'w')
pickle.dump(Fliq, f)
pickle.dump(Nice, f)
pickle.dump(x, f)
pickle.dump(diffperdt, f)
pickle.dump(rainperdt_terr, f)
pickle.dump(rainperdt_edge, f)
pickle.dump(Fliqmax, f)
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

