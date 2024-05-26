'''
Sum of upper and lower triangles

Given a square matrix of size N*N, print the sum of upper and lower triangular elements. Upper Triangle consists of elements on the diagonal and above it. The lower triangle consists of elements on the diagonal and below it. 

Example 1:

Input:
N = 3 
mat[][] = {{6, 5, 4},
           {1, 2, 5}
           {7, 9, 7}}
Output: 
29 32
Explanation:
The given matrix is
6 5 4
1 2 5
7 9 7
The elements of upper triangle are
6 5 4
  2 5
    7
Sum of these elements is 6+5+4+2+5+7=29.
The elements of lower triangle are
6
1 2
7 9 7
Sum of these elements is 6+1+2+7+9+7= 32.
'''

class Solution:
    
    #Function to return sum of upper and lower triangles of a matrix.
    def sumTriangles(self,matrix, n):
        upper_sum=0
        lower_sum=0
        
        for i in range(n):
            for j in range(n):
                if j>i:
                    upper_sum+=matrix[i][j]
                elif j==i:
                    upper_sum+=matrix[i][j]
                    lower_sum+=matrix[i][j]
                else:
                    lower_sum+=matrix[i][j]
        
        return upper_sum,lower_sum
