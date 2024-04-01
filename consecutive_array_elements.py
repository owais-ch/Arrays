'''
Consecutive Array Elements (GFG)

Given an unsorted array arr[] of size N, the task is to check whether the array consists of consecutive numbers or not.

Example 1:

Input: N = 5, arr[] = {5, 4, 2, 1, 3}
Output: Yes
Explanation: All are consecutive elements,
according to this order 1,2,3,4 and 5.
'''

class Solution:
    def areConsecutives(self, arr, n):
        minimum=min(arr)
        
        expected_maximum=minimum+n-1
        
        arr_total=sum(arr)
        
        sum_total=0
        
        for k in range(minimum,expected_maximum+1):
            sum_total+=k
            
        if arr_total==sum_total:
            return 1
            
        return 0
