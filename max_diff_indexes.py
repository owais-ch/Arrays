'''
Maximum difference Indexes (GFG)
Given an array A[]of size N. Let us call difference between indices of an element's first and last appearance in the array A[] a gap. Find the maximum possible gap.  Note that if any element appears only once, then the gap for that element is 0.
 

Example 1:

Input:
N = 9
A[] = {2, 1, 3, 4, 2, 1, 5, 1, 7}
Output:
6
Explanation:
For the above test case (Assuming 0-based indexing): 
Number 1's first appearance is at index 1 and last appearance is at index 7. This implies gap is 7-1=6
This is the maximum possible in the given test case.
'''
class Solution:
    def maxDiffIndex(self, A, N):
        dict1=dict()
        
        gap=0
        
        for i in range(N):
            if A[i] not in dict1:
                dict1[A[i]]=i
            else:
                gap=max(gap,i-dict1[A[i]])
                
        return gap
