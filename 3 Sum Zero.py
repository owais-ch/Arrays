'''Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 

Find all unique triplets in the array which gives the sum of zero.

Note:

Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.

For example, given array S = {-1 0 1 2 -1 -4},

A solution set is:

  (-1, 0, 1)

  (-1, -1, 2)'''

from collections import OrderedDict

class Solution:
    def threeSum(self, A):
        length=len(A)
        A.sort()
        
        dict1=OrderedDict()
        for i in range(length-2):
            j,k=i+1,length-1
            if A[i]+A[j]>0:
                break
            while j<k:
                sum1=A[i]+A[j]+A[k]

                if sum1==0:
                    if (A[i],A[j],A[k]) not in dict1:
                        dict1[(A[i],A[j],A[k])]=1
                    
                    j+=1
                    k-=1
                elif sum1>0:
                    k-=1
                elif sum1<0:
                    j+=1

                
                
        return list(dict1.keys())
    
  
  
