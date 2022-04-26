'''Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        
        row=0
        col=m-1
        
        while row<=n-1 and col>=0:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                col=col-1
            else:
                row=row+1
                
        return False
