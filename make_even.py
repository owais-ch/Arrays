'''
Given an array arr[] consisting of N positive integers, the task is to make all array elements even by replacing any pair of array elements with their sum.

Examples: 

Input: arr[] = {5, 6, 3, 7, 20}
Output: 3
Explanation: 
Operation 1: Replace arr[0] and arr[2] by their sum ( = 5 + 3 = 8) modifies arr[] to {8, 6, 8, 7, 20}.
Operation 2: Replace arr[2] and arr[3] by their sum ( = 7 + 8 = 15) modifies arr[] to {8, 6, 15, 15, 20}.
Operation 3: Replace arr[2] and arr[3] by their sum ( = 15 + 15 = 30) modifies arr[] to {8, 6, 30, 30, 20}.

Input: arr[] = {2, 4, 16, 8, 7, 9, 3, 1}
Output: 2
'''

def make_even(arr):
    length=len(arr)
    count=0
    
    for i in range(length):
        if arr[i]%2!=0:
            count+=1
    if count%2==0:
        return count//2
    return (count//2)+2
