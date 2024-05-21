'''
Max and Second Max
Given an array arr[] of size N of positive integers which may have duplicates. The task is to find the maximum and second maximum from the array, and both of them should be different from each other,
so If no second max exists, then the second max will be -1.

Example 1:

Input:
N = 3
arr[] = {2,1,2}
Output: 2 1
Explanation: From the given array 
elements, 2 is the largest and 1 
is the second largest.
'''
class Solution:
    # Function to find largest and second largest element in the array
    def largestAndSecondLargest(self, n, arr):
        #arr=list(set(arr))
        #n=len(arr)
        
        first_maximum,second_maximum=-1,-1
        
        if arr[0]>arr[1]:
            first_maximum=arr[0]
            second_maximum=arr[1]
        elif arr[1]>arr[0]:
            first_maximum=arr[1]
            second_maximum=arr[0]
        else:
            first_maximum=arr[0]
            
        for i in range(2,n):
            if arr[i]>first_maximum:
                second_maximum=first_maximum
                first_maximum=arr[i]
            elif second_maximum!=-1 and arr[i]>second_maximum and arr[i]<first_maximum:
                second_maximum=arr[i]
            elif second_maximum==-1 and arr[i]<first_maximum:
                second_maximum=arr[i]
        return first_maximum,second_maximum
