'''
Given an array A of size n, the task is to check if the array can be sorted in increasing order, if the only operation allowed is swapping the adjacent elements if
they are of opposite parity. The operation can be done any number of times.

Examples:

Input : n = 4, A = [1, 6, 51, 16]
Output: YES
Explanation: Since 51 is odd and 16 is even, we will just swap them. The array now becomes [1, 6, 16, 51], which is sorted in increasing order.

Input: n = 4, A = [5, 5, 5, 5]
Output: YES
Explanation: The array is already sorted.
'''

def sort_parity(arr):
    length=len(arr)
    
    even_max=-9999
    odd_max=-9999
    
    for i in range(length):
        if arr[i]%2==0:
            if arr[i]<even_max:
                return False
            else:
                even_max=arr[i]
        else:
            if arr[i]<odd_max:
                return False
            else:
                odd_max=arr[i]
                
    return True
