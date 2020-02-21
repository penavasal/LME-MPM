import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from matplotlib.ticker import FixedLocator
from matplotlib.ticker import FormatStrFormatter


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

def Get_Riemann_I(Stress_I,Velocity_I):
    R_I = (0.5/StaticVisco)*(- Stress_I + Velocity_I*StaticVisco)
    return R_I

def Get_Riemann_II(Stress_II,Velocity_II):
    R_II = (0.5/StaticVisco)*(Stress_II + Velocity_II*StaticVisco)
    return R_II

# Material properties
L = 0.1333
E = 200*10**9 # Pa
rho = 7833 # kg/m³
CEL = 5033 # m/s , np.sqrt(E/rho)
# L = 1
# E = 1 # Pa
# rho = 1 # kg/m³
# CEL = 1 # m/s

T_go = L/CEL #
T_end = 16*T_go

# Spatial mesh
# dx = 0.000001
dx = 0.001

# Time mesh
dt =  0.000001
# dt =  0.1

# Discretize domain
N_x = int(L/dx)
X = np.linspace(0,L,N_x)
# Discretize time
N_t = int(T_end/dt)
T = np.linspace(0,T_end,N_t)

# Initial conditions
v0 = -5
# v0 = -1
Stress = np.zeros([N_t,N_x])
Velocity = np.zeros([N_t,N_x])
for x in range(0,N_x):
    if X[x] <= 0.25*L :
        Velocity[0,x] = v0
    else :
        Velocity[0,x] = 0

        
# Get the static viscosity
StaticVisco = np.sqrt(E*rho)

        
# figures
Show_grafs = True
format_fig = 'png'
        
################################################################
####################### Loop in time ###########################
################################################################
for t in range(0,N_t):
    
    ############################################################    
    ##################### Solve domain #########################
    ############################################################
    for x in range(1,N_x-1):

        # Get boundary values through characteristics lines
        t_I = T[t] - X[x]/CEL
        t_II = T[t] - (L-X[x])/CEL
    
        # Get stress and velocity values in I and II
        if(t_I>0):
            t_i = find_nearest(T, t_I)
            Stress_I = 0
            Velocity_I = Velocity[t_i,0]
        else:
            x_i = find_nearest(X, L-T[t]*CEL)
            Stress_I = Stress[0,x_i]
            Velocity_I = Velocity[0,x_i]
        if(t_II>0):
            t_i = find_nearest(T, t_II)
            Stress_II = Stress[t_i,-1]
            Velocity_II = 0
        else:
            x_i = find_nearest(X, T[t]*CEL)
            Stress_II = Stress[0,x_i]
            Velocity_II = Velocity[0,x_i]
            
        # Rimman invariants
        R_I = Get_Riemann_I(Stress_I,Velocity_I)
        R_II = Get_Riemann_II(Stress_II,Velocity_II)
        
        # Stress-velocity actualization
        Stress[t,x] = StaticVisco*(R_II - R_I) 
        Velocity[t,x] = R_I + R_II
    
    
    ############################################################
    ################### Solve left boundary ####################
    ############################################################

    # Get time in the right boundary
    t_II = T[t] - (L-X[0])/CEL

    # Get stress and velocity values in I and II 
    if(t_II>0):
        t_i = find_nearest(T, t_II)
        Velocity_II = 0
        Stress_II = Stress[t_i,-1]
    else:
        x_i = find_nearest(X, T[t]*CEL)
        Velocity_II = Velocity[0,x_i]
        Stress_II = Stress[0,x_i]

    # Get Riemann II
    R_II = Get_Riemann_II(Stress_II,Velocity_II)
    
    # Get the value in the boundary
    Stress[t,0] = 0
    Velocity[t,0] = 2*R_II
            
    ############################################################
    ################### Solve right boundary ###################
    ############################################################

    # Get time in the left boundary
    t_I = T[t] - X[-1]/CEL   
    
    # Get stress and velocity values in I and II
    if(t_I>0):
        t_i = find_nearest(T, t_I)
        Stress_I = 0
        Velocity_I = Velocity[t_i,0]
    else:
        x_i = find_nearest(X, L-T[t]*CEL)
        Stress_I = Stress[0,x_i]
        Velocity_I = Velocity[0,x_i]

    # Get Riemann I
    R_I = Get_Riemann_I(Stress_I,Velocity_I)

    # Get the value in the boundary
    Stress[t,-1] = - 2*StaticVisco*R_I
    Velocity[t,-1] = 0

################################################################
############### Print results in x-t diagram ###################
################################################################

# Generate mesh
XX, TT = np.meshgrid(X,T)

min_vel = np.min(np.min(Velocity))
max_vel = np.max(np.max(Velocity))
min_str = np.min(np.min(Stress))
max_str = np.max(np.max(Stress))

################################################################
################### Velocity 3D Figure  ########################
################################################################

fig = plt.figure()
ax = fig.gca(projection='3d')
# ax.grid(False)
ax.xaxis.pane.set_edgecolor('black')
ax.yaxis.pane.set_edgecolor('black')
ax.zaxis.pane.set_edgecolor('black')
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
for line in ax.xaxis.get_ticklines():
    line.set_visible(False)
for line in ax.yaxis.get_ticklines():
    line.set_visible(False)


