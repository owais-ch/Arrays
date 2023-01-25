'''
Find all indices of Array having prefix sum greater than suffix sum

Given an array arr[] of N integers, the task is to divide find all the indices such that prefix sum (i.e. sum of elements in range [0, i)) is greater than the
suffix sum (elements in the range [i, N-1])

Examples: 

Input: arr = [10, -3, 4, 6]
Output: [1, 3]
Explanation: Consider index 1. Prefix sum = 10, suffix sum = 7, i.e. (10 > 7)
Consider index 3. Prefix sum = 11, suffix sum = 6, i.e(11 > 6)

Input: arr = [-2, -3, -4, 10]
Output: []
Explanation: There is no index such that prefix sum is greater than suffix sum.
'''

def count_indices(arr,n):
    lsum=0
    rsum=sum(arr)
    
    count=0
    list1=[]
    
    for i in range(n-1):
        lsum+=arr[i]
        rsum-=arr[i]
        if lsum>rsum:
            list1.append(i+1)
        
    return list1
