# Copyright Kopinjol Baishya
# contact: kopinjol@gmail.com

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class data:
    def __init__(self, function, filename=' '):
        self.filename = input("Enter data-file name. \n")
        self.function = function
    def store(self):
        fh = open(self.filename, "r")
        print("File opened")
        i = 0
        w = []
        l = fh.readlines()
        for line in l:
            w.append(line.split(' ', 1))
            #print(w[i])
            i = i+1
        #print(l)
        print(w[0][0])
        fh.close()
        #X = np.arange(11)
        #Y = np.arange(11)
        #ww = []
        X = []; Y = []
        print("X:= \n")
        print(X)
        print(self.function)
        for i in range(0,10):
            X.append(w[i][0])
            Y.append(w[i][1])
        return(X, Y)

    def solve(self, X,Y):
        self.xx = np.array(X, dtype=float)
        yi = np.array(Y, dtype=float)
        yf = np.zeros(12, dtype=float)
        self.yf = yi
        print(self.function(1.0,2.0))
        for j in range(1,10):
            #print(j)
            self.yf[j] = float(self.yf[j-1]) + self.function(float(self.xx[j]),float(self.yf[j]))

        return(yf) 
    
    
    def plot(self):
        sns.set()
        plt.plot(self.xx, self.yf)
        plt.show()
        
    
        
