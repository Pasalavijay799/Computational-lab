import numpy as np
t=np.arange(0,1,0.01)
f=5
x=np.sin(2*np.pi*f*t)
f=open("sin.txt","w")
f.write(str(x))
f.close()
f1=open("sin.txt","r")
y=f1.read()
print(y)
f1.close()
