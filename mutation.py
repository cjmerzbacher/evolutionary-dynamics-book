import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 20 #number of individuals
num_red = int(N/2)
color_choice = ['r', 'b']
pop = []

for i in range(N):
    x = np.random.uniform(0.1, 4.9, 1)[0]
    y = np.random.uniform(0.1, 4.9, 1)[0]
    color = 'ro'
    pop.append([x, y, color])

prob = [0.9, 0.1]
def generation():
    i = np.random.randint(1,N)
    ind = pop[i]
    c = np.random.choice(color_choice, p=prob, replace=True) #probability of changing colors
    if c == 'r':
        ind[2] = 'ro'
    else:
        ind[2] = 'y*'
    pop[i] = ind

generations = 100

fig, ax = plt.subplots()
ax.set_xlim([0., 5.0])
ax.set_ylim([0., 5.0])

def update(frame):
    ax.clear()
    generation()
    for i in range(N):
        ax.plot(pop[i][0], pop[i][1], pop[i][2], markersize=20)
    ax.set_title('Time Step = {}'.format(frame))

ani = FuncAnimation(fig, update, generations, interval = 100, blit=False)
plt.show()
