'''Problem Description
 
Given an integer array A.
Find the count of elements whose value is greater than all of its previous elements.

Note: Since there are no elements before first element so it should be considered in our answer.

Problem Constraints
1 <= |A| <= 105
1 <= Ai <= 109

Input Format
Given an integer array A.

Output Format
Return an integer.

Example Input
Input 1:
A = [1, 2, 3, 4]
Input 2:

A = [1, 1, 2, 2]

Example Output
Output 1:
4
Output 2:

2'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maximum=A[0]

        count=0

        for i in range(1,len(A)):
            if A[i]>maximum:
                count+=1
                maximum=A[i]

        return count+1
