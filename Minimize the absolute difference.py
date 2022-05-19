'''Given three sorted arrays A, B  and Cof not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.

i.e. minimize | max(a,b,c) - min(a,b,c) |.

Example :

Input:

A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]
Output:

1
Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.'''

import numpy as np

class Solution:
	def solve(self, A, B, C):
        length1,length2,length3=len(A),len(B),len(C)

        i,j,k=0,0,0

        min_diff=9999999

        while i<length1 and j<length2 and k<length3:
            minimum=min(A[i],B[j],C[k])
            maximum=max(A[i],B[j],C[k])

            min_index=np.argmin([A[i],B[j],C[k]])

            if min_index==0:
                i+=1
            elif min_index==1:
                j+=1
            else:
                k+=1

            diff=abs(maximum-minimum)

            if diff<min_diff:
                min_diff=diff

        return min_diff
