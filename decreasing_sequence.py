'''
Decreasing Sequence

A sequence a[0], a[1], …, a[N-1] is called decreasing if a[i] >= a[i+1] for each i: 0 <= i < N-1. You are given a sequence of numbers a[0], a[1],…, a[N-1] and a positive integer K. In each 'operation',
you may subtract K from any element of the sequence. You are required to find the minimum number of 'operations' to make the given sequence decreasing.
Note: As the answer can be large return your answer modulo 109+7.

Example 1:

Input:
N = 4, K = 5
A[] = {1, 1, 2, 3}
Output:
3
Explanation:
One operation is required to change a[2] = 2
into -3 and two opertations are required to
change a[3] = 3 into -7. The resulting
sequence will be 1 1 -3 -7. Hence, in
total 3 operations are required.
'''
import math

def minMoves( arr, n, k):
    count=0
    
    for i in range(1,n):
        if arr[i]>arr[i-1]:
            diff=arr[i]-arr[i-1]
            
            times=math.ceil(diff/k)
            count+=times
            arr[i]=arr[i]-times*k
            
    return count%(10**9+7)
