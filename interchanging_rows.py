'''
Interchanging the rows of a Matrix (GFG)

Given a matrix of dimensions n1 x m1. Interchange its rows in-place such that the first row will become the last row and so on. 

Example 1:

Input:
n1 = 4, m1 = 4
matrix[][] = {{1, 2, 3, 4},
             {5, 6, 7, 8},
             {9, 10, 11, 12},
             {13, 14, 15,16}}
Output: 
13 14 15 16 9 10 11 12 5 6 7 8 1 2 3 4
Explanation:
Matrix after exchanging rows:
13 14 15 16
 9 10 11 12
 5  6  7  8
 1  2  3  4
Note: Output is printed row-wise linearly. 
'''
class Solution:
    #Function to interchange the rows of a matrix.
    def interchangeRows(self,matrix):
        num_rows=len(matrix)
        num_cols=len(matrix[0])
        
        i,j=0,num_rows-1
        
        while i<j:
            matrix[i],matrix[j]=matrix[j],matrix[i]
            i+=1
            j-=1
            
        return matrix
