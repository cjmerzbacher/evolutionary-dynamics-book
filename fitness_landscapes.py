import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

#Constants
M = 1.8 #Upper limit of expression
d = 0.17 #Growth rate advantage conferred by Z
n = 0.02 #Cost of lac operon at 0 lactose

def f(Z, L):
    c = (n*Z)/(1-Z/M) #cost function
    b = d*Z*L   #benefit function
    return b - c


#Make grid of Z and L values
z = np.linspace(0, 1.5, 20)
l = np.linspace(0, 5.0, 20)

Z, L = np.meshgrid(z, l)

#calculate fitness function
F = f(Z, L)

fig = plt.figure()
ax = mplot3d.axes3d.Axes3D(fig)

ax.set_xlim3d([0, 1.5])
ax.set_xlabel('Relative Lac expression, Z/$Z_{wt}$')

ax.set_ylim3d([0, 5.0])
ax.set_ylabel('Lactose concentration, M')

ax.set_zlim3d([-0.5, 1.5])
ax.set_zlabel('Relative growth rate difference')

ax.plot_surface(Z, L, F)

plt.show()
