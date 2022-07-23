# Copyright Kopinjol Baishya
# contact: kopinjol@gmail.com

import EulerOde as Eul

#def fn(x):
#    z = -y + 2*x
#    return(z)
    
b = Eul.data(lambda x,y: -y + 2*x)
X, Y = b.store()
print(X)
YY = b.solve(X, Y)
print(YY)
b.plot()
