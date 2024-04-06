'''
Remove minimum number of elements

Given two arrays A[] and B[] consisting of N and M elements respectively. The task is to find minimum number of elements to remove from each array such that no common element exist in both the arrays.
 
Example 1:

Input :
A[] = { 2, 3, 4, 5, 8 }
B[] = { 1, 2, 3, 4}
Output :
3
Explanation:
We need to remove 2, 3 and 4 from any 
array.
'''
class Solution:
    def minRemove(self, a, b, n, m):
        dict1=dict()
        dict2=dict()
        
        for i in range(n):
            if a[i] not in dict1:
                dict1[a[i]]=1
            else:
                dict1[a[i]]+=1
                
        for i in range(m):
            if b[i] not in dict2:
                dict2[b[i]]=1
            else:
                dict2[b[i]]+=1
                
        #total1=0
        #total2=0
        total=0
        for i in dict1:
            if i in dict2:
                total+=min(dict1[i],dict2[i])
        return total
