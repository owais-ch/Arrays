'''Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
 
Constraints:

n == nums.length
1 <= n <= 104
-105 <= nums[i] <= 105'''

class Solution:
    def checkPossibility(self, nums):
        length=len(nums)
        
        if length==1:
            return True
        
        count=0
        countz=0
        
        indexz=-1
        
        for i in range(length-1):
            if nums[i]>nums[i+1]:
                indexz=i
                count+=1
            
            elif nums[i]<nums[i+1]:
                countz+=1
                
            if count>1:
                return False
            
        
        if indexz==0 or indexz==-1 or indexz==length-1 or indexz==length-2:
            return True
        elif nums[indexz-1]<=nums[indexz+1]:
            return True
        if nums[:indexz]==sorted(nums[:indexz]) and nums[indexz+1:]==sorted(nums[indexz+1:]) and nums[indexz-1]<=nums[indexz+1]:
            return True
        elif nums[:indexz+1]==sorted(nums[:indexz+1]) and nums[indexz+2:]==sorted(nums[indexz+2:]) and nums[indexz]<=nums[indexz+2]:
            return True
        return False
