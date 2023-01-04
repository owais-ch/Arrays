'''
Given an array of size N, find the number of distinct pairs {i, j} (i != j) in the array such that the sum of a[i] and a[j] is greater than 0.

Example 1:

Input: N = 3, a[] = {3, -2, 1}
Output: 2
Explanation: {3, -2}, {3, 1} are two 
possible pairs.
Example 2:

Input: N = 4, a[] = {-1, -1, -1, 0}
Output: 0
Explanation: There are no possible pairs.
'''

class Solution:
    def ValidPair(self, arr, n): 
    	arr.sort()
    	count=0
    	
    	i,j=0,n-1
    	
    	while i<j:
    	    if arr[i]+arr[j]>0:
    	        j-=1
            else:
                count+=(n-j-1)
                i+=1
                
        pos=(n-j-1)
        count+=((pos*(pos+1))//2)
        return count
