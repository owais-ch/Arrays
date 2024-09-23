'''
Problem 2: Convert Array Using Operations
You are given two arrays A and B of size n. You are allowed to perform the following operations:

Increase any element of A by 1.
Decrease any element of A by 1.
Find the minimum number of operations required to make array A identical to array B.
'''

class Solution:
    def convert_arr(self,arr1,arr2,n):
        arr1.sort()
        arr2.sort()

        total=0

        for i in range(n):
            total+=abs(arr1[i]-arr2[i])

        return total
