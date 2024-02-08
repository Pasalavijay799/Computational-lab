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
