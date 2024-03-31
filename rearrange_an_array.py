'''
Rearrange an array such that arr[i] = i

Given an array of size N that has elements ranging from 0 to N-1. All elements may not be present in the array. If the element is not present then there will be -1 present in the array.
Rearrange the array such that A[i] = i, and if i is not present, display -1 at that place.

Example 1:

â€‹Input : arr[ ] = {-1, -1, 6, 1, 9, 3, 2, 
                              -1, 4, -1}
Output : -1 1 2 3 4 -1 6 -1 -1 9
Explanation:
In range 0 to 9, all except 0, 5, 7 and 8 
are present. Hence, we print -1 instead of 
them.
'''

class Solution:
    def modifyArray (self, arr,  n) : 
        i=0
        while i<n:
            if arr[i]==-1:
                i+=1
            elif arr[i]==i:
                i+=1
            else:
                value1=arr[i]
                value2=arr[arr[i]]
                arr[arr[i]]=value1
                arr[i]=value2
                
            #print(arr,i)
                
        return arr
