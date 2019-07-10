# Modeling Evolution

We can use differential equations to model reproduction, selection, mutation, and thus evolution. While mutations are introduced randomly, selective pressures and their effects on the frequencies of alleles in the populations are deterministic.

## Reproduction

The simplest biological models include reproducing organisms. Bacteria such as *E. coli* can divide into two identical daughter cells in a process known as **asexual reproduction**. Without limiting environmental conditions, the number of cells is $2^n$. This type of exponential growth results in an explosion of population. If even a single bacterial cell grew exponentially for three days, the total mass of its offspring would exceed the mass of the earth! Below is an example of a simple exponential function.

### Insert exp growth here

However, cells do not grow exponentially forever. Depletion of nutrients, accumulation of toxic byproducts, or increased cell death can all contribute to slowing growth. Another function commonly used to model microbial growth is a logistic functions. As the number of bacteria nears some carrying capacity, K, growth slows until the population asymptotes to the carrying capacity.

### Insert logistic growth here

Other, more complex equations can model aspects of reproduction not captured by these two simple models. However, as with any choice of model, it's important to remember that all models have tradeoffs in accuracy, simplicity, and utility. For many applications, an exponential or logistic growth curve is sufficient.

## Selection

Selection operates when two types of individuals reproduce at different rates. If two types, A and B, reproduce at rates *a* and *b*, respectively, Assuming exponential growth, two differential equations can express the frequencies of A and B in the population, *x* and *y*.

### Insert equations here

If you run the simulation below, you will see that the fittest type will outcompete the other. This is an example of survival of the fittest.

## Insert simulation here

Not all populations have a linear growth rate. Vary the slider labeled "Growth rate". What happens if it is less than 1? Greater than 1?

If the growth rate is less than one, the population is *subexponential*. In this case, neither population outcompetes the other entirely and a mixed equilibrium of A and B is stable. This phenomenon is known as **survival of all**.

If the growth rate is greater than one, the population is *superexponential*. In this case, the first population to take over dominates and cannot be invaded, even if the other type has a higher growth rate. This case is known as **survival of the first**.

These results can be expanded to three or more types. Example code of a four-type equilibrium is below.

#Insert four-type simulation here.

## Mutation

New alleles are introduced into the population by mistakes in DNA replication known as **mutations**. New mutations can spread if they have neutral or adaptive effects in the environment. In the simulation below, mutations can be introduced with a frequency given by the slider. The stars are mutated organisms. 

#Insert mutation simulation here
