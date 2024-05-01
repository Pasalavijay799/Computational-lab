import matplotlib.pyplot as py
x=[1,2,3,4,5]
y=[1,32,4,9,8]
lx=len(x)
ly=len(y)
ki=[]
z = []
sum=[]
for k in range(0, ly): 
    summation = 0
    for n in range(len(x)):
        if n+k < len(y):
            summation += x[n] * y[n+k]
    sum.append(summation)
    ki.append(k)
    z.append(summation)
print(z)
py.plot(ki,z)
py.show()
