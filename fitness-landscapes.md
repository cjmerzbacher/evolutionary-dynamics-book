# Fitness Landscapes
## Sequence spaces and fitness landscapes

**Sequence space** is a way of representing every possible sequence in a genome. Each dimension represents a nucleotide site that can have one of four values (A, C, T, and G). For simplicity, many models reduce this to two values (0 and 1). Neighbors in sequence space differ by a single nucleotide.

A 100-base pair segment of genome has a 100-dimensional sequence space, and a full human genome a much higher-dimensional one. While the size of sequence space makes it impossible to model directly, it is a useful thought experiment to imagine evolution as a trajectory through sequence space.

Evolution is driven by fluctuations in the **fitness landscape**. Fitness landscapes visualize the relationship between genotypes and reproductive success. Each point in sequence space, which corresponds to a specific genotype, has an associated fitness value. While most possible genomes are not viable and thus their corresponding fitness values are low, regions of higher fitness exist.

### Tuning protein expression levels
Fitness landscapes can also be used to describe protein sequences and expression levels. One example we will consider in more depth is tuning lac operon expression levels in *E. coli*.

The lactose operon, or lac operon, is a sequence of genes which produce the proteins needed for *E. coli* to digest lactose. Glucose is the preferred carbon source for the bacterium, so if sufficient glucose is present, lactose does not need to be digested and the lac operon should be turned off. Furthermore, when there is no lactose present, the operon should be turned off regardless of the glucose concentration. When only lactose is present, however, the operon should work. In this case, it encodes LacZ, which degrades lactose for energy, and LacY, which transports lactose into the cell.

In addition to just turning off and on, however, the lac operon can tune its expression levels to match the concentration of lactose. Cells with just enough LacZ to digest the surrounding lactose but not too much to slow down production of other proteins reproduce the fastest. By natural selection, we would expect this expression level to dominate the population over time.

The tradeoff between too much and too little LacZ can be modeled by a simple cost/benefit function. The cost function describes the tradeoff of producing LacZ rather than another useful protein. When fit to experimental data, a limit M describes the upper limit of LacZ expression at which the cost of production strongly increases. The cost function used is:

### Equation here

The benefit function describes the growth rate advantage conferred by LacZ:

### Equation here

Subtracting the cost from the benefit results in the fitness function. This function can be calculated for a variety of LacZ and external lactose levels to find the optimal lac operon expression at a specific lactose level:

## Picture/code inserted here.

## Quasispecies theory
Natural selection and mutations guide populations through sequence space to an equilibrium. This equilibrium often results in a population of variable genomes, known as a **quasispecies**, rather than a single genotype. For instance, viruses mutate rapidly, which results in multiple genotypes within a single host. Most of these viruses have approximately equal fitness; it is a more successful reproduction strategy to have a broader range of fit genotypes rather than a single fittest genotype. This phenomenon is known as **survival of the quasispecies**.

The quasispecies equation describes the mutation and selection process of an infinitely large population on the fitness landscape. The relative frequency of a genome *i* changes because of two phenomena: species death to maintain population size and mutation from another genome *j*. These two teams make up the quasispecies equation:

### Quasispecies equation here; insert phi and subscripts below

The first term describes mutation. The number of mutations converting genome *j* to genome *i* is equivalent to the frequency of *j* in the population multiplied by the fitness of *j* (*fj*) and *qij*, the probability that the mutation will occur. The second term accounts for removal of *i* due to death, which occurs at the rate of the average population fitness phi. Quasispecies climb upward in a fitness landscape to one globally stable equilibrium; however, this equilibrium may not include the fittest individual genome.

### Insert simulation here.
