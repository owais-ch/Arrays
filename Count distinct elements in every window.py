'''Given an array of integers and a number K. Find the count of distinct elements in every window of size K in the array.

Example 1:

Input:
N = 7, K = 4
A[] = {1,2,1,3,4,2,3}
Output: 3 4 4 3
Explanation: Window 1 of size k = 4 is
1 2 1 3. Number of distinct elements in
this window are 3. 
Window 2 of size k = 4 is 2 1 3 4. Number
of distinct elements in this window are 4.
Window 3 of size k = 4 is 1 3 4 2. Number
of distinct elements in this window are 4.
Window 4 of size k = 4 is 3 4 2 3. Number
of distinct elements in this window are 3.'''


class Solution:
    def countDistinct(self, A, N, K):
        dict1=dict()
        distinct=0
        for i in range(K):
            if A[i] not in dict1:
                dict1[A[i]]=1
                distinct+=1
            else:
                dict1[A[i]]+=1
        list1=[distinct]
        
        first=0
        for i in range(K,N):
            dict1[A[first]]-=1
            if dict1[A[first]]==0:
                distinct-=1
            if A[i] not in dict1:
                dict1[A[i]]=1
                distinct+=1
            else:
                dict1[A[i]]+=1
                if dict1[A[i]]==1:
                    distinct+=1
            list1.append(distinct)
            
            first+=1
            
        return list1
