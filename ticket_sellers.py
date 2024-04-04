'''
Ticket sellers (GFG)

There are N ticket sellers where the ith ticket seller has A[i] tickets.

The price of a ticket is the number of tickets remaining with the ticket seller. They are allowed to sell at most K tickets. Find the maximum amount they can earn by selling K tickets.

The amount of tickets of each seller is provided in array A. Give the answer modulo 109 + 7.

Example 1:

Input: N = 5, K = 3
A = {4, 3, 6, 2, 4}
Output: 15
Explaination: Consider 0 based indexing. 
For first two turns the 2nd seller sells. 
For the third turn either 0th or 2nd 
seller can sell. So the total becomes 
6 + 5 + 4 = 15.
'''
import bisect

class Solution:
    def maxAmount(self, N, K, A):
        if N==1:
            for i in range(K):
                if i==0:
                    total=A[0]
                    A[0]=A[0]-1
                    if A[0]==0:
                        break
                else:
                    total+=A[0]
                    A[0]=A[0]-1
                    if A[0]==0:
                        break
            return total%(10**9+7)
        A=A[:N]    
        A.sort()
        
        total=0
        
        for i in range(K):
            if A[-1]>=A[-2]:
                total+=A[-1]
                A[-1]=A[-1]-1
            else:
                value=A.pop(-1)
                bisect.insort(A,value)
                total+=A[-1]
                if A[-1]==0:
                    break
                A[-1]=A[-1]-1
                
        return total%(10**9+7)
