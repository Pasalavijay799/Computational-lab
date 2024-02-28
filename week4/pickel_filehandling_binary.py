import pickle as pk 
import numpy as np
t=np.arange(0,1,0.01)
f=5
x=np.sin(2*np.pi*f*t)
f=open("sine_pic","wb")
pk.dump(x,f)
f.close()
f2=open("sine_pic","rb")
y=pk.load(f2)
print(y)
