import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display


growth = widgets.FloatSlider(min=0., max=10.)
carrying = widgets.IntSlider(min=10., max=1000.)
print("Growth rate:")
display(growth)
print("Carrying capacity:")
display(carrying)

K = 100. #carrying capacity
r = growth.value
def exponential(C, t):
  dCdt = C*r
  return dCdt

def logistic(C, t):
  dCdt = C*r*(1-C/K)
  return dCdt

times = np.linspace(0., 2., 100)
exp_Cs = odeint(func=exponential, y0=[1.], t=times)
log_Cs = odeint(func=logistic, y0=[1.], t=times)


fig, ax = plt.subplots()
ax.plot(times, exp_Cs, label='Exponential')
ax.plot(times, log_Cs, label='Logistic')

ax.legend()
ax.set_xlabel('time, hr')
ax.set_ylabel('Number of cells')
