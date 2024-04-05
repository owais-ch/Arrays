'''
Pairs with Difference less than K (GFG)

Given an array of N integers, the task is to find all pairs with an absolute difference less than K.

NOTE: Pair (i, j) is considered same as (j, i)

Example 1:

Input : Arr[] = {1, 10, 4, 2}, K = 3
Output : 2
Explanation:
we have an array a[] = {1, 10, 4, 2} and 
K = 3 We can make only two pairs with a 
difference of less than 3.
(1, 2) and (4, 2). So, the answer is 2.
'''
class Solution:
    def countPairs(self,arr, n, k): 
        count=0
        
        arr.sort()
        start=1
        
        last_count=0
        
        for i in range(n):
            count+=(start-i-1)
            for j in range(start,n):
                if abs(arr[i]-arr[j])<k:
                    count+=1
                else:
                    start=j
                    break

            if start==n or j==n:
                return (n-1)*(n)//2
        
        return count
