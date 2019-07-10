import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

global pop, n_r, N, pop_blue, pop_red
N = 20 #number of individuals SLIDER
prop_red = 0.5 #proportion red SLIDER
n_r = prop_red*N
num_reds = int(prop_red*N)
color_choice = ['r', 'b']
pop_red = []
pop_blue = []

#initialize populations of red and blue
for i in range(num_reds):
    x = np.random.uniform(0.1, 4.9, 1)[0]
    y = np.random.uniform(0.1, 4.9, 1)[0]
    color = 'ro'
    pop_red.append([x, y, color])

for i in range(N-num_reds):
    x = np.random.uniform(0.1, 4.9, 1)[0]
    y = np.random.uniform(0.1, 4.9, 1)[0]
    color = 'bo'
    pop_blue.append([x, y, color])

pop = pop_blue+pop_red

r = 0.1 #SLIDER
def generation():
    #Location of new individual
    x = np.random.uniform(0.1, 4.9, 1)[0]
    y = np.random.uniform(0.1, 4.9, 1)[0]

    global pop, n_r, N, pop_blue, pop_red
    prob_reproduction = [(r*n_r)/(r*n_r+N-n_r),(N-n_r)/(r*n_r+N-n_r)]
    prob_elimination = [n_r/N, (N-n_r)/N]

    elim = np.random.choice(color_choice, p=prob_elimination)
    repr =  np.random.choice(color_choice, p=prob_reproduction)


    if elim == 'r' and len(pop_red) != 0:
        del pop_red[0]
        n_r = n_r -1
    if elim == 'b' and len(pop_blue) != 0:
        del pop_blue[0]

    if repr == 'r':
        pop_red.append([x,y,'ro'])
        n_r += 1
    else:
        pop_blue.append([x,y,'bo'])

    pop = pop_blue + pop_red



generations = 100


fig, ax = plt.subplots()

def update(frame):
    generation()
    ax.clear()
    for i in range(N):
        ax.plot(pop[i][0], pop[i][1], pop[i][2], markersize=20)
    ax.set_title('Time Step = {}'.format(frame+1))
    ax.set_xlim([0., 5.0])
    ax.set_ylim([0., 5.0])

ani = FuncAnimation(fig, update, generations, repeat=False)
plt.show()
