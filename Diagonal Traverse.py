'''Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]'''

import numpy as np

class Solution:
    def findDiagonalOrder(self, mat):
        if type(mat[0])==int:
            return mat
        
        n=len(mat)
        m=len(mat[0])
        if m==1:
            return np.ravel(mat)
        
        if n==m:
            length=2*n-1
        else:
            length=2*max(n,m)
            
        
        row=0
        col=0
        
        list2=[]
        
        for i in range(m):
            list1=[]
            if i<=m:
                while row>=0 and row<=n-1 and col>=0 and col<=m-1:
                    list1.append(mat[row][col])
                    if row==n-1 or col==0:
                        break
                    row+=1
                    col-=1
                    
                row=0
                col=i+1
            
            if i%2==0:
                list2.extend(list1[::-1])
            else:
                list2.extend(list1)
        row=1
        col=m-1
        
        for i in range(m,length):
            list1=[]
            while row>=0 and row<=n-1 and col>=0 and col<=m-1:
                list1.append(mat[row][col])
                if row==n-1 or col==0:
                    break
                    
                row+=1
                col-=1
                    
            row=i-m+2
            col=m-1
            
            if i%2==0:
                list2.extend(list1[::-1])
            else:
                list2.extend(list1)
            
            
        
             
        return list2
