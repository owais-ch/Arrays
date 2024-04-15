'''
Given an array A of positive integers, find the smallest non-negative integer (i.e. greater than or equal to zero) that can be placed between any two elements of the array such that the sum of elements in the subarray occurring before it, 
is equal to the sum of elements occurring in the subarray after it, with the newly placed integer included in either of the two subarrays.

Example 1:

Input : Arr[] = {3, 2, 1, 5, 7, 8}
Output : 4 5 1
Explanation:
The smallest possible number that we can 
insert is 4, at position 5 (i.e. between 
5 and 7) as part of first subarray so that 
the sum of the two subarrays becomes 
equal as, 3+2+1+5+4=15 and 7+8=15.

Example 2:

Input : Arr[] = {9, 5, 1, 2, 0}
Output : 1 2 2
Explanation:
The smallest possible number that we can 
insert is 1,at position 2 (i.e. between 9 
and 5) as part of second subarray in 
order to get an equal sum of 9.
'''

import math
class Solution:
    def EqualSum(self,a,n):
        right_sum=sum(a)
        left_sum=0
        
        min_value=math.inf
        min_indexz=0
        min_which_side=0
        
        for i in range(n):
            left_sum+=a[i]
            right_sum-=a[i]
        
            if left_sum<right_sum:
                diff=right_sum-left_sum
                minimum=diff
                indexz=i+2
                which_side=1
                if minimum<min_value:
                    min_value=minimum
                    min_indexz=indexz
                    min_which_side=which_side
                    
            elif left_sum>right_sum:
                diff=left_sum-right_sum
                minimum=diff
                indexz=i+2
                which_side=2
                if minimum<min_value:
                    min_value=minimum
                    min_indexz=indexz
                    min_which_side=which_side
            else:
                minimum=0
                indexz=i+2
                min_value=minimum
                min_indexz=indexz
                min_which_side=1
                    
        return min_value,min_indexz,min_which_side
