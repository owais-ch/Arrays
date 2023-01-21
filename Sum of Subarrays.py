'''
Given an array A[] with N elements , you need to find the sum all sub arrays of array A. Since the sum could be very large print the sum modulo (109+7).


Example 1:

Input:
N = 3
A[] = {1, 2, 3}
Output: 20
Explanation:
All subarrays are [1], [2], [3],
[1,2], [2,3], [1,2,3].
Thus total sum is 20.
'''

class Solution:
    def subarraySum(self, a, n):
        sum1=0
        
        for i in range(n):
            sum1+=(i+1)*(n-i)*a[i]
            
        return sum1%(10**9+7)

