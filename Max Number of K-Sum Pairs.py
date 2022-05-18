'''You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.'''

from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dict1=Counter(nums)
        count=0
        
        for i in dict1:
            if k-i in dict1:
                if k-i==i and dict1[i]>1:
                    total=dict1[i]//2
                    count+=total
                    dict1[i]=dict1[i]-(total*2)
                elif k-i!=i:
                    total=min(dict1[i],dict1[k-i])
                    dict1[i]=dict1[i]-total
                    dict1[k-i]=dict1[k-i]-total
                    count+=total
        
        return count

