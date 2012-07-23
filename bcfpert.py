

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

# reloads the data from the pre-run (Fliq0, Nice0, x, diffperdt, diffCofact, rainperdt_(terr and edge), Fliqmax, oldgrowthRate)
print "Reloading input data"
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

#Variables that stay the same.
Nx = 500 #Changed this to half
xmax = 501
Fliqstart = .1

#Askes how long you want to run for
Ntimes = 2000
ntimes= raw_input("How many extra steps:")
if ntimes=='':
    print Ntimes
else:
    Ntimes = int(ntimes)
    print Ntimes
#Fliq0 = Fliq0 + 3*exp(-(x-250)**2/(2*100^2))

tau_terr_sec = 20.0e-6
tau_terr = 40
D_cm2persec = 0.5e-5
t0 = tau_terr_sec/tau_terr # seconds
x0 = 0.025 #microns
diffperdt = D_cm2persec/x0**2*t0*1e8

#stuff that you will be asked to change
Fliqmax = 01.5992
supersatpfactor = 0.949
supersat = 0.04
tau_edge = 05000

showcode = Ntimes


an= raw_input("\n0.normal \n1.Fliqmax \n2.supersatpfactor \n3.supersaturation \n4.Edge Lifetime\n# of variable you would like to change:")
if an.isdigit():
    if int(an)== 1:
        var= raw_input("Change from "+ str(Fliqmax) +" to:")
        Fliqmax= float(var)
        savedFN = "FliqM"
    elif int(an) ==2:
        var= raw_input("Change from "+ str(supersatpfactor) +" to:")
        supersatpfactor= float(var)
        savedFN = "ssp"
    elif int(an) ==3:
        var= raw_input("Change from "+ str(supersat) +" to:")
        supersat= float(var)
        savedFN = "ss"
    elif int(an) ==4:
        #print "Experimentally Realistic range: 0.02 to 1 (E-5 cm^2/s)"
        var= raw_input("Change from "+ str(tEdge) +" to:")
        tau_edge= float(var)
        savedFN = "tEdge"
    elif int(an) ==0:
        print "Normal"
        savedFN = "normal"
        var=''
    else :
        print "Nothing was changed! Label saved file 'erase'\n"
        savedFN = "erase"
        var=''
else:
    print "Nothing was changed! Label saved file 'erase'\n"
    savedFN = "erase"
    var= ''

#creating rainperdt
supersatp = supersat * supersatpfactor
c = (supersat - supersatp) / xmax ** 2
rainperdt = x ** 2 * c + supersatp
      
# Call to bcf code
[Fliq, Nice] = bcf1.bcf1(x, Fliq0, Nice0, Ntimes, rainperdt, diffperdt, tau_terr, tau_edge, Fliqmax, showcode)

# Calculate a growth rate
Vgrowth_layerspersec = (Nice[Nx-1]-Nice0[Nx-1])/(Ntimes)/t0
Vgrowth_micrometerspersec = Vgrowth_layerspersec*.3/1000
print "Vgrowth =", Vgrowth_micrometerspersec, "microns/second"

#new paraa meters
rSizeNice=Nice[499]
mSizeNice=Nice[249]
lSizeNice=Nice[0]
velMod = rSizeNice/(Ntimes+ oldtime0) #velocity of simulation in layers per t(0) (at the larger side)
velMod =velMod/t0 #velocity of sim in layers per second
#growthRate= velMod/ (1E3 *(1/layer))
#velExp= growthRate*1E3*(1/layer)
#print "\n(  OLD  ,  NEW  ) in microm/sec. (calc)"
#print "(" + str(round(oldgrowthRate, 5)) + "," + str(round(growthRate,5)) + ")"


# Save it
# This asks user what he/she would like to save the file as 
       #>> savedFN = raw_input("\n\n\nWhat was changed? \n (example: ssp or diff)\n")
numb= oldtime0 + Ntimes
savedFileName ='d' + str(numb) + '_' + str(savedFN) + str(var) + '.dat'
print "*****************\n" + savedFileName + "\n*****************"
f = open(savedFileName, 'w')
pickle.dump(Fliq, f)
pickle.dump(Nice, f)
pickle.dump(x, f)
pickle.dump(diffperdt, f)
pickle.dump(rainperdt, f)
pickle.dump(Fliqmax, f)
pickle.dump(oldtime,f)
pickle.dump(Vgrowth_micrometerspersec ,f)
f.close()

# Plot it
figurenumber = 1
figure(figurenumber)
clf()
plot(x, Nice, x, Fliq + Nice)
xlabel('x')
ylab= "Layer thickness (1= " + str(0.30) + "nm)"
ylabel(ylab)
stitle = 'Ntimes = '
stitle += str(Ntimes)
stitle += ' 1d model'
title(stitle)