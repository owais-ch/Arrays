'''Problem Description

Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.
Example:

Input:

1 2 3
4 5 6
7 8 9
Return the following:
[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]


Input: 
1 2
3 4
Return the following: 
[
  [1],
  [2, 3],
  [4]
]'''



import numpy as np

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n=len(A)
        
        list1=np.ravel(A)
        
        list2=[[] for i in range(2*(n-1)+1)]

        for i in range(n):
            list2[i].append(list1[i])
            indexz=i+n-1
            for j in range(i):
                list2[i].append(list1[indexz])
                indexz+=n-1
                
        start=2*n-1
        
        maxz=n-1
        
        for i in range(n,2*n):
            indexz=start
            for j in range(maxz):
                list2[i].append(list1[indexz])
                indexz+=n-1
            start+=n
            maxz=maxz-1
                
            
        
        return list2
