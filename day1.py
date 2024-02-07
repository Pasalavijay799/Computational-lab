a1=2
b1=3
print(a1+b1)
a1=input("enter a number")
b1=input("enter a number")
print(a+b)
#dot produt
a=[2,3,4]
b=[5,0,7]
new=0
for i in range(3):
	new+=(a[i]*b[i])
print(new)
# divide the numbers
a=input("enter the number")
b=input("enter the number")
acopy = a.replace(".", "")
bcopy = b.replace(".", "")

if ((a.isnumeric() or acopy.isnumeric()) and (b.isnumeric() or bcopy.isnumeric()) ):
	print(float(a) / float(b))
else:
	print("Given data is wrong")
#determinent of matrix
matrix =[[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        inp = int(input("Enter a number: "))
        matrix[i][j] = inp
print()

# determinent
det=0
for j in range(3):
    det = det + matrix[0][j]*((matrix[(1)%3][(j+1)%3] * matrix[(2)%3][(j+2)%3]) - (matrix[(1)%3][(j+2)%3] * matrix[(2)%3][(j+1)%3]))


print("given matrix")
for i in range(3):
    for j in range(3):
        print(matrix[i][j],end=" ")
    print()

print("The determinent of the matrix is: %d"%det)

