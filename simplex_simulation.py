from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

#set constants with sliders
growth = widgets.FloatSlider(min=0., max=5.)
initial_frac = widgets.FloatSlider(min=0., max=1.)
x_fitness = widgets.FloatSlider(min=0., max=5.)
y_fitness = widgets.FloatSlider(min=0., max=5.)
print("Growth rate:")
display(growth)
print("Initial fraction of X:")
display(initial_frac)
print("Fitness of X:")
display(x_fitness)
print("Fitness of Y:")
display(y_fitness)

a = 1 #fitness of X
b = 1.2 #fitness of Y
c = 1 #growth rate linearity
Xo = [0.5, 0.5] #initial frequencies

#Linear/Nonlinear growth rates
def get_freqs(X, t):
  x, y = X
  dxdt = a*x**c
  dydt = b*y**c
  return [dxdt, dydt]

generations = 20
times = np.linspace(0., generations, generations)
ans = odeint(func=get_freqs, y0 = Xo, t = times)

Xs = ans[:, 0]
Ys = ans[:, 1]
Xfrac = Xs/(Xs + Ys)
Yfrac = Ys/(Xs + Ys)

#Pie chart of pop fracs
#fig, ax = plt.subplots()
#final_fracs = [Xfrac[199], Yfrac[199]]
labels = ['X', 'Y']
#plt.pie(final_fracs, labels = labels);


fig, ax = plt.subplots()

def update(frame, Xa, Ya):
    ax.clear()
    ax.axis('equal')
    nums = [Xa[frame], Ya[frame]]
    ax.pie(nums, labels=labels)
    ax.set_title('Generation = {}'.format(frame))

ani = FuncAnimation(fig, update, generations, fargs = (Xfrac, Yfrac), interval = 100, blit=False)
plt.show()
