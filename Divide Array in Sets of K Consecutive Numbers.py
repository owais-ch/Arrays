'''Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

Return true if it is possible. Otherwise, return false.

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.'''

from collections import Counter

class Solution:
    def isPossibleDivide(self, nums, k):
        length=len(nums)
        
        nums.sort()
        #for i in range(1,length):
        #    if nums[i]-nums[i-1]>1:
        #        return False
        dict1=Counter(nums)
        
        if length%k!=0:
            return False
        
        num_sets=length//k
        
        for i in range(num_sets):
            count=0
            list1=[]
            for j in dict1:
                if count>1 and dict1[j]==0:
                    return False
                if dict1[j]>0:
                    dict1[j]-=1
                    count+=1
                    list1.append(j)
                    
                if count==k:
                    break
                    
            if count<k:
                return False
            elif k>1:
                for q in range(1,k):
                    
                    if list1[q]-list1[q-1]!=1:
                        return False
                    
            
        return True
                    
