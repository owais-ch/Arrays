'''Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []'''

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict1=dict()
        dict2=dict()
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            elif dict1[i]==1:
                dict2[i]=1
                dict1[i]+=1
        return dict2.keys()
