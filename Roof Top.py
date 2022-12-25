'''You are given heights of consecutive buildings. You can move from the roof of a building to the roof of next adjacent building. You need to find the maximum number 
of consecutive steps you can put forward such that you gain an increase in altitude with each step.

Example 1:

Input:
N = 5
A[] = {1,2,2,3,2}
Output: 1
Explanation: 1, 2 or 2, 3 are the only consecutive 
buildings with increasing heights thus maximum number
of consecutive steps with increase in gain in altitude
would be 1 in both cases.
'''

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self,A, N):
        maximum=0
        count=0
        
        for i in range(N-1):
            if A[i]<A[i+1]:
                count+=1
                #print(count)
            else:
                maximum=max(maximum,count)
                count=0
        maximum=max(maximum,count)        
        return maximum
