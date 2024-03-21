'''
Find distinct elements(GFG)

Given a N x N matrix M. Write a program to find count of all the distinct elements common to all rows of the matrix. Print count of such elements.

Example 1:

Input: 
N = 4
M = {{2, 1, 4, 3},
     {1, 2, 3, 2},
     {3, 6, 2, 3},
     {5, 2, 5, 3}}
Output: 
2
Explaination: Only 2 and 3 are common in all rows.
'''

class Solution:
    def distinct(self, M, N):
        if N==1:
            return len(M[0])
        for i in range(1,N):
            if i==1:
                set1=set(M[i]).intersection(M[i-1])
            else:
                set1=set1.intersection(M[i])
        return len(set1)
