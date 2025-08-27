#Se usa para sumar valores de distintas matrices.
matrix1 = [[1,2,3],[7,8,9],[13,14,15]]
matrix2 = [[4,5,6],[10,11,12],[16,17,18]]

matrix3 = [[1,2,3],[7,8,9],[13,14,15]]

#Suma de valores de distintas matrices.
"""matrix3[0][0]=matrix1[0][0]+matrix2[0][0]"""

for rowPosition, value in enumerate(matrix1):
    for columPosition, value2 in enumerate(value):
        matrix3[rowPosition][columPosition]=value2+matrix2[rowPosition][columPosition]+matrix2[rowPosition][columPosition]
print(matrix3)