surf = ax.plot_surface(XX, TT, Velocity, rstride=1,
                       cstride=1, cmap=cm.jet,
                       linewidth=0, antialiased=False)

ax.set_zlim3d(min_vel, max_vel)
ax.set_zticks([min_vel, 0.5*min_vel, 0, 0.5*max_vel, max_vel])
plt.tight_layout()
fig.colorbar(surf)

ax.set_xlabel('X')
ax.set_ylabel('Time')
ax.set_zlabel('Velocity')
plt.savefig("Analytical_3D_Velocity.%s"%(format_fig))  
if Show_grafs:
    plt.show()
    
fig.clear()


################################################################
################### Proyections Velocity #######################
################################################################

fig = plt.figure()
ax = fig.gca(projection='3d')
# ax.grid(False)
ax.xaxis.pane.set_edgecolor('black')
ax.yaxis.pane.set_edgecolor('black')
ax.zaxis.pane.set_edgecolor('black')
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
for line in ax.xaxis.get_ticklines():
    line.set_visible(False)
for line in ax.yaxis.get_ticklines():
    line.set_visible(False)

cset_z = ax.contour(XX, TT, Velocity, zdir='z', offset=min_vel, cmap=cm.coolwarm)
cset_x = ax.contour(XX, TT, Velocity, zdir='x', offset=0, cmap=cm.coolwarm)
cset_y = ax.contour(XX, TT, Velocity, zdir='y', offset=T_end, cmap=cm.coolwarm)

ax.set_zlim3d(min_vel, max_vel)
ax.set_zticks([min_vel, 0.5*min_vel, 0, 0.5*max_vel, max_vel])
plt.tight_layout()
fig.colorbar(cset_z)

ax.set_xlabel('X')
ax.set_ylabel('Time')
ax.set_zlabel('Velocity')
plt.savefig("Analytical_contour_Velocity.%s"%(format_fig))
if Show_grafs:
    plt.show()
fig.clear()


################################################################
################## 1D results of velocity ######################
################################################################

fig, ax = plt.subplots()
ax.plot(T,Velocity[:,0])
ax.set_xlabel('Time')
ax.set_ylabel('Velocity')
plt.title('Right side velocity evolution')
plt.tight_layout()
plt.grid()
plt.savefig("1D_right_Velocity.%s"%(format_fig))
if Show_grafs:
    plt.show()
fig.clear()


################################################################
##################### Stress 3D Figure #########################
################################################################

fig = plt.figure()
ax = fig.gca(projection='3d')
# ax.grid(False)
ax.xaxis.pane.set_edgecolor('black')
ax.yaxis.pane.set_edgecolor('black')
ax.zaxis.pane.set_edgecolor('black')
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
for line in ax.xaxis.get_ticklines():
    line.set_visible(False)
for line in ax.yaxis.get_ticklines():
    line.set_visible(False)
        
surf = ax.plot_surface(XX, TT, Stress, rstride=1,
                       cstride=1, cmap=cm.jet,
                       linewidth=0, antialiased=False)
ax.set_zlim3d(min_str, max_str)
ax.set_zticks([min_str,0.5*min_str,0, 0.5*max_str, max_str])
plt.tight_layout()
fig.colorbar(surf)

ax.set_xlabel('X')
ax.set_ylabel('Time')
ax.set_zlabel('Stress')
plt.savefig("Analytical_3D_Stress.%s"%(format_fig))
if Show_grafs:
    plt.show()

fig.clear()

################################################################
#################### Proyections Stress ########################
################################################################

fig = plt.figure()
ax = fig.gca(projection='3d')
# ax.grid(False)
ax.xaxis.pane.set_edgecolor('black')
ax.yaxis.pane.set_edgecolor('black')
ax.zaxis.pane.set_edgecolor('black')
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
for line in ax.xaxis.get_ticklines():
    line.set_visible(False)
for line in ax.yaxis.get_ticklines():
    line.set_visible(False)

cset_z = ax.contour(XX, TT, - Stress, zdir='z',
                        offset=min_str, cmap=cm.coolwarm)
cset_x = ax.contour(XX, TT, - Stress, zdir='x',
                        offset=0, cmap=cm.coolwarm)
cset_y = ax.contour(XX, TT, - Stress, zdir='y',
                        offset=T_end, cmap=cm.coolwarm)

ax.set_zlim3d(min_str, max_str)
ax.set_zticks([min_str,0.5*min_str,0, 0.5*max_str, max_str])
plt.tight_layout()
fig.colorbar(cset_z)

ax.set_xlabel('X')
ax.set_ylabel('Time')
ax.set_zlabel('Stress')
plt.savefig("Analytical_contour_Stress.%s"%(format_fig))
if Show_grafs:
    plt.show()

fig.clear()

################################################################
################## 1D results of stress ########################
################################################################

fig, ax = plt.subplots()
ax.plot(T,Stress[:, find_nearest(X, 0.25*L)])
ax.set_xlabel('Time')
ax.set_ylabel('Stress')
plt.title('3/4 L point stress evolution')
plt.tight_layout()
plt.grid()
plt.savefig("1D_left_Stress.%s"%(format_fig))
if Show_grafs:
    plt.show()
fig.clear()


