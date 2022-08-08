# Numerical-MEthods
Some numerical method codes I wrote to teach. They are written in Python 3 in Jupyter notebooks. The two files EulerOde.py and driver.py consists of a very simple 1st order ODE solver using the Euler method. EulerOde.py is a module that has to be imported into any function using it. In this case the script driver.py imports the Module. One can specify the ODE by specifying the lambda function in the call to the constructor of data class. The plot method plots the calculated solution.

OdeSolver.py is a tiny class that can solve a first order differential equation with Euler and RK-2 method. After reading in the data with the  store method, call whichever method you want to use, solve_euler for euler and solve_rk for RK-2 method.
