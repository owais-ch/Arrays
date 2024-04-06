'''
Partition Point in the Array
Given an unsorted array of integers. Find an element such that all the elements to its left are smaller and to its right are greater. Print -1 if no such element exists. Note that there can be more than one such element.
In that case print the first such number occurring in the array.

Example 1:

Input: N = 7, arr[] = {4, 3, 2, 5, 8, 6, 7} 
Output: 5
Explanation: To the left of element 5 
every element is smaller to it and to 
the right of element 5 every element 
is greater to it.  
'''
class Solution:
    def FindElement(self,arr, N):
        left=[0]*n
        right=[0]*n
        
        i,j=0,n-1
        
        while i<n and j>=0:
            if i==0:
                left[i]=arr[i]
                left_max=arr[i]
            else:
                if arr[i]>=left_max:
                    left_max=arr[i]
                    left[i]=left_max
                else:
                    left[i]=left_max
                    
            if j==n-1:
                right[j]=arr[j]
                right_max=arr[j]
            else:
                if arr[j]<=right_max:
                    right_max=arr[j]
                    right[j]=right_max
                else:
                    right[j]=right_max
            i+=1
            j-=1
        
        for i in range(n):
            if i==0:
                if right[i+1]>arr[i]:
                    return arr[i]
            elif i==n-1:
                if left[i-1]<arr[i]:
                    return arr[i]
            elif left[i-1]<arr[i]<right[i+1]:
                return arr[i]
        return -1

