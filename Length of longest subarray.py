'''
Given an array A[] of size N, return length of the longest subarray of non- negative integers.

Note: Subarray here means a continuous part of the array.
 

Example 1:

Input : 
N = 9
A[] = {2, 3, 4, -1, -2, 1, 5, 6, 3}
Output : 
4
Explanation :
The subarray [ 1, 5, 6, 3] has longest length 4 and
contains no negative integers
'''

def longestSubarry( arr, N):
    count=0
    maximum=0
    
    for i in range(N):
        if arr[i]>=0:
            count+=1
        else:
            maximum=max(maximum,count)
            count=0
    if count>0:
        maximum=max(maximum,count)
    return maximum
