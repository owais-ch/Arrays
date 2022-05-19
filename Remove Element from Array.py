'''Given an array and a value, remove all the instances of that value in the array. 

Also return the number of elements left in the array after the operation.

It does not matter what is left beyond the expected length.

Example:

If array A is [4, 1, 1, 2, 1, 3]

and value elem is 1, 

then new length is 3, and A is now [4, 2, 3]

Try to do it in less than linear additional space complexity.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        length=len(A)

        x=0
        count=0
        for i in range(length):
            if A[i]!=B:
                A[x]=A[i]
                x+=1
            else:
                count+=1

        length=length-count

        return length
