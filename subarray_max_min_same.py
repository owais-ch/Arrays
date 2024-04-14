'''
Number of subarrays whose minimum and maximum are same

Given an array A[] of n integers, the task is to find the number of subarrays whose minimal and maximum elements are same.

Example 1:

Input : Arr[] = {1, 1, 3}
Output : 4
Explanation:
The subarrays are
(1), (1), (3) and (1, 1) 

Example 2:

Input : Arr[] = {1, 2, 3, 4}
Output : 4
'''
class Solution:
    def numberOfways(self, a, n): 
        count=1
        total=n
        
        for i in range(1,n):
            if arr[i]==arr[i-1]:
                count+=1
            else:
                if count>1:
                    total+=(count*(count-1))//2
                count=1
            
        if count>1:
            total+=(count*(count-1))//2
            
        return total
            
