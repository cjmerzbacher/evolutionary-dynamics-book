# Finite Populations


## Mutation and the Neutral Theory of Evolution

New alleles are introduced into the population by mistakes in DNA replication known as **mutations**. New mutations can spread if they have neutral or adaptive effects in the environment. In the simulation below, mutations can be introduced with a frequency given by the slider. The stars are mutated organisms.

### Insert simulation here

However, most mistakes do not result in an adaptive or even neutral mutation. These neutral mutations can still fix, or take over, a population by random **genetic drift**. In fact, the vast majority of mutations at the molecular level are due to random genetic drift of neutral mutations. This theory is known as the **neutral theory of evolution**.

We can model the neutral theory with a **Moran process**. A Moran process assumes a finite, steady population size. At each time step, one organism dies and another is born. If the population has two alleles, red and blue, there are four possible outcomes in a single time step:

- Blue dies, blue is born
- Red dies, blue is born
- Blue dies, red is born
- Red dies, red is born

If the chance of a particular phenotype reproducing is proportional to that phenotype's frequency in the population, a single allele can eventually take over due to random genetic drift.

### Insert simulation here

## Selection in Finite Populations

To improve our Moran model and incorporate selection, we can define the relative fitness *r*, which is the ratio of the red organisms' fitness to the blue organisms' fitness. As *r* increases, the red organisms dominate over the blue organisms.

### Insert simulation here.

## Mating

Up until this point, we have only examined asexually reproducing populations. However, many organisms, including humans, mate and reproduce sexually. One of the simplest models of sexual reproduction results in **Hardy-Weinberg equilibrium**. Hardy-Weinberg models rely on several assumptions:
- The population is infinite
- Mating is random
- Only sexual reproduction occurs
- Organisms are diploid and each parent carries two copies of the gene
- There is no selection

While these assumptions are often violated in real-world scenarios, the Hardy-Weinberg model provides a simple way of understanding gene frequencies in a population. In the simplest case, two alleles, *A* and *a*, have frequencies *p* and *q* respectively. The genotype frequencies are *$p^2$* for *AA* homozygotes, *$q^2$* for the *aa* homozygotes, and *2pq* for the heterozygotes. Over the generations, variability is maintained in the population.

Deviations from the Hardy-Weinberg formula in finite populations can be seen in the finite population simulation below. With smaller population sizes, we see larger deviations from the ideal Hardy-Weinberg lines.

### insert simulation here
