'''
Surpasser Count

An element Y is said to be the surpasser of element X if it is a greater element on the right of X. ie, if X = arr[i] and Y = arr[j], i<j and Arr[i] < Arr[j]. 
Given an array of size N containing distinct integers, find the number of surpassers for each of its elements.


Example 1:

Input:
N = 5
Arr[] = {4, 5, 1, 2, 3}

Output: 1 0 2 1 0

Explanation: There are no elements greater 
than 3 at the right of 3. There is one 
element at right of 2 and greater than 2. 
There are 2 elements greater than 1 at the 
right of 1. And so on.
'''
import bisect
from collections import deque

class Solution:
    def findSurpasser(self, arr, n):
        stack=deque([])
        list1=[0]*n
        
        for i in range(n-1,-1,-1):
            if i==n-1:
                stack.append(arr[i])
                maximum=arr[i]
                minimum=arr[i]
                list1[i]=0
            elif arr[i]>maximum:
                maximum=arr[i]
                list1[i]=0
                stack.append(arr[i])
            elif arr[i]<minimum:
                minimum=arr[i]
                list1[i]=n-i-1
                stack.appendleft(arr[i])
            else:
                bisect.insort(stack,arr[i])
                indexz=bisect.bisect_left(stack,arr[i])
                length=len(stack)
                list1[i]=length-indexz-1
                
        return list1
