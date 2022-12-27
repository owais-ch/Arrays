'''
Given an array of integers, count number of subarrays (of size more than one) that are strictly increasing. 
Expected Time Complexity : O(n) 
Expected Extra Space: O(1)

Examples:

Input: arr[] = {1, 4, 3}
Output: 1
There is only one subarray {1, 4}

Input: arr[] = {1, 2, 3, 4}
Output: 6
There are 6 subarrays {1, 2}, {1, 2, 3}, {1, 2, 3, 4}
                      {2, 3}, {2, 3, 4} and {3, 4}
'''

def count_sub(arr):
    length=len(arr)
    total=0
    count=0
    for i in range(1,length):
        if arr[i]>arr[i-1]:
            count+=1
            if i==length-1:
                total+=(count*(count+1)//2)
        else:
            total+=(count*(count+1)//2)
            count=0
            
    return total
