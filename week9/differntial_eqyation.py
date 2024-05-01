import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
def return_dxdy(y,t):
    dxdy=13*np.exp(t)+y
    return dxdy
y0=[8,89]
t=np.linspace(0,5)
y=odeint(return_dxdy,y0,t)
plt.plot(t,y)
plt.xlabel("Time")
plt.ylabel("Y")
plt.show()

