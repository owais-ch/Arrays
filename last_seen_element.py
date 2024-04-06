'''
Last seen array element
Given an array arr of N integers that might contain duplicates, find the element whose last appearance is earliest.
 
Example 1:

Input : arr[] = {10, 30, 20, 10, 20}
Output : 30
Explanation:
Below are indexes of last
appearances of all elements (0 based
indexes). 10 last occurs at index 3
30 last occurs at index 1. 20 last
occurs at index 4 The element whose
last appearance earliest is 30.
'''

import math

class Solution:
      
    def firstNonRepeating(self, arr, n): 
        dict1=dict()
        
        for i in range(n):
            if arr[i] not in dict1:
                dict1[arr[i]]=i
            else:
                dict1[arr[i]]=i
        
        maximum=math.inf
        
        for i in dict1:
            if dict1[i]<maximum:
                maximum=dict1[i]
                value=i
                
        return value
