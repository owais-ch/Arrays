'''
Addition of submatrix (GFG)

Given a matrix Arr of size N x M. You are given position of submatrix as X1, Y1 and X2, Y2 inside the matrix. Find the sum of all elements inside that submatrix. Here X1, Y1, X2, Y2 are 1-based.

Example 1:

Input: 
N = 5 , M = 6
Arr[][] = {{1, 2, 3, 4, 5, 6},
           {7, 8, 9, 10, 11, 12},
           {13, 14, 15, 16, 17, 18},
           {19, 20, 21, 22, 23, 24},
           {25, 26, 27, 28, 29, 30}}
X1=3, Y1=4, X2=4, Y2=5
Output: 78
Explanation: Sum from cell starting at
position (3, 4) (1-based indexing) and 
ending at (4, 5) is 78 (16+17+22+23).
'''

import numpy as np

class Solution:
	def subMatrixSum(self,arr, n, m, x1, y1, x2, y2):
	    return np.sum(np.array(arr)[x1-1:x2,y1-1:y2])
