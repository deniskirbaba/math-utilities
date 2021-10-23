## Extrema of functions of several valiables ##

Purpose of the work: to learn how to find the extrema of functions of several variables by the analytical and numerical method.

Operating procedure:

1. Analytical method
 * find stationary points
 * for each point, obtain the Hessian matrix and check the sufficient condition for the extremum
 * if the sufficient condition is not met, check this point using the definition of an extremum
 * build a graph of this function by the program method and the line level. Mark stationary points

2. Numerical method
 * choose one extreme point if there are many
 * choose starting point
 * at each step: calculate the value of the function, the increment of the function and the gradient at the current point (x<sub>k</sub>, y<sub>k</sub>). Determine the next point (x<sub>k+1</sub>, y<sub>k+1</sub>) = (x<sub>k</sub>, y<sub>k</sub>) - a<sub>k</sub> * grad f (x<sub>k</sub>, y<sub>k</sub>), where the coefficient a<sub>k</sub> is responsible for the rate of step decrease.
  * think through reaching a breakpoint
  * result of the program: shutdown criterion; midpoint; function value; working hours; a picture (or video) displaying the results of each step; conclusion (comparison with the exact result)