'''
The Light Problem (GFG)
There are N office cubicles placed in a straight line, each with a bright bulb. Each light bulb can brighten K rooms on either side of it (also the one in which the light bulb itself is), but all the cubicles don't have a bulb.
You are given an array A which gives the information about the location of the bulbs. If A[i] is equal to 1, then the cubicle has a light bulb, else if A[i] is 0, then the cubicle doesn't have a bulb. You need to find out whether all the cubicles are bright or not.

Example 1:

Input: N = 4, K = 3
A = {0, 1, 0, 1}
Output: 1
Explaination: The first cubicle can be 
brightened by 2nd cubicle. The third 
cubicle can be brightened by 4th cubicle.
'''
class Solution:
    def isBrightened(self, N, K, A):
        
        for i in range(N):
            if A[i]==1:
                j=i-1
                count=K
                while count>0 and j>=0:
                    if A[j]==0:
                        A[j]='T'
                    count-=1
                    j-=1
                    
                j=i+1
                count=K
                while count>0 and j<N:
                    if A[j]==0:
                        A[j]='T'
                    count-=1
                    j+=1
        for i in range(N):
            if A[i]=='T':
                A[i]=1
        total=sum(A)
        
        if total<N:
            return 0
        return 1
