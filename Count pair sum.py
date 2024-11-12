'''

Given two sorted arrays arr1 and arr2 of distinct elements. Given a value x. The problem is to count all pairs from both arrays whose sum equals x.
Note: The pair has an element from each array.

Examples:

Input: x = 10, arr1[] = [1, 3, 5, 7], arr2[] = [2, 3, 5, 8] 
Output: 2
Explanation: The pairs are: (5, 5) and (7, 3).  
Input: x = 5, arr1[] = [1, 2, 3, 4], arr2[] = [5, 6, 7, 8]
Output: 0
Explanation: There are no valid pairs.
'''

class Solution:
    def countPairs(self,arr1, arr2, x):
        n=len(arr1)
        m=len(arr2)
        total_count=0
        
        i,j=0,m-1
        
        while i<n and j>=0:
            if arr1[i]+arr2[j]==x:
                total_count+=1
                i+=1
                j-=1
            elif arr1[i]+arr2[j]>x:
                j-=1
            else:
                i+=1
                
        return total_count
