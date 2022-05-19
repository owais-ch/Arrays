'''Given an array ‘A’ of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

Example:

Input :

    A : [1 3 5] 
    k : 4
Output : YES

as 5 - 1 = 4

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Try doing this in less than linear space complexity.'''

class Solution:
    def diffPossible(self, A, B):
        length=len(A)

        i,j=0,1

        while i<length and j<length:
            if (A[i]-A[j]==B or A[i]-A[j]==-B) and i!=j:
                return 1
            elif A[j]-A[i]>B:
                i+=1
            elif A[j]-A[i]<B:
                j+=1
            if i==j:
                j+=1
        return 0
