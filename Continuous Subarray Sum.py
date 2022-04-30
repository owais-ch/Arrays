'''Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false'''

class Solution:
    def checkSubarraySum(self, nums, k):
        length=len(nums)
        
        sum1=sum(nums)
        
        if sum1<k and nums.count(0)<2:
            return False
        
        dict1={0:-1}
        total=0
        for i in range(length):
            total+=nums[i]
            
            rem=total%k
            
            if rem not in dict1:
                dict1[rem]=i
            elif rem in dict1 and i-dict1[rem]>1:
                return True
            
            
            if i>0:
                if nums[i]==0 and nums[i-1]==0:
                    return True
        return False
