# Syntesizing harmonically rich Auditory Distortion Products: Experiments

This repository has some of the main experiments used to understand the theory and optimization behind the algorithm published in [CITA](link acá). A brief description of each experiment can be found here.

## Experiment 1. Finding a Gröbner basis

The first experiment implements a way of finding a Gröbner basis for the system considering *n* equations.

## Experiment 2. Iterations amount

The second experiment implements a solver for the system using Newton-Raphson method. Such solver does not work for every target since the system can not be solved in general, so in this experiment this method is used with mainly two objectives:
1. Find out and approximation of the measure of the set of unsolvable targets.
2. Find out how many iterations are necessary for the algorithm to converge provided that it actually converges. 

## Experiment 3. Proof of conjecture

In this experiment we try to prove the conjecture

*Conjecture 1. For every target there is another target that sounds the same such that is solvable*

## Experiment 4. Algorithm Optimization

In this experiment several combination of techniques are used to find out the best way to implement the solution.
