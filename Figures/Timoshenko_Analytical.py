import numpy as np
import matplotlib.pyplot as plt

L = 8
c = 0.5
D= 2*c
# c = np.sqrt(3)/2
nu = 0.3
E = 3E5
P = 100
I = (1/12)*(2*c)**3

DeltaX = 0.1
Nx = int(L/DeltaX)
Ny = int(2*c/DeltaX)
x0 = np.linspace(0,L,Nx)
y0 = np.linspace(-c,c,Ny)
X0, Y0 = np.meshgrid(x0, y0, indexing='ij', sparse=False)

Xf = np.zeros([Nx,Ny])
Yf = np.zeros([Nx,Ny])

for i in range(0,Nx):
    for j in range(0,Ny):

        Xf[i][j] = X0[i][j] + P*Y0[i][j]/(6*E*I)*((6*L-3*X0[i][j])*X0[i][j] + (2+nu)*(Y0[i][j]**2 - (D**2)/4 ))
        Yf[i][j] = Y0[i][j] - P/(6*E*I)*(3*nu*Y0[i][j]**2*(L-X0[i][j]) + (4+5*nu)*X0[i][j]*(D**2)/4 + (3*L-X0[i][j])*X0[i][j]**2)


fig, ax = plt.subplots()
# ax.scatter(X0,Y0)
ax.scatter(Xf,Yf)
ax.axis('equal')
fig.tight_layout()
plt.grid()
plt.show()
