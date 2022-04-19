'''Problem Description
 
Given an integer array A of size N.

You need to check that whether there exist a element which is strictly greater than all the elements on left of it and strictly smaller than all the elements on right of it.

If it exists return 1 else return 0.

NOTE:

Do not consider the corner elements i.e A[0] and A[N-1] as the answer.

Problem Constraints
3 <= N <= 105

1 <= A[i] <= 109

Input Format
First and only argument is an integer array A containing N integers.

Output Format
Return 1 if there exist a element that is strictly greater than all the elements on left of it and strictly  smaller than all the elements on right of it else return 0.

Example Input
Input 1:

 A = [5, 1, 4, 3, 6, 8, 10, 7, 9]
Input 2:

 A = [5, 1, 4, 4]'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):
        maximum=A[0]
        minimum=min(A[2:])
        length=len(A)
        
        for i in range(1,length-1):
            
            if A[i]>maximum and A[i]<minimum:
                return 1
            if A[i]>maximum:
                maximum=A[i]
            
            if i+2<length:
                if A[i+1]==minimum:
                    minimum=min(A[i+2:])
            else:
                break
            
                
        return 0
