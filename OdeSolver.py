# Copyright Kopinjol Baishya
# contact: kopinjol@gmail.com

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class data:
    def __init__(self, function, filename=''):
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

    def solve_euler(self, X, Y):
        self.xx = np.array(X)
        yi = np.array(Y)
        yf = np.zeros(12)
        self.yf = yi
        print(self.function(1.0,2.0))
        for j in range(1,10):
            #print(j)
            self.yf[j] = float(self.yf[j-1]) + self.function(float(self.xx[j]),float(self.yf[j]))

        return(yf)

    def solve_rk(self, X, Y):
        self.xx = np.array(X)
        h = float(X[1]) - float(X[0])
        self.yf = np.zeros(len(Y))
        k1 = np.zeros(len(Y))
        k2 = np.zeros(len(Y))
        for i in range(0, len(Y)):
            k1[i] = h*self.function(float(X[i]),float(Y[i]))
            k2[i] = h*self.function(float(X[i]) + h/2, float(Y[i]) + float(k1[i])*(1/2))
            
        #k1 = h*self.function(X, Y)
        #k2 = h*self.function(X + h/2, Y + k1*(1/2))
        self.yf[0] = self.function(float(X[0]), float(Y[0]))

        for i in range(1, len(Y)):
            self.yf[i] = float(self.yf[i-1]) + float(k2[i-1])

        #print(yf)
        return list(self.yf)



    def plot(self):
        sns.set()
        plt.plot(self.xx, self.yf)
        plt.show()
