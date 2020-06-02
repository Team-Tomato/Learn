print("***MATRIX MULTIPLICATION***)
MAX = 10
def PrintMatrix(Matrix,row,col):
    for i in range(row):
        for j in range(col):
            print(Matrix[i][j],end=" ")
        print()
def Matrix_multiplication(matrix1,row1,col1,matrix2,row2,col2):
    if(row2==col1):
        result = [[0 for i in range(MAX)]for j in range (MAX)]
        for i in range(row1):
            for j in range(col2):
                result[i][j] = 0
                for k in range(row2):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        print("Resultant Matrix:")
        PrintMatrix(result,row1,col2)
    else:
        print("Cannot perform matix multiplication."
              "Since Row of Matrix1(",row1,") is not equal to Column of the Matrix2(",col2,")")
if __name__ == "__main__":
    Matrix1 = [[0 for i in range(MAX)]for j in range(MAX)] 
    Matrix2 = [[0 for i in range(MAX)]for j in range(MAX)] 
    row1 = int(input("Enter the number of rows of First Matrix: ")) 
    col1 = int(input("Enter the number of columns of First Matrix: "))  
    print("Enter the elements of First Matrix: ")  
    for i in range(row1) :  
        for j in range(col1) :  
            Matrix1[i][j] = int(input("Matrix1[" + str(i) +
                                "][" + str(j) + "]: ")) 
    print("First Matrix: ") 
    PrintMatrix(Matrix1, row1, col1) 

    row2 = int(input("Enter the number of rows of Second Matrix: "))  
    col2 = int(input("Enter the number of columns of Second Matrix: "))  
    print("Enter the elements of Second Matrix: ");  
    for i in range(row2) :  
        for j in range(col2) : 
            Matrix2[i][j] = int(input("Matrix2[" + str(i) +
                                "][" + str(j) + "]: "))  
    print("Second Matrix: ") 
    PrintMatrix(Matrix2, row2, col2)

    Matrix_multiplication(Matrix1, row1, col1, Matrix2, row2, col2)
