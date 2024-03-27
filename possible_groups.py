'''
Possible groups (GFG)
Given an array of positive integers of size N, form groups of two or three such that the sum of all elements in a group is a multiple of 3. Count all possible number of groups that can be generated in this way.

Example 1:

Input:
N = 5
arr[] = {3, 6, 7, 2, 9}
Output: 8
Explanation: 
Groups of two are: 
{3, 6}, {3, 9}, {9, 6}, {7, 2}.
Groups of three are: 
{3, 7, 2}, {7, 2, 6}, {7, 2, 9}, {3, 6, 9}.
'''

class Solution:
    def findgroups(self, arr, n):
        arr=[i%3 for i in arr]
        num_zeros=0
        num_ones=0
        num_twos=0
        
        for i in range(n):
            if arr[i]==0:
                num_zeros+=1
            elif arr[i]==1:
                num_ones+=1
            else:
                num_twos+=1
                
        group_of_two=0
        
        if num_zeros>1:   
            group_of_two+=(num_zeros*(num_zeros-1))//2
            
        group_of_two+=(num_ones*num_twos)  ##### group of two
        
        group_of_three=0
        
        if num_zeros>=3:
            group_of_three+=(num_zeros*(num_zeros-1)*(num_zeros-2))//6
            
        if num_ones>=3:
            group_of_three+=(num_ones*(num_ones-1)*(num_ones-2))//6
            
        if num_twos>=3:
            group_of_three+=(num_twos*(num_twos-1)*(num_twos-2))//6
        
        group_of_three+=(num_zeros*num_ones*num_twos)
        
        return group_of_two+group_of_three
