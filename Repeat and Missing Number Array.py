'''You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4'''

from collections import Counter

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        dict1=Counter(A)

        list1=[]

        for i in dict1:
            if dict1[i]>1:
                list1.append(i)

        A=list(set(A))
        
        length=len(A)

        sum1=sum(A)
        sum2=A[-1]*(A[-1]+1)/2
        
        if sum1-sum2==0:
            list1.append(length+1)
            return list1
        else:
            list1.append(int(sum2-sum1))
            return list1
