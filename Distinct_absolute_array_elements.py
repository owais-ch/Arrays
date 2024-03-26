'''
Distinct absolute array elements (GFG)

Given a sorted array of size N. Count the number of distinct absolute values present in the array.
 
Example 1:

Input:
N = 6
Arr[] = {-3, -2, 0, 3, 4, 5}
Output: 5
Explanation: There are 5 distinct absolute 
values i.e. 0, 2, 3, 4 and 5.
'''

class Solution:
    def distinctCount(self, arr, n):
        j=1
        
        for i in range(1,n):
            if arr[i]!=arr[i-1]:
                arr[j]=arr[i]
                j+=1
                
        arr[:]=arr[:j]
        length=len(arr)
        
        i,j=0,length-1
        count=0
        #print(arr[:j])
        while i<=j:
            if abs(arr[i])<abs(arr[j]):
                count+=1
                j-=1
            elif abs(arr[i])>abs(arr[j]):
                count+=1
                i+=1
            else:
                count+=1
                i+=1
                j-=1
                
        return count  
                
