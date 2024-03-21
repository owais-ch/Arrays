'''
Minimum Number(GFG)
You are given an array arr of n elements. In one operation you can pick two indices i and j, such that arr[i] >= arr[j] and replace the value of arr[i] with (arr[i] - arr[j]). You have to minimize the values of the array after performing any number of such operations.

Example 1:

Input:
n = 3
arr = {3,2,4}
Output:
1
Explanation:
1st Operation : We can pick 4 & 3, subtract 4-3 => {3,2,1}
2nd Opeartion : We can pick 3 & 2, subtarct 3-2 => {1,2,1}
3rd Operation : We can pick 1 & 2, subtract 2-1 => {1,1,1}
4th Opeartion : We can pick 1 & 1, subtract 1-1 => {1,0,1}
5th Operation : We can pick 1 & 1, subtract 1-1 => {0,0,1}
After this no operation can be performned, so maximum no is left in the array is 1, so the ans is 1.
Example 2:
Time Complexity:O(N)  Space complexity:O(1)
'''

import math
class Solution:
    def minimumNumber(self, n, arr):
        if n==1:
            return arr[0]
        #arr.sort()
        num_odd=0
        minimum_even=math.inf
        
        for i in range(n):
            if arr[i]%2!=0:
                return 1
            else:
                if arr[i]<minimum_even:
                    minimum_even=arr[i]
        return minimum_even
