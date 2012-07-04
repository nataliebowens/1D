def simple1d4(x=None, Fliq=None, Nice=None, Ntimes=None, diffperdt=None, Tau=None, rainperdt=None, Fliqmax=None):
    "This is a 1-d model"
    
    print "This is a 1-d model"
    # step dynamics, 1-dimensional, fixed boundary conditions corresponding to
    # prismatic-prismatic edges
    import numpy
    import time
    import matplotlib.mlab
    import matplotlib.pyplot
    import pdb
    
    # Other initializing
    
    Fliqnext = numpy.zeros(numpy.size(x))
    tDiff=0.0
    tLookE=0.0
    tFind=0.0
    tVap=0.0
    tLookN=0.0
    tUpdate=0.0
 

        #This will ask the user if you want to have the program
        #plot the variables as it is calculating and how often....
    ans = raw_input("Real-time plotting? \n (y?) :")

    if ans == 'y':
        timesteps= raw_input("How many time steps? \n (integer) :") 
        ts= int(timesteps) # this is used in the ploting function
            
    else:
        pass #Should just pass to the next code

   
    for itime in range(1,Ntimes):
        
        # Diffusion of liquid to adjacent cells
        end = Fliqnext.size-1
        Fliqnext[1:end] = Fliq[1:end] * (1 - diffperdt) + (Fliq[0:end-1] + Fliq[2:end+1]) * diffperdt / 2
        Fliqnext[0] = Fliq[0] * (1 - diffperdt / 2) + Fliq[1] * diffperdt / 2
        Fliqnext[end] = Fliq[end] * (1 - diffperdt / 2) + Fliq[end-1] * diffperdt / 2
        
        # Look for edges
        Eice = numpy.zeros(numpy.size(Nice))
        dNice = numpy.diff(Nice)
        Iedge_up = matplotlib.mlab.find(dNice > 0)
        Eice[Iedge_up] = 1; #print Eice
        
        Iedge_dn = matplotlib.mlab.find(dNice < 0) + 1
        Eice[Iedge_dn] = -1; #print Eice
        
        
        # Find locations of edges and terraces
        Iterr = matplotlib.mlab.find(Eice == 0)
        Iedge = matplotlib.mlab.find(Eice != 0)
        
        # Net deposition from vapor
        Fliqnext[Iterr] = Fliqnext[Iterr]*(1-1/Tau) + rainperdt[Iterr]
        Fliqnext[Iedge] = Fliqnext[Iedge] + rainperdt[Iedge] 
        
        # Look for layer nucleation sites
        tLookN= tLookN - time.time() 
        Ilrnc = Fliqnext > Fliqmax
        Fliqnext[Ilrnc] = Fliqnext[Ilrnc] - Fliqmax
        Nice[Ilrnc] = Nice[Ilrnc] + Fliqmax
        tLookN= tLookN + time.time() 
        
        # Update Fliq
        tUpdate= tUpdate - time.time() 
        Fliq = Fliqnext 
        tUpdate= tUpdate + time.time() 
        
        if ans == 'y':
            
            # Graphics
            if numpy.mod(itime,ts)==0:
                matplotlib.pyplot.clf() 
                matplotlib.pyplot.plot(x, Nice, x, Fliq + Nice)                  
                print itime 
                matplotlib.pyplot.pause(0.001) #What is this for?
            
        else:
            pass #Should just pass to the next code
       
    end
    
    # This prints out the time that it takes each step to complete in the loop. 
   # print "time for... \n\btDiff=", round(tDiff, 3), "\btLookE=", round(tLookE, 3), "\btLookN=", round(tLookN, 3), "\btFind=", round(tFind,3), "\btVap=", round(tVap,3), "\bUpdate=", round(tUpdate,3)
    
    
    # Record stuff and get out
    return Fliq, Nice


