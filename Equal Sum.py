'''
Given an array Arr of length N. Determine if there exists an element in the array such that the sum of the elements on its left is equal to the sum of the
elements on its right. If there are no elements to the left/right, then the sum is considered to be zero. 
Formally, find an i, such that, Arr1 + Arr2 ... Arri-1 = Arri+1 + Arri+2 ... ArrN.

Example 1:

Input:
N = 4
Arr[] = {1, 2, 3, 3}
Output: YES
Explanation: Consider i = 3, for [1, 2] 
sum is 3 and for [3] sum is also 3.
'''

class Solution:

	def equilibrium(self,arr, n): 
	    if n==1:
	        return "YES"
    	total=sum(arr)
    	left_sum=0
    	right_sum=total-(arr[0])
    	for i in range(1,n-1):
    	    left_sum+=arr[i-1]
    	    right_sum=right_sum-arr[i]
    	    
    	    if left_sum==right_sum:
    	        return "YES"
        return "NO"
