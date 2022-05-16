'''Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
nums[i] - nums[j] == k
Notice that |val| denotes the absolute value of val.

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.'''

from collections import Counter,OrderedDict

class Solution:
    def findPairs(self, nums, k):
        if k==0:
            total=0
            dict1=Counter(nums)
            
            for i in dict1:
                if dict1[i]>1:
                    total+=1
                    
            return total
        
        nums=sorted(list(set(nums)))
        dict1=Counter(nums)
        print(dict1)
        total=0
        
        for i in dict1:
            
            if abs(k-i) in dict1 and i>abs(k-i):
                if abs(i-abs(k-i))==k:
                    dict1[i]=0
                    total+=1
            elif i-k in dict1:
                dict1[i]=0
                total+=1
            
                
        return total
