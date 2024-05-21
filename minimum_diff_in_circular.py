'''
Minimum adjacent difference in a circular array (GFG)

Given an array Arr of n integers arranged in a circular fashion. Your task is to find the minimum absolute difference between adjacent elements.

Example 1:

Input:
n = 7
Arr[] = {8,-8,9,-9,10,-11,12}
Output: 4
Explanation: The absolute difference 
between adjacent elements in the given 
array are as such: 16 17 18  19 21 23 4
(first and last). Among the calculated 
absolute difference the minimum is 4.
'''
import math
class Solution:
    #Complete this function
    #Function to find minimum adjacent difference in a circular array.
    def minAdjDiff(self,arr, n):
        minimum=math.inf
        
        for i in range(n-1):
            if abs(arr[i]-arr[i+1])<minimum:
                minimum=abs(arr[i]-arr[i+1])
                
        if abs(arr[0]-arr[-1])<minimum:
            minimum=abs(arr[0]-arr[-1])
            
        return minimum
