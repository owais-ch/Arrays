'''Given two sorted arrays such the arrays may have some common elements. Find the sum of the maximum sum path to reach from beginning of any array to end
of any of the two arrays. You can start from any array and switch from one array to another array only at common elements. 

Example 1:

Input:
M = 5, N = 4
Arr1[] = {2, 3, 7, 10, 12}
Arr2[] = {1, 5, 7, 8}
Output: 35
Explanation: 35 is sum of 1 + 5 + 7 + 10 +
12. We start from the first element of
Arr2 which is 1, then we move to 5, then 7
From 7, we switch to Arr1 (as 7 is common)
and traverse 10 and 12.
'''

class Solution:

	def maxPathSum(self,arr1, arr2, m, n):
		sum1,sum2=0,0
		max_sum=0
		
		i,j=0,0
		
		while i<m and j<n:
		    if arr1[i]<arr2[j]:
		        sum1+=arr1[i]
		        i+=1
            elif arr2[j]<arr1[i]:
                sum2+=arr2[j]
                j+=1
            else:
                sum1+=arr1[i]
		        sum2+=arr2[j]
		        max_sum+=max(sum1,sum2)
		        sum1=0
		        sum2=0
		        i+=1
                j+=1
            
        if i==m:
            while j<n:
                sum2+=arr2[j]
                j+=1
                
            max_sum+=max(sum1,sum2)
        elif j==n:
            while i<m:
                sum1+=arr1[i]
                i+=1
            max_sum+=max(sum1,sum2)
        else:
            max_sum+=max(sum1,sum2)
        
        return max_sum
