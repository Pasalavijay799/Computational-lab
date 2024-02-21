#add numbers......................................................
a1=2
b1=3
print(a1+b1)
a1=input("enter a number")
b1=input("enter a number")
print(a1+b1)
#dot produt........................................................
n=int(input("enter the how many number want to add : "))
a=[]
b=[]
for i in range(n):
	tem=int(input("enter the number vector1"))
	temp2=int(input("enter the number vector2"))
	a.append(tem)
	b.append(temp2)
new=0
print(a)
print(b)
for i in range(3):
	new+=(a[i]*b[i])
print("the dot product above vectors: ",new)
# divide the numbers.................................................................
def check(a):
	if(a != "" and a[0] == '-'):
		return 1
	else:
		return 0	


a=input("enter the number")
b=input("enter the number")
acopy = a.replace(".", "")
bcopy = b.replace(".", "")
if (check(a)):
	acopy = acopy.replace("-", "")
if (check(b)):
	bcopy = bcopy.replace("-", "") 

if ((a.isnumeric() or acopy.isnumeric()) and (b.isnumeric() or bcopy.isnumeric()) ):
	print(float(a) / float(b))
else:
	print(" data is not enterd correctly")


#determinent of matrix...............................................................................
matrix =[[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        inp = int(input("Enter a number: "))
        matrix[i][j] = inp
print()

# determinent..........................................
det=0
for j in range(3):
    det = det + matrix[0][j]*((matrix[(1)%3][(j+1)%3] * matrix[(2)%3][(j+2)%3]) - (matrix[(1)%3][(j+2)%3] * matrix[(2)%3][(j+1)%3]))


print("given matrix")
for i in range(3):
    for j in range(3):
        print(matrix[i][j],end=" ")
    print()

print("The determinent of the matrix is: %d"%det)

