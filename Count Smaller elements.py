'''
Given an array Arr of size N containing positive integers. Count number of smaller elements on right side of each array element.

Example 1:

Input:
N = 7
Arr[] = {12, 1, 2, 3, 0, 11, 4}
Output: 6 1 1 1 0 1 0
Explanation: There are 6 elements right
after 12. There are 1 element right after
1. And so on.
'''

import bisect

class Solution:

	def constructLowerArray(self,arr, n):
		list1=[arr[-1]]
		arr2=[0]
		maximum=arr[-1]
		minimum=arr[-1]
		
		for i in range(-2,-n-1,-1):
            if arr[i]>maximum:
                maximum=arr[i]
                arr2.append(-i-1)
                bisect.insort(list1,arr[i])
            elif arr[i]<minimum:
                minimum=arr[i]
                arr2.append(0)
                bisect.insort(list1,arr[i])
            else:
                bisect.insort(list1,arr[i])
                value=bisect.bisect_left(list1,arr[i])
                arr2.append(value)
                
        return arr2[::-1]
