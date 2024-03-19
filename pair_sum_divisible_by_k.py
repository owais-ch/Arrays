'''
Count pairs in array divisible by K (GFG)

Given an array A[] and positive integer K, the task is to count total number of pairs in the array whose sum is divisible by K.

Example 1:

Input : 
A[] = {2, 2, 1, 7, 5, 3}, K = 4
Output : 5
Explanation : 
There are five pairs possible whose sum
is divisible by '4' i.e., (2, 2), 
(1, 7), (7, 5), (1, 3) and (5, 3)
'''

class Solution:
    def countKdivPairs(self, arr, n, k):
        arr1=[i%k for i in arr]
        dict1=dict()
        count=0
        total=0
        
        for i in range(n):
            if arr1[i]==0:
                count+=1
            else:
                if arr1[i] not in dict1:
                    dict1[arr1[i]]=1
                else:
                    dict1[arr1[i]]+=1
        #print(dict1)
        for p in dict1:
            if k-p==p:
                total+=(dict1[p]*(dict1[p]-1))//2
                dict1[p]=0
            else:
                if k-p in dict1 and dict1[k-p]>0 and dict1[p]>0:
                    total+=dict1[k-p]*dict1[p]
                    dict1[p]=0
                    dict1[k-p]=0
                
        if count>1:
            total+=(count*(count-1))//2
            
        return total
