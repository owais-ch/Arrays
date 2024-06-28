'''
The Palindrome Pattern (GFG)

Given a two-dimensional integer array arr of dimensions n x n, consisting solely of zeros and ones, identify the row or column (using 0-based indexing) where all elements form a palindrome. If multiple palindromes are identified, prioritize the palindromes found in rows over those in columns. Within rows or columns, the palindrome with the smaller index takes precedence. The result should be represented by the index followed by either 'R' or 'C', indicating whether the palindrome was located in a row or column. The output should be space-separated. If no palindrome is found, return the string -1.

Examples:

Input: 
arr[][] =  [[1, 0, 0], 
           [0, 1, 0],
           [1, 1, 0]]
Output: 1 R
Explanation: In the first test case, 0-1-0 is a palindrome 
occuring in a row having index 1.
'''

class Solution:
    def pattern (self, arr):
        num_rows=len(arr)
        num_cols=len(arr[0])
        
        for i in range(num_rows):
            p,q=0,num_cols-1
            while p<q:
                if arr[i][p]==arr[i][q]:
                    p+=1
                    q-=1
                else:
                    break
            if p>=q:
                return str(i)+' R'
        
        for j in range(num_cols):
            p,q=0,num_rows-1
            while p<q:
                if arr[p][j]==arr[q][j]:
                    p+=1
                    q-=1
                else:
                    break
            if p>=q:
                return str(j)+' C'
                
        return -1
