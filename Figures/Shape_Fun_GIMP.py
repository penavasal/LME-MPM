#!/opt/anaconda3/bin/python3

from mayavi import mlab
import numpy as np

def GIMP(L, lp, Xp, Xi):
    """"""
    if (np.abs(Xp-Xi) >= L+lp):
        Sip = 0
    elif (-L-lp < Xp-Xi <= -L+lp):
        Sip = (1/(4*L*lp))*(L+lp+Xp-Xi)**2
    elif (-L+lp < Xp-Xi <= -lp):
        Sip = 1 + (Xp-Xi)/(L)
    elif (-lp < Xp-Xi <= lp):
        Sip = 1 - ((Xp - Xi)**2 + (lp)**2)/(2*L*lp)
    elif (lp < Xp-Xi <= L-lp):
        Sip = 1 - (Xp-Xi)/(L)
    elif (L-lp < Xp-Xi <= L+lp):
        Sip = (1/(4*L*lp))*(L+lp-Xp+Xi)**2
    return Sip

def d_GIMP(L, lp, Xp, Xi):
    """"""
    if (np.abs(Xp-Xi) >= L+lp):
        d_Sip = 0
    elif (-L-lp < Xp-Xi <= -L+lp):
        d_Sip = (1/(2*L*lp))*(L+lp+Xp-Xi)
    elif (-L+lp < Xp-Xi <= -lp):
        d_Sip = 1/L
    elif (-lp < Xp-Xi <= lp):
        d_Sip = -(Xp - Xi)/(L*lp)
    elif (lp < Xp-Xi <= L-lp):
        d_Sip = -1/L
    elif (L-lp < Xp-Xi <= L+lp):
        d_Sip = -(1/(2*L*lp))*(L+lp-Xp+Xi)
    return d_Sip


def print_dx_GIMP(Show_grafs):
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
            Sip_dxdy[i][j] = d_GIMP(L,lp,xp[i],xi) * GIMP(L,lp,yp[j],yi) 
            
    surf = mlab.mesh(Xp, Yp, Sip_dxdy)
    
    if Show_grafs:
        mlab.axes(surf)
        mlab.outline(surf)
        mlab.show(surf)

def print_dy_GIMP(Show_grafs):
    N = 50
    xp = yp = np.linspace(-2, 2, N)
    Xp, Yp = np.meshgrid(xp, yp, indexing='ij', sparse=False)
    Sip_dxdy = np.zeros([N,N])
    xi = yi = 0
    L = 1.
    lp = 1/4.

    for i in range(0,N):
        for j in range(0,N):
            Sip_dxdy[i][j] = GIMP(L,lp,xp[i],xi) * d_GIMP(L,lp,yp[j],yi) 
            

    surf = mlab.mesh(Xp, Yp, Sip_dxdy)
    # surf.actor.actor.scale = (0.25, 0.25, 1.0)
    
    if Show_grafs:
        mlab.axes(surf)
        mlab.outline(surf)
        mlab.show(surf)
    
def print_GIMP(Show_grafs):
    N = 50
    xp = yp = np.linspace(-2, 2, N)
    Xp, Yp = np.meshgrid(xp, yp, indexing='ij', sparse=False)
    Sip_xy = np.zeros([N,N])
    xi = yi = 0
    L = 1.
    lp = 1/4.

    for i in range(0,N):
        for j in range(0,N):
            Sip_xy[i][j] = GIMP(L,lp,xp[i],xi) * GIMP(L,lp,yp[j],yi)
            
    surf = mlab.mesh(Xp, Yp, Sip_xy)
    surf.actor.actor.scale = (1.0, 1.0, 4.0)
    
    if Show_grafs:
        mlab.show(surf)

print_GIMP(True)
# print_dx_GIMP(True)
# print_dy_GIMP(True)

