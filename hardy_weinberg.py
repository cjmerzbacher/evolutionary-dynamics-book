import numpy as np
import matplotlib.pyplot as plt

#Define constants (with sliders)
N = 200
p = 0.5
q = 1-p
a_freq = [p, q]
genotypes = ['A', 'a']
pop = [np.random.choice(genotypes, 2, p=a_freq, replace=True) for i in range(N)]

def cross(parent1, parent2):
    offspring_1 = np.random.choice(parent1, size = 1, replace = False)
    offspring_2 = np.random.choice(parent2, size = 1, replace = False)
    offspring = [offspring_1[0], offspring_2[0]]
    return offspring

def random_mating(pop):
    temp_pop = pop
    for n in range(N):
        parents = np.random.randint(1,N,2)
        temp_pop[n] = cross(pop[parents[0]], pop[parents[1]])
    pop = temp_pop

I = 200 #number of individuals
aa_freq, AA_freq, aA_freq = [], [], []
p_vec = []
for i in range(I):
    p = np.random.uniform(0., 1., 1)[0]
    q = 1-p
    a_freq = [p, q]
    pop = [np.random.choice(genotypes, 2, p=a_freq, replace=True) for i in range(N)]
    random_mating(pop)

    f_aa, f_aA, f_AA = 0, 0, 0

    for n in range(N):
        if pop[n] == ['A', 'A']:
            f_AA +=1
        if ((pop[n] == ['A','a']) or (pop[n] == ['a','A'])):
            f_aA += 1
        if pop[n] == ['a', 'a']:
                f_aa +=1

    f_aa = f_aa/N
    f_AA = f_AA/N
    f_aA = f_aA/N

    p_vec.append(p)
    aa_freq.append(f_aa)
    aA_freq.append(f_aA)
    AA_freq.append(f_AA)

#Theoretical curves
xs = np.linspace(0., 1., 100)
AAs = [(x**2) for x in xs]
aas = [(1-x)**2 for x in xs]
aAs = [2*x*(1-x) for x in xs]
fig, ax = plt.subplots()
ax.plot(p_vec, aa_freq, 'r.')
ax.plot(p_vec, AA_freq, 'b.')
ax.plot(p_vec, aA_freq, 'g.')
ax.plot(xs, aas, 'r-', label='aas')
ax.plot(xs, AAs, 'b-', label='AAs')
ax.plot(xs, aAs,'g-', label='aAs')

ax.legend()
ax.set_xlabel('p or 1-q')
plt.show()
