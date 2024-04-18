'''
Sum pair closest to X (GFG)

Given a sorted array arr[] of size N and a number X, find a pair in array whose sum is closest to X.

Note: If there are multiple such pairs return the pair with maximum absolute difference.

Example 1:

Input:
N = 6, X = 54
arr[] = {10, 22, 28, 29, 30, 40}
Output: 22 30
Explanation: As 22 + 30 = 52 is closest to 54.
'''

import math

class Solution:
    def sumClosest(self, arr, x):
        minimum=math.inf
        
        i,j=0,n-1
        
        while i<j:
            if arr[i]+arr[j]==x:
                if abs(arr[i]+arr[j]-x)<minimum:
                    minimum=abs(arr[i]+arr[j]-x)
                    list1=[arr[i],arr[j]]
                elif abs(arr[i]+arr[j]-x)==minimum:
                    if abs(arr[i]-arr[j])>abs(list1[0]-list1[1]):
                        minimum=abs(arr[i]+arr[j]-x)
                        list1=[arr[i],arr[j]]
                i+=1
                j-=1
            elif arr[i]+arr[j]>x:
                if abs(arr[i]+arr[j]-x)<minimum:
                    minimum=abs(arr[i]+arr[j]-x)
                    list1=[arr[i],arr[j]]
                elif abs(arr[i]+arr[j]-x)==minimum:
                    if abs(arr[i]-arr[j])>abs(list1[0]-list1[1]):
                        minimum=abs(arr[i]+arr[j]-x)
                        list1=[arr[i],arr[j]]
                j-=1
            elif arr[i]+arr[j]<x:
                if abs(arr[i]+arr[j]-x)<minimum:
                    minimum=abs(arr[i]+arr[j]-x)
                    list1=[arr[i],arr[j]]
                elif abs(arr[i]+arr[j]-x)==minimum:
                    if abs(arr[i]-arr[j])>abs(list1[0]-list1[1]):
                        minimum=abs(arr[i]+arr[j]-x)
                        list1=[arr[i],arr[j]]
                i+=1
                
        return list1
