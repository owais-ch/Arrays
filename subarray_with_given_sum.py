'''
subarray with given sum (GFG)
Given an unsorted array arr[] of N integers and a sum. The task is to count the number of subarrays which add to a given number.

Example 1:

Input:
N=5
sum=-10
arr[] = { 10, 2, -2, -20, 10 }
Output:  3
Explanation:
Subarrays with sum -10 are: 
[10, 2, -2, -20], [2, -2, -20, 10]
and [-20, 10].
'''
class Solution:
    def findSubarraySum(self,arr, n, Sum):  
        dict1=dict()
        total=0
        count=0
        
        for i in range(n):
            total+=arr[i]
            if total==Sum:
                count+=1
                
            if total-Sum in dict1:
                count+=dict1[total-Sum]
                
            if total not in dict1:
                dict1[total]=1
            else:
                dict1[total]+=1
        return count
