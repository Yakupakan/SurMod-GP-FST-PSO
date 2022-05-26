# Combining Genetic Programming and Particle Swarm Optimization to simplify rugged landscapes exploration

Python implementation for paper "Combining Genetic Programming and Particle Swarm Optimization to simplify rugged landscapes exploration", Gloria Pietropolli, Giuliamaria Menara, Mauro Castelli, 2022.

### Abstract
Most real-world optimization problems are difficult to be solved with traditional statistical techniques as well as with metaheuristics. The main difficulty is related to the existence of a considerable number of local optima, which may result in the premature convergence of the optimization process.
To address this problem, we propose a novel heuristic method to construct a smooth surrogate model of the original function. The surrogate function is easier to optimize but maintains a fundamental property of the original rugged fitness landscape: the location of the global optimum.
To create such a surrogate model, we consider a linear genetic programming approach enhanced by a self-tuning fitness function.
The proposed algorithm, called \emph{GP-FST-PSO Surrogate Model}, achieves satisfactory results concerning both the search for the global optimum and the production of a visual approximation of the original benchmark function (in the 2-dimensional case).

## Instructions

Code runs with python 3.8.5 and Julia 1.4.1 on Ubuntu 20.04.
To run the code, enter the following command:

```bash
python main.py 
```
that will return the fitness results for the 30 runs performed for the selected benchmark function and save them in the correspondent folder.

The script automatically perform the experiments for all the considered benchmark problems, that are: 
- _Ackley_
- _Alpine_
- _Griewank_
- _Michalewic_
- _Rastring_
- _Rosenbrock_
- _Vincent_
- _Xin-She Yang n.2_
