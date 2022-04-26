'''Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 
Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109'''

class Solution:
    def nextGreaterElements(self, nums):
        length=len(nums)
        
        list1=[-999999]*length
        
        stack=[nums[-1]]
        
        for i in range(-1,-length-1,-1):
            while stack!=[]:
                if nums[i]>=stack[-1]:
                    stack.pop()
                    
                else:
                    break
                  
            if stack!=[]:
                
                list1[i]=stack[-1]
            stack.append(nums[i])
            
            if list1[i]==-999999:
                for j in range(-length,i):
                    if nums[j]>nums[i]:
                        list1[i]=nums[j]
                        break
                
                if list1[i]==-999999:
                    list1[i]=-1
            
        return list1
