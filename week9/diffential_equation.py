import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def return_dydt(y,t):
    dydt=((1-y)/(1.95-y)) - (y/(0.05+y))
    return dydt
y0=[0,1,2]
t=np.linspace(0,5)
y=odeint(return_dydt,y0,t)
plt.plot(t,y)
plt.xlabel("Time")
plt.ylabel("Y")
plt.show()
