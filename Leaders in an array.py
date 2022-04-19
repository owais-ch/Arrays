'''Problem Description
Given an integer array A containing N distinct integers, you have to find all the leaders in the array A.

 An element is leader if it is strictly greater than all the elements to its right side.

NOTE:The rightmost element is always a leader.

Input Format
First and only argument is an integer array A.

Output Format
Return an integer array denoting all the leader elements of the array.

NOTE: Ordering in the output doesn't matter.

Example Input
Input 1:

 A = [16, 17, 4, 3, 5, 2]

Example Output
Output 1:

[17, 2, 5]'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        length=len(A)

        maximum=max(A[1:])

        list1=[]

        for i in range(length-1):
            if A[i]>maximum:
                list1.append(A[i])

            if i+2>length-1:
                break

            if A[i+1]==maximum:
                maximum=max(A[i+2:])
        list1.append(A[-1])

        return list1

