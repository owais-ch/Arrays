'''
Boundary traversal of matrix
You are given a matrix of dimensions n x m. The task is to perform boundary traversal on the matrix in a clockwise manner starting from the first row of the matrix.

Example 1:

Input:
n = 4, m = 4
matrix[][] = {{1, 2, 3, 4},
         {5, 6, 7, 8},
         {9, 10, 11, 12},
         {13, 14, 15,16}}
Output: 1 2 3 4 8 12 16 15 14 13 9 5
Explanation:
The matrix is:
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16
The boundary traversal is:
1 2 3 4 8 12 16 15 14 13 9 5
'''

def BoundaryTraversal(self,matrix, n, m):
        list1=[]
        if n==1:
            list1.extend(matrix[0])
            return list1
        elif m==1:
            for i in range(n):
                list1.append(matrix[i][0])
            return list1
        
        
        i,j=0,0
        
        direction="right"
        
        while i<n and j<m:
            if direction=="right" and j<m-1:
                list1.append(matrix[i][j])
                j+=1
            elif direction=="right" and j==m-1:
                list1.append(matrix[i][j])
                direction="down"
                i+=1
            elif direction=="down" and i<n-1:
                list1.append(matrix[i][j])
                direction="down"
                i+=1
            elif direction=="down" and i==n-1:
                list1.append(matrix[i][j])
                direction="left"
                j-=1
            elif direction=="left" and j>0:
                list1.append(matrix[i][j])
                j-=1
            elif direction=="left" and j==0:
                list1.append(matrix[i][j])
                direction="up"
                i-=1 
            elif direction=="up" and i>0:
                list1.append(matrix[i][j])
                direction="up"
                i-=1
            elif direction=="up" and i==0:
                break
            
            if i==0 and j==0:
                break
            
        return list1
