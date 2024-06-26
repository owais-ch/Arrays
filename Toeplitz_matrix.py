'''
Toeplitz Matrix (GFG)

A Toeplitz (or diagonal-constant) matrix is a matrix in which each descending diagonal from left to right is constant, i.e., all elements in a diagonal are the same. Given a rectangular matrix mat, your task is to complete the function isToeplitz which returns 1 if the matrix is Toeplitz otherwise, it returns 0.

Examples:

Input:
mat = [[6, 7, 8],
       [4, 6, 7],
       [1, 4, 6]]
Output: 1
Explanation: The test case represents a 3x3 matrix
 6 7 8 
 4 6 7 
 1 4 6
Output: 1(True) as values in all downward diagonals from left to right contain the same elements.
'''

def isToepliz(mat):
    num_rows=len(mat)
    num_cols=len(mat[0])
    
    for i in range(num_rows):
        for j in range(num_cols):
            if i+1<num_rows and j+1<num_cols and mat[i][j]!=mat[i+1][j+1]:
                return False
                
    return True
