'''
Pair array product sum(GFG)

Given a array a[] of non-negative integers. Count the number of pairs (i, j) in the array such that a[i] + a[j] < a[i]*a[j]. (the pair (i, j) and (j, i) are considered same and i should not be equal to j)

Example 1:

Input:
N=3
arr[] = {3, 4, 5} 
Output: 3
Explanation: Pairs are (3, 4) , (4, 5) and (3,5).  
'''

class Solution:
    def CountPairs (self,arr,n):
        num_ones=0
        num_twos=0
        
        for i in range(n):
            if arr[i]==1:
                num_ones+=1
            elif arr[i]==2:
                num_twos+=1
        
        
        return ((n-num_ones)*(n-num_ones-1))//2-(num_twos*(num_twos-1))//2
