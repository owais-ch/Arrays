'''
Reversing the columns of a Matrix

Given a matrix of dimensions n1 x m1. Reverse its columns in-place such that the last column will become the first column and so on. 

Example 1:

Input:
n1 = 4, m1 = 3
matrix[][] = {{ 1,  2,  3},
              { 5,  6,  7},
              {11, 10,  9},
              {13, 14, 15}}
Output: 3 2 1 7 6 5 9 10 11 15 14 13
Explanation:
Array after exchanging columns:
3 2 1
7 6 5
9 10 11
15 14 13
'''

class Solution:
    #Function to reverse the columns of a matrix.
    def reverseCol(self,matrix):
        num_rows=len(matrix)
        num_cols=len(matrix[0])
        
        for p in range(num_rows):
            i,j=0,num_cols-1
            while i<j:
                matrix[p][i],matrix[p][j]=matrix[p][j],matrix[p][i]
                i+=1
                j-=1
                
        return matrix
