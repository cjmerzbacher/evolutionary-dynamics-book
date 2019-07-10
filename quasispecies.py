#Import necessary packages
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import random
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import pandas as pd

#Establish fitness function
def f(x, y):
    return 3*(1-x)**2.*np.exp(-(x**2) - (y+1)**2) #single peak
    #- 10*(x/5 - x**3 - y**5)*np.exp(-x**2-y**2)-1/3*np.exp(-(x+1)**2 - y**2) #dips

#Make grid of x, y, z values
x = np.linspace(-6, 6, 121)
y = np.linspace(-6, 6, 121)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

#Set mutation rate and population
mutation_rate = 0.5
population = 50
quasispecies_variance = 0.1

#initialize organisms randomly
#center point
x_center = random.randint(-60, 60)/10
y_center = random.randint(-60, 60)/10

#establish other members of quasispecies
organisms = [[x_center, y_center, f(x_center, y_center)]]
for p in range(population):
    x_var = random.randint(-quasispecies_variance*10, quasispecies_variance*10)/10
    y_var = random.randint(-quasispecies_variance*10, quasispecies_variance*10)/10
    x = x_center + x_var
    y = y_center + y_var
    z = f(x, y)
    organisms.append([x, y, z])

#conversion function to convert x/y values to indices
def convert(x):
    return int((x+6)*10)

#runs generation
def run_generation(orgs):
    kids = []
    for p in range(population):
        mutate = 1
        x,y,z = orgs[p]
        step_x = random.randint(-0.2*10, 0.2*10)/10
        step_y = random.randint(-0.2*10, 0.2*10)/10
        #print("Organism coordinates", x, y, z)
        if mutate == 1:
            prev_x, prev_y, prev_z = x, y, z
            conv_x, conv_y = convert(x), convert(y)
            x = x + step_x
            y = y + step_y
            z = f(x, y)
            if z >= prev_z:
                kids.append([x, y, z])
            else:
                if random.randint(0, 1) == 1:
                    kids.append([x,y,z])
                else:
                    kids.append([prev_x, prev_y, prev_z])
        else:
            kids.append([x, y, z])
    return kids

generations = 200
generation_data= [organisms]
xs = []
ys = []
zs = []
k = organisms
for g in range(generations):
    k_prev = k
    k = run_generation(k_prev)
    xd = [o[0] for o in k]
    yd = [o[1] for o in k]
    zd = [o[2] for o in k]
    generation_data.append(k)
    xs.append(xd)
    ys.append(yd)
    zs.append(zd)

#Final animation
# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

# Setting the axes properties
ax.set_xlim3d([-6.0, 6.0])
ax.set_xlabel('X')

ax.set_ylim3d([-6.0, 6.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-6.0, 6.0])
ax.set_zlabel('Fitness')

ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10, cmap="Greens")

title = ax.set_title("Test")

sct, = ax.plot([], [], [], 'o', markersize = 4, markerfacecolor = 'r', markeredgecolor = 'r')
def update(frame, xa, ya, za):
    sct.set_data(xa[frame], ya[frame])
    sct.set_3d_properties(za[frame])
    title.set_text('Generation = {}'.format(frame))


# Creating the Animation object
ani = animation.FuncAnimation(fig, update, generations, fargs=(xs,ys,zs), interval=50, blit=False)


plt.show()

#Save video
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
ani.save('test.mp4', writer=writer)
