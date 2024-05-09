'''
Remove minimum elements (GFG)

Given an unsorted array Arr of size N. Find the minimum number of removals required such that twice of minimum element in the array is greater than or equal to the maximum in the array.

Example 1:

Input:
N = 9
Arr[] = {4,5,100,9,10,11,12,15,200}
Output: 4
Explanation: In the given array 4 elements 
4, 5, 200 and 100 are removed from the
array to make the array such that
2*minimum >= max (2*9 > 15).
'''
import bisect 
class Solution:
	def minRemoval(self,arr, n):
		arr.sort()
        
		minimum=n+1

		for i in range(n):
			target=2*arr[i]

			if target>=arr[-1]:
			    if i<minimum:
			        minimum=i
			elif i<n-1 and target<arr[i+1]:
			    if n-1<minimum:
			        minimum=n-1
			else:
				right_index=bisect.bisect_right(arr,target)
				
				indexz=n-right_index  
				
				left_index=bisect.bisect_left(arr,target)
				
				
				if i+indexz<minimum:
				    minimum=i+indexz
				
			if minimum<=i:
			    return minimum


		return minimum
