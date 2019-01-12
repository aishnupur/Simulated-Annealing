#importing libraries
import random
import numpy as np
#initialization
p=0
w=[]
x=[]
y=[]
z=[]
#function for finding the probability
def prob(x1, x2, T): 	
    ex1 = np.subtract((x1*x1), (15*x1)) +54 	
    ex2 = np.subtract((x2*x2), (15*x2)) +54 
    q=(ex1-ex2)/T
    p=np.exp(q)
    return p
#performing iterations for finding the optimum value of x
for T in range(100, 0, -10):
    for k in range(5):
        x1 = random.randint(0,99)
        x2 = random.randint(0,99)
        p = prob(x1, x2, T)
        if(p<1.0):
            print("Rejects: x1=", x1 , ", X2=", x2, ",P=", p, ", T=", T)
        if(p>1.0):
            print("Accepts: x1=", x1, ", X2=", x2, ", P=", p, ", T=", T)	
            w.append(x1)
            x.append(x2)
    y.append(T)
    z.append(p)
    print("-----------------------", T,"----------------------------")
    p=0
