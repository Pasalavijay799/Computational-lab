import numpy as np
t=np.arange(0,1,0.01)
f=5
x=np.sin(2*np.pi*f*t)
f=open("sine_bin","wb")
f.write(x)
f.close()
f1=open("sine_bin","rb")
y=f1.read()
print(y)
f1.close()
