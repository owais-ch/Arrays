'''
Search in a row-column sorted Matrix (GFG)

Given a matrix of size n x m, where every row and column is sorted in increasing order, and a number x. Find whether element x is present in the matrix or not.

Example 1:

Input:
n = 3, m = 3, x = 62
matrix[][] = {{ 3, 30, 38},
              {36, 43, 60},
              {40, 51, 69}}
Output: 0
Explanation:
62 is not present in the matrix, 
so output is 0.
'''

class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def search(self,matrix, n, m, x): 
        count=0
        low_limit_row=-1
        high_limit_row=-1
        
        def binary_search(arr,low,high,x):
            
            while low<=high:
                mid=(low+high)//2
                if arr[mid]==x:
                    return True
                elif arr[mid]>x:
                    high=mid-1
                else:
                    low=mid+1
                    
            return False
            
        for i in range(n):
            if binary_search(matrix[i],0,m-1,x)==True:
                return True
                
        return False
