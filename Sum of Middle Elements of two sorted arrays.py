'''
Given 2 sorted arrays Ar1 and Ar2 of size N each. Merge the given arrays and find the sum of the two middle elements of the merged array.

Example 1:

Input:
N = 5
Ar1[] = {1, 2, 4, 6, 10}
Ar2[] = {4, 5, 6, 9, 12}
Output: 11
Explanation: The merged array looks like
{1,2,4,4,5,6,6,9,10,12}. Sum of middle
elements is 11 (5 + 6).
'''

class Solution:
    def findMidSum(self, ar1, ar2, n):
        count=0
        
        i=0
        j=0
        total_sum=0
        iter=0
        
        while i<n and j<n:
            if ar1[i]<=ar2[j]:
                if iter==n-1 or iter==n:
                    total_sum+=ar1[i]
                    count+=1
                    if count==2:
                        return total_sum
                i+=1
            else:
                
                if iter==n-1 or iter==n:
                    total_sum+=ar2[j]
                    count+=1
                    if count==2:
                        return total_sum
                        
                j+=1
            iter+=1
            
        if count<2:
          if i==n:
              total_sum+=ar2[j]
          elif j==n:
              total_sum+=ar1[i]
        return total_sum
