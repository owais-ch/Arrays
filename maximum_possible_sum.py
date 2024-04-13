'''
Maximum possible sum (GFG)
Given two arrays A and B of size N, the task is to find the maximum sum possible of a window in array B such that elements of the same window in array A are unique.

Example 1:

Input: N = 7
A = [0, 1, 2, 3, 0, 1, 4] 
B = [9, 8, 1, 2, 3, 4, 5] 
Output: 20
Explanation: The maximum sum possible 
in B[] such that all corresponding 
elements in A[] are unique is 
(9+8+1+2) = 20.
'''
import math

class Solution:
    def returnMaxSum(self, a, b, n):
        dict1=dict()
        
        maximum=-math.inf
        total=0
        last=0
        count=0
        
        for i in range(n):
            if a[i] not in dict1:
                dict1[a[i]]=i
                total+=b[i]
            else:
                maximum=max(maximum,total)
                
                
                previous=dict1[a[i]]
                
                #print(b[i],last,dict1[a[i]])
                
                if count==0:
                    #print('xxxxxxxx')
                    for p in range(dict1[a[i]]+1):
                        dict1.pop(a[p])
                        total-=b[p]
                else:
                    for p in range(last+1,dict1[a[i]]+1):
                        dict1.pop(a[p])
                        total-=b[p]
                #print(maximum,total)
                last=previous    
                total+=b[i]
                dict1[a[i]]=i
                count+=1
                
        
             
        maximum=max(maximum,total)
        
        return maximum
                
