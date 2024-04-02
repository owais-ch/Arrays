'''
Binary subarray with sum (GFG)
Given a binary array arr of size N and an integer target, return the number of non-empty subarrays with a sum equal to target.
Note : A subarray is the contiguous part of the array.

Example 1:

Input:
N = 5
target = 2
arr[ ] = {1, 0, 1, 0, 1}
Output: 4
Explanation: The 4 subarrays are:
{1, 0, 1, _, _}
{1, 0, 1, 0, _}
{_, 0, 1, 0, 1}
{_, _, 1, 0, 1}
 '''

class Solution:
    def numberOfSubarrays(self, arr, N, target):
        total=0
        arr1=[0]*(N)
        
        num_zeros=0
        
        for i in range(N):
            total+=arr[i]
            arr1[i]=total
            if total==0:
                num_zeros+=1
        
        for i in range(N):
            if arr1[i]!=0:
                arr1[i]=arr1[i]-1
                arr1[arr1[i]%N]=(arr1[arr1[i]%N]+N)
        for i in range(N):
            arr1[i]=arr1[i]//N
        
        arr1[0:0]=[num_zeros]
        count=0
        
        for j in range(target,N+1):
            if j==target:
                count+=arr1[j]
                count+=arr1[j]*arr1[0]
            else:
                count+=(arr1[j]*arr1[j-target])
                
        return count
