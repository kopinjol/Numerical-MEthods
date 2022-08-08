import numpy as np
import matplotlib as mpl
import seaborn as sns
import OdeSolver as Ode

def main():
    b = Ode.data(lambda x,y : -y + 2*x)
    X, Y = b.store()
    print(X)
    YY = b.solve_rk(X, Y)
    print(YY)
    b.plot()

if __name__=='__main__':
    main()
