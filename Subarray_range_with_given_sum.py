'''
Subarray range with given sum (GFG)

Given an unsorted array of integers and a sum. The task is to count the number of subarray which adds to the given sum.

Example 1:

Input:
n = 5
arr[] = {10,2,-2,-20,10}
sum = -10
Output: 3
Explanation: Subarrays with sum -10 are: 
[10, 2, -2, -20], [2, -2, -20, 10] and 
[-20, 10].
'''

class Solution:
    def subArraySum(self,arr, n, sum):
        dict1=dict()
        
        total=0
        count=0
        
        for i in range(n):
            total+=arr[i]
            
            if total==sum:
                count+=1
            
            if total-sum in dict1:
                count+=dict1[total-sum]
                
            if total not in dict1:
                dict1[total]=1
            else:
                dict1[total]+=1
                
        return count
