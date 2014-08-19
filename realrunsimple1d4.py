

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
f = open('d30000predata.dat', 'r')
Fliq0 = pickle.load(f)
Nice0 = pickle.load(f)
x = pickle.load(f)
diffperdt= pickle.load(f)
diffCofact=pickle.load(f)                
rainperdt_terr = pickle.load(f)
rainperdt_edge = pickle.load(f)
Fliqmax = pickle.load (f)
oldgrowthRate= pickle.load(f)
f.close()
Ntimes = 2000
ntimes= raw_input("How many extra steps:")
if ntimes=='':
    print Ntimes
else:
    Ntimes = int(ntimes)
    print Ntimes
#Fliq0 = Fliq0 + 3*exp(-(x-250)**2/(2*100^2))


#Don't Change!!
alpha_terr = 0.1
Nx = 500
xmax = 501
Fliqstart = 0.1
layer = 0.30 #size of layer in nanometers
Tau = 1.20E-6 # in seconds
tNot= -Tau*(log(alpha_terr))

#Changables
supersat = 0.04                
supersatpfactor = 0.9
alpha_edge = 1.0
diffCofact= 0.1 #in 10^-5 cm^2/s
Fliqmax = 1.5

an= raw_input("\n0.normal \n1.supersat \n2.supersatpfactor \n3.alpha_edge \n4.diffCofact \n5.FliqMax\n# of variable you would like to change:")
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
        var= raw_input("Change from "+ str(alpha_edge) +" to:")
        alpha_edge= float(var)
        savedFN = "aEdge"
    elif int(an) ==4:
        print "Experimentally Realistic range: 0.02 to 1 (E-5 cm^2/s)"
        var= raw_input("Change from "+ str(diffCofact) +" to:")
        diffCofact= float(var)
        savedFN = "diff"
    elif int(an) ==5:
        var= raw_input("Change from "+ str(Fliqmax) +" to:")
        Fliqmax= float(var)
        savedFN = "FliqM"
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

#Creating rainperdt
supersatp = supersat * supersatpfactor
c = (supersat - supersatp) / xmax ** 2
rainperdt = x ** 2 * c + supersatp
rainperdt_terr = rainperdt * alpha_terr
rainperdt_edge = rainperdt * alpha_edge

#Making diffperdt
diffCo= diffCofact*1E-5
diffperdt=diffCo*((1E4)**2)*((1/0.1)**2)*tNot


# Call to simple1d3
[Fliq, Nice] = simple1d3.simple1d3(x, Fliq0, Nice0, Ntimes, diffperdt, rainperdt_terr, rainperdt_edge, Fliqmax)

#new paraa meters
rSizeNice=Nice[499]
mSizeNice=Nice[249]
lSizeNice=Nice[0]
velMod = rSizeNice/(Ntimes+30000) #velocity of simulation in layers per t(0) (at the larger side)
velMod =velMod/tNot #velocity of sim in layers per second
growthRate= velMod/ (1E3 *(1/layer))
velExp= growthRate*1E3*(1/layer)
print "\n(  OLD  ,  NEW  ) in microm/sec. (calc)"
print "(" + str(round(oldgrowthRate, 5)) + "," + str(round(growthRate,5)) + ")"


# Save it
# This asks user what he/she would like to save the file as 
       #>> savedFN = raw_input("\n\n\nWhat was changed? \n (example: ssp or diff)\n")
numb= 30000 + Ntimes
savedFileName ='d' + str(numb) + '_' + str(savedFN) + str(var) + '.dat'
print "*****************\n" + savedFileName + "\n*****************"
f = open(savedFileName, 'w')
pickle.dump(Fliq, f)
pickle.dump(Nice, f)
pickle.dump(x, f)
pickle.dump(diffperdt, f)
pickle.dump(diffCofact, f)
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