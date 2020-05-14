print("***MATRIX MULTIPLICATION PROGRAM***")
MAX = 100 
def printMatrix(M, rowSize, colSize) :  
    for i in range(rowSize) :  
        for j in range(colSize) :  
            print(M[i][j], end = " ") 
        print()  
   
def multiplyMatrix(row1, col1, A,  
                   row2, col2, B) : 
    C = [[0 for i in range(MAX)]  
            for j in range(MAX)] 
    if (row2 == col1) : 
      for i in range(row1) : 
          for j in range(col2) : 
              C[i][j] = 0
              for k in range(row2) : 
                  C[i][j] += A[i][k] * B[k][j];  
      print("Resultant Matrix: ") 
      printMatrix(C, row1, col2)
    else:
        print("Multiplication of above two matrices is not Possible") 
        return 

if __name__ == "__main__" :   
    A = [[0 for i in range(MAX)]  
            for j in range(MAX)] 
    B = [[0 for i in range(MAX)]  
            for j in range(MAX)] 
    row1 = int(input("Enter the number of rows of First Matrix: ")) 
    col1 = int(input("Enter the number of columns of First Matrix: "))  
    print("Enter the elements of First Matrix: ");  
    for i in range(row1) :  
        for j in range(col1) :  
            A[i][j] = int(input("A[" + str(i) +
                                "][" + str(j) + "]: ")) 
    print("First Matrix: ") 
    printMatrix(A, row1, col1) 

    row2 = int(input("Enter the number of rows of Second Matrix: "))  
    col2 = int(input("Enter the number of columns of Second Matrix: "))  
    print("Enter the elements of Second Matrix: ");  
    for i in range(row2) :  
        for j in range(col2) : 
            B[i][j] = int(input("B[" + str(i) +
                                "][" + str(j) + "]: "))  
    print("Second Matrix: ") 
    printMatrix(B, row2, col2) 
    
    multiplyMatrix(row1, col1, A, row2, col2, B) 