'''Problem Description

Given an integer array A of size N. You need to count the number of special elements in the given array.

A element is special if removal of that element make the array balanced.

Array will be balanced if sum of even index element equal to sum of odd index element.

Problem Constraints
1 <= N <= 105

1 <= A[i] <= 109

Input Format
First and only argument is an integer array A of size N.

Output Format
Return an integer denoting the count of special elements.

Example Input
Input 1:

 A = [2, 1, 6, 4]
Input 2:

 A = [5, 5, 2, 5, 8]


Example Output
Output 1:

 1
Output 2:

 2'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        length=len(A)

        even_total=sum([A[i] for i in range(length) if i%2==0])

        odd_total=sum(A)-even_total

        prefix_odd=0
        prefix_even=0

        suffix_odd=odd_total
        suffix_even=even_total

        count=0

        for i in range(length):
            if i%2==0:
                suffix_even=suffix_even-A[i]
                if i>0:
                    prefix_odd+=A[i-1]

            else:
                suffix_odd=suffix_odd-A[i]
                if i>0:
                    prefix_even+=A[i-1]

            if prefix_odd+suffix_even==prefix_even+suffix_odd:
                count+=1

        return count
