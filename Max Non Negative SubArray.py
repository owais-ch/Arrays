'''Problem Description

Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

NOTE:  

If there is a tie, then compare with segment's length and return segment which has maximum length.
If there is still a tie, then return the segment with minimum starting index.


Problem Constraints
1 <= N <= 105

-109 <= A[i] <= 109



Input Format
The first and the only argument of input contains an integer array A, of length N.



Output Format
Return an array of integers, that is a subarray of A that satisfies the given conditions.



Example Input
Input 1:

 A = [1, 2, 5, -7, 2, 3]
Input 2:

 A = [10, -1, 2, 3, -4, 100]


Example Output
Output 1:

 [1, 2, 5]
Output 2:

 [100]'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        list1=[]

        length=len(A)

        sum1=0
        list2=[]
        
        positive_count=0
        
        for i in range(length):
            if A[i]<0:
                if positive_count>0:
                    list1.append(A[i-positive_count:i])
                    list2.append(sum1)
                    sum1=0
                    positive_count=0
            elif A[i]>=0:
                positive_count+=1
                sum1+=A[i]
        if positive_count>0:
            list1.append(A[i-positive_count+1:i+1])
            list2.append(sum1)
            sum1=0
            
        if list2==[]:
            return []
        indexz=list2.index(max(list2))
        return list1[indexz]
