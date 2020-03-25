#!/opt/anaconda3/bin/python3

from mayavi import mlab
import numpy as np

def MPM(L, Xp, Xi):
    """"""
    if (np.abs(Xp-Xi) >= L):
        Sip = 0
    elif (-L <= Xp-Xi <= 0):
        Sip = 1-np.abs(Xp-Xi)/L
    elif (L >= Xp-Xi >=0):
        Sip = 1-np.abs(Xp-Xi)/L
    return Sip

def d_MPM(L, Xp, Xi):
    """"""
    if (np.abs(Xp-Xi) >= L):
        Sip = 0
    elif (-L <= Xp-Xi <= 0):
        Sip = 1/L
    elif (L >= Xp-Xi >=0):
        Sip = -1/L
    return Sip

def print_dx_MPM(Show_grafs):
    N = 50
    xp = yp = np.linspace(-2, 2, N)
    Xp, Yp = np.meshgrid(xp, yp, indexing='ij', sparse=False)
    Sip_dxdy = np.zeros([N,N])
    xi = yi = 0
    L = 1.
    format_fig = 'png'

    for i in range(0,N):
        for j in range(0,N):
            Sip_dxdy[i][j] = d_MPM(L,xp[i],xi) * MPM(L,yp[j],yi)
           
           
    surf = mlab.mesh(Xp, Yp, Sip_dxdy)
    
    if Show_grafs:
        mlab.axes(surf)
        mlab.outline(surf)
        mlab.show(surf)

def print_dy_MPM(Show_grafs):
    N = 50
    xp = yp = np.linspace(-2, 2, N)
    Xp, Yp = np.meshgrid(xp, yp, indexing='ij', sparse=False)
    Sip_dxdy = np.zeros([N,N])
    xi = yi = 0
    L = 1.
    lp = 1/4.
    format_fig = 'png'

    for i in range(0,N):
        for j in range(0,N):
            Sip_dxdy[i][j] = MPM(L,xp[i],xi) * d_MPM(L,yp[j],yi) 
            

    surf = mlab.mesh(Xp, Yp, Sip_dxdy)
    # surf.actor.actor.scale = (0.25, 0.25, 1.0)
    
    if Show_grafs:
        mlab.axes(surf)
        mlab.outline(surf)
        mlab.show(surf)
            
def print_MPM(Show_grafs):
    N = 50
    xp = yp = np.linspace(-2, 2, N)
    Xp, Yp = np.meshgrid(xp, yp, indexing='ij', sparse=False)
    Sip_xy = np.zeros([N,N])
    xi = yi = 0
    L = 1.
    lp = 1/4.
    format_fig = 'png'

    for i in range(0,N):
        for j in range(0,N):
            Sip_xy[i][j] = MPM(L,xp[i],xi) * MPM(L,yp[j],yi)
            

    surf = mlab.mesh(Xp, Yp, Sip_xy)
    surf.actor.actor.scale = (1.0, 1.0, 4.0)
    
    if Show_grafs:
        mlab.show(surf)
    
    
print_MPM(True)
# print_dx_MPM(True)
# print_dy_MPM(True)
