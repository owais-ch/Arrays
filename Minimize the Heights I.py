'''
Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by increasing or decreasing 
them by K only once.
Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.
Note: Assume that height of the tower can be negative.
'''

import numpy as np
import math

class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        arr=np.array(arr)
        minz=math.inf
        minimum=arr[0]
        maximum=arr[-1]
        minz=min(minz,maximum-minimum)
        
        arr=arr+k
        
        minimum=arr[0]
        maximum=arr[-1]
        minz=min(minz,maximum-minimum)
        
        right_max=-math.inf
        for i in range(-1,-n-1,-1):
            arr[i]=arr[i]-2*k
            right_max=max(right_max,arr[i])
            
            if arr[i]<minimum:
                minimum=arr[i]
            
                
            if i==-1:
                maximum=max(arr)
            elif i>-n:
                maximum=max(arr[i-1],right_max)       
            else:
                maximum=right_max
                
            minz=min(minz,maximum-minimum)
            
        return minz
