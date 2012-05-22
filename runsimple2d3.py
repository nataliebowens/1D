def simple2d3(Fliq=None, Nice=None, Ntimes=None, diffperdt=None, rainperdt_terr=None, rainperdt_edge=None, Fliqmax=None):
    "This is a 2d simulation"
    
    print "This is a 2d simulation"

    # step dynamics, 2-dimensional, fixed boundary conditions in the x-direction corresponding to
    # prismatic-prismatic edges and prismatic boundary conditions in the z-direction
    import numpy
    import time
    import matplotlib.mlab
    import matplotlib.pyplot
    #import pdb
    
    # Other initializing
    Fliqnext = numpy.zeros(numpy.shape(Fliq))
    Nx,Nz = Fliq.shape
    padx = numpy.zeros([1,Nz])
    Ntot = Nx*Nz
    endx = Nx-1
    endz = Nz-1
    
    print Ntimes
    
    # Loop over time
    for itime in range(1,Ntimes):
        
        # Diffusion of liquid to adjacent cells in the x-direction
        Fliqnext[1:endx,:] = Fliq[1:endx,:] * (1 - diffperdt)     + (Fliq[0:endx-1,:] + Fliq[2:endx+1,:]) * diffperdt / 2
        Fliqnext[0,:]      = Fliq[0,:]      * (1 - diffperdt / 2) +  Fliq[1,:]                            * diffperdt / 2
        Fliqnext[endx,:]   = Fliq[endx,:]   * (1 - diffperdt / 2) +  Fliq[endx-1,:]                       * diffperdt / 2
        
        # Diffusion of liquid to adjacent cells in the z-direction
        Fliqnext[:,1:endz] = Fliq[:,1:endz] * (1 - diffperdt)     + (Fliq[:,0:endz-1] + Fliq[:,2:endz+1]) * diffperdt / 2
        Fliqnext[:,0]      = Fliq[:,0]      * (1 - diffperdt)     + (Fliq[:,1]        + Fliq[:,endz])     * diffperdt / 2
        Fliqnext[:,endz]   = Fliq[:,endz]   * (1 - diffperdt)     + (Fliq[:,endz-1]   + Fliq[:,0])        * diffperdt / 2
        
        # Initialize the Edge array
        Eice = numpy.zeros(numpy.shape(Nice))
        
        # Look for edges in x
        dNicex = numpy.diff(Nice,axis=0)
        dNicex_padright = concatenate([dNicex,padx],axis=0)
        dNicex_padleft  = concatenate([padx,dNicex],axis=0)
        Iedge_up = matplotlib.mlab.find(dNicex_padright > 0)
        Eice.reshape(Ntot)[Iedge_up] = 1
        Iedge_dn = matplotlib.mlab.find(dNicex_padleft < 0)
        Eice.reshape(Ntot)[Iedge_dn] = -1
        
        # Look for edges in z
        #pdb.set_trace()
        Nice_padright = concatenate([Nice,Nice[:,0].reshape([Nx,1])],   axis=1)
        Nice_padleft  = concatenate([Nice[:,endz].reshape([Nx,1]),Nice],axis=1)
        dNicez_padright = numpy.diff(Nice_padright,axis=1)
        dNicez_padleft  = numpy.diff(Nice_padleft, axis=1)
        Iedge_up = matplotlib.mlab.find(dNicez_padright > 0)
        Eice.reshape(Ntot)[Iedge_up] = 1
        Iedge_dn = matplotlib.mlab.find(dNicez_padleft < 0)
        Eice.reshape(Ntot)[Iedge_dn] = -1
        
        # Find locations of edges and terraces
        Iterr = matplotlib.mlab.find(Eice == 0)
        Iedge = matplotlib.mlab.find(Eice != 0)
        
        # Net deposition from vapor
        Fliqnext.reshape(Ntot)[Iterr] = Fliqnext.reshape(Ntot)[Iterr] + rainperdt_terr.reshape(Ntot)[Iterr]
        Fliqnext.reshape(Ntot)[Iedge] = Fliqnext.reshape(Ntot)[Iedge] + rainperdt_edge.reshape(Ntot)[Iedge]
        
        # Look for layer nucleation sites
        Ilrnc = matplotlib.mlab.find(Fliqnext > Fliqmax)
        Fliqnext.reshape(Ntot)[Ilrnc] = Fliqnext.reshape(Ntot)[Ilrnc] - 1
        Nice.reshape(Ntot)[Ilrnc] = Nice.reshape(Ntot)[Ilrnc] + 1
        
        # Update Fliq
        Fliq = Fliqnext
    
    # Record stuff and get out
    return Fliq, Nice



# Two-dimensional simulation

from pylab import *
import pdb
import time
import pickle
import time


# Load a 1-d starting vector
f = open('simple1d3.dat', 'r')
Fliqx          = pickle.load(f)
Nicex          = pickle.load(f)
x              = pickle.load(f)
diffperdt      = pickle.load(f)
rainperdt_terr = pickle.load(f)
rainperdt_edge = pickle.load(f)
Fliqmax        = pickle.load(f)
f.close()

# Construct a 2-d array from it
Nz = 100
Ntimes = 6000
z = linspace(0,Nz-1,Nz)
zgrid,Fliqxz = meshgrid(z,Fliqx)
zgrid,Nicexz = meshgrid(z,Nicex)
zgrid,rainperdt_terrxz = meshgrid(z,rainperdt_terr)
zgrid,rainperdt_edgexz = meshgrid(z,rainperdt_edge)
#plot(x, Nicexz[:,0], x, Fliqxz[:,0] + Nicexz[:,0])
f
# Introduce a perturbation
zpert = 10
Fliqxz[:,zpert] = Fliqxz[:,zpert]*1.1

# Call to simple2d3
tstart = time.time()
[Fliq, Nice] = simple2d3(Fliqxz, Nicexz, Ntimes, diffperdt, rainperdt_terrxz, rainperdt_edgexz, Fliqmax)
tend = time.time()
print  (tend - tstart)/60
figure(2); clf(); plot(x,Nice[:,zpert],x,Fliq[:,zpert] + Nice[:,zpert]); xlabel("x"); title("at perturbed z")
figure(3); clf(); contour(transpose(Nice),30); xlabel("x"),ylabel("z"); colorbar()

