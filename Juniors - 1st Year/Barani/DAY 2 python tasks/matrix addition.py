print("***MATRIX ADDITION***")
MAX = 20
def printMatrix(matrix, rowSize, colSize) :  
    for i in range(rowSize) :  
        for j in range(colSize) :  
            print(matrix[i][j], end = " ") 
        print()
        
def matrix_addition(matrix1,row1,col1,matrix2):
    result = [[matrix1[i][j] + matrix2[i][j]  for j in range(col1)] for i in range(row1)]
    printMatrix(result,row1,col1)
    
if __name__ == '__main__':
    row1 = int(input("Enter no. of rows needed in matrix1   ="))
    col1 = int(input("Enter no. of columns needed in matrix1="))
    row2 = int(input("Enter no. of rows needed in matrix2   ="))
    col2 = int(input("Enter no. of columns needed in matrix2="))
    
    matrix1 = [[0 for i in range(MAX)]
                  for j in range(MAX)]
    matrix2 = [[0 for i in range(MAX)]
                  for j in range(MAX)]
    for i in range(row1) :  
        for j in range(col1) :  
            matrix1[i][j] = int(input("matrix1["+str(i)+"]["+str(j)+"]: "))
    printMatrix(matrix1,row1,col1)
    for i in range(row2) :  
        for j in range(col2) :  
            matrix2[i][j] = int(input("matrix2["+str(i)+"]["+str(j)+"]: "))
    printMatrix(matrix2,row2,col2)
    
    if row1!=row2 or col1!=col2:
        print("CANNOT PERFORM MATRIX ADDITON")
    else:
        matrix_addition(matrix1,row1,col1,matrix2)
