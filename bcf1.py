def bcf1(x=None, Fliq0=None, Nice0=None, Ntimes=None, rainperdt=None, diffperdt=None, tau_terr=None, tau_edge=None, Fliqmax=None, showflag=None):
    "This is a 1-d model"
    
    print "This is a 1-d model"
    # step dynamics, 1-dimensional, fixed boundary conditions corresponding to
    # prismatic-prismatic edges
    import numpy
    import matplotlib.mlab
    import matplotlib.pyplot
    
    # Other initializing
    #pdb.set_trace()http://piercetransit.org/http://piercetransit.org/
    
    Fliq = Fliq0
    Fliqnext = numpy.zeros(numpy.size(x))
    Nice = numpy.zeros(numpy.size(x))
    #Nice = numpy.zeros_like(Nice0)
    #Nice = Nice0.copy()
    end = Fliqnext.size-1
    Nice[0:end+1] = Nice0[0:end+1]
    deltat = 1

   
    for itime in range(1,Ntimes):
        
        # Diffusion of liquid to adjacent cells  
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
        #Fliqnext[Iterr] = Fliqnext[Iterr]*(1-Fliqnext[Iterr]/tau_terr)+rainperdt[Iterr]
        #Fliqnext[Iedge] = Fliqnext[Iedge]*(1-Fliqnext[Iedge]/tau_edge)+rainperdt[Iedge]
        Fliqnext[Iterr] = Fliqnext[Iterr] + (rainperdt[Iterr] - Fliqnext[Iterr]/tau_terr)*deltat
        Fliqnext[Iedge] = Fliqnext[Iedge] + (rainperdt[Iedge] - Fliqnext[Iedge]/tau_edge)*deltat
        
        # Look for layer nucleation sites
        Ilrnc = Fliq > Fliqmax
        Fliqnext[Ilrnc] = Fliqnext[Ilrnc] - 1
        Nice[Ilrnc] = Nice[Ilrnc] + 1
        
        # Update Fliq
        Fliq = Fliqnext 
        
        if showflag > 0:
            
            # Graphics
            if numpy.mod(itime,showflag)==0:
                matplotlib.pyplot.figure(2)
                matplotlib.pyplot.clf() 
                matplotlib.pyplot.plot(x, Nice, x, Fliq + Nice)                  
                #print itime 
                matplotlib.pyplot.grid()
                #matplotlib.pyplot.xlim([0,100])
                matplotlib.pyplot.title(str(itime))
                matplotlib.pyplot.pause(0.001)##>> 100 below equals answer
            
        else:
            pass #Should just pass to the next code
       
    end
    
    # Record stuff and get out
    return Fliq, Nice


