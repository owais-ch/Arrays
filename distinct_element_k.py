'''
Maximum distinct elements after removing K elements
Given an array containing N elements. The task is to find the maximum number of distinct elements after removing K elements from the array.

Example 1:

Input : Arr[] = {5, 7, 5, 5, 1, 2, 2}, K = 3
Output : 4
Explanation:
Remove 2 occurrences of element 5 and 
1 occurrence of element 2.
'''

class Solution:
    def maxTripletSum (self, arr,  n, K) : 
        if K==n:
            return 0
        set1=set(arr)
        set_length=len(set1)
        
        diff_length=n-set_length
        
        if K<=diff_length:
            return set_length
        
        return set_length-(K-diff_length)
