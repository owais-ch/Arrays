'''Problem Description

Given an one-dimensional unsorted array A containing N integers.

You are also given an integer B, find if there exists a pair of elements in the array whose difference is B.

Return 1 if any such pair exists else return 0.

Problem Constraints
1 <= N <= 105
-103 <= A[i] <= 103
-105 <= B <= 105

Input Format
First argument is an integer array A of size N.

Second argument is an integer B.

Output Format
Return 1 if any such pair exists else return 0.'''

from collections import Counter

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        length=len(A)

        dict1=Counter(A)

        for i in dict1:
            if i-B in dict1:
                if i-B==i and dict1[i]>1:
                    return 1
                elif i-B!=i:
                    return 1

        return 0
