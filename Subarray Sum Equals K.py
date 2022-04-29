'''Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2'''

class Solution:
    def subarraySum(self, nums, k):
        
        dict1={0:0}
        
        total=0
        
        count=0
        
        for i in nums:
            total+=i
            
            if total not in dict1:
                dict1[total]=0
            
                
            if total==k:
                count+=1
            if total-k in dict1:
                
                    count+=dict1[total-k]
            
            dict1[total]+=1
               
        return count
