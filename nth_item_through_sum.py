'''
Nth item through Sum (GFG)
Given two arrays A and B of length L1 and L2, we can get a set of sums(add one element from the first and one from second). Find the Nth element in the set considered in sorted order.
Note: Set of sums should have unique elements.

Example 1:

Input: L1 = 2, L2 = 2
A = {1, 2}
B = {3, 4}
N = 3
Output: 6
Explaination: The set of sums are in 
the order 4, 5, 6.
'''

class Solution:
    def nthItem(self, L1, L2, A, B, N):
        set1=set()
        
        for i in range(L1):
            for j in range(L2):
                set1.add(A[i]+B[j])
                
        list1=sorted(list(set1))
        length=len(list1)
        if N>length:
            return -1
        return list1[N-1]
