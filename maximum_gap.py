'''
Maximum Gap (GFG)
Given an unsorted array Arr of length N. Your task is to find the maximum difference between the successive elements in its sorted form.
Return 0 if the array contains less than 2 elements.
'''
import bisect
import math

class Solution:
    def maxSortedAdjacentDiff(self,arr, n):
        if n<2:
            return 0
        stack=[]
        arr=list(set(arr))
        n=len(arr)
        minimum=math.inf
        maximum=-math.inf
        
        for i in range(n):
            if i==0:
                stack.append(arr[i])
                maximum=arr[i]
                minimum=arr[i]
            else:
                if arr[i]>=maximum:
                    stack.append(arr[i])
                    maximum=arr[i]
                elif arr[i]<=minimum:
                    stack[0:0]=[arr[i]]
                    minimum=arr[i]
                else:
                    bisect.insort(stack,arr[i])
        
        max_diff=-math.inf
        
        for i in range(1,n):
            if stack[i]-stack[i-1]>max_diff:
                max_diff=stack[i]-stack[i-1]
                
        return max_diff
