def simple1d3(x=None, Fliq0=None, Nice0=None, Ntimes=None, diffperdt=None, rainperdt_terr=None, rainperdt_edge=None, Fliqmax=None):
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
    
    Fliq = Fliq0
    Nice = Nice0
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
        tDiff= tDiff - time.time()  
        end = Fliqnext.size-1
        Fliqnext[1:end] = Fliq[1:end] * (1 - diffperdt) + (Fliq[0:end-1] + Fliq[2:end+1]) * diffperdt / 2
        Fliqnext[0] = Fliq[0] * (1 - diffperdt / 2) + Fliq[1] * diffperdt / 2
        Fliqnext[end] = Fliq[end] * (1 - diffperdt / 2) + Fliq[end-1] * diffperdt / 2
        tDiff= tDiff + time.time()
        
        # Look for edges
        tLookE= tLookE - time.time()
        Eice = numpy.zeros(numpy.size(Nice))
        dNice = numpy.diff(Nice)
        Iedge_up = matplotlib.mlab.find(dNice > 0)
        Eice[Iedge_up] = 1; #print Eice
        
        Iedge_dn = matplotlib.mlab.find(dNice < 0) + 1
        Eice[Iedge_dn] = -1; #print Eice
        tLookE= tLookE + time.time()
        
        
        # Find locations of edges and terraces
        tFind= tFind - time.time()
        Iterr = matplotlib.mlab.find(Eice == 0)
        Iedge = matplotlib.mlab.find(Eice != 0)
        tFind= tFind + time.time()
        
        # Net deposition from vapor
        tVap= tVap - time.time()
        Fliqnext[Iterr] = Fliqnext[Iterr] + rainperdt_terr[Iterr]
        Fliqnext[Iedge] = Fliqnext[Iedge] + rainperdt_edge[Iedge]
        tVap= tVap + time.time()
        
        # Look for layer nucleation sites
        tLookN= tLookN - time.time() 
        Ilrnc = Fliqnext > Fliqmax
        Fliqnext[Ilrnc] = Fliqnext[Ilrnc] - 1
        Nice[Ilrnc] = Nice[Ilrnc] + 1
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
<<<<<<< HEAD
                matplotlib.pyplot.grid()
                matplotlib.pyplot.xlim([0,100])
                matplotlib.pyplot.pause(0.001)##>> 100 below equals answer
=======
                matplotlib.pyplot.pause(0.001) #What is this for?
>>>>>>> FETCH_HEAD
            
        else:
            pass #Should just pass to the next code
       
    end
    
    # This prints out the time that it takes each step to complete in the loop. 
   # print "time for... \n\btDiff=", round(tDiff, 3), "\btLookE=", round(tLookE, 3), "\btLookN=", round(tLookN, 3), "\btFind=", round(tFind,3), "\btVap=", round(tVap,3), "\bUpdate=", round(tUpdate,3)
    
    
    # Record stuff and get out
    return Fliq, Nice


