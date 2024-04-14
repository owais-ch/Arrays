'''
Leaders in an Array (GFG)
Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 

Example 1:

Input:
n = 6
A[] = {16,17,4,3,5,2}
Output: 17 5 2
Explanation: The first leader is 17 
as it is greater than all the elements
to its right.  Similarly, the next 
leader is 5. The right most element 
is always a leader so it is also 
included.
'''

class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        list1=[]
        
        for i in range(-1,-N-1,-1):
            if i==-1:
                list1.append(A[i])
                maximum=A[i]
            else:
                if A[i]>=maximum:
                    maximum=A[i]
                    list1.append(maximum)
                    
        return list1[::-1]
