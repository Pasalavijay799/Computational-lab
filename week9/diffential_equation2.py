import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def return_dydt(y,t):
    dydt=13-y*t
    return dydt
y0=[i for i in range(1,10)]
t=np.linspace(0,5)
y=odeint(return_dydt,y0,t)
plt.plot(t,y)
plt.xlabel("Time")
plt.ylabel("Y")
plt.show()
