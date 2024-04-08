'''
Absolute distinct count (GFG)

Given a sorted array of N integers, find the number of distinct absolute values among the elements of the array. 

Example 1:

Input:
N = 6
arr[] = {-3, -2, 0, 3, 4, 5}
Output: 5
Explanation: There are 5 distinct absolute 
values among the elements of this array, 
i.e. 0, 2, 3, 4 and 5.
'''
class Solution:
    def distinctCount(self, arr, n):
        j=1
        
        for i in range(1,n):
            if arr[i]!=arr[i-1]:
                arr[j]=arr[i]
                j+=1
                
        arr=arr[:j]
        n=len(arr)
        count=n
  
        i,j=0,n-1
        
        while i<j:
            if abs(arr[i])==abs(arr[j]):
                count-=1
                if (i+1<n and arr[i+1]==arr[i]) and (j-1>=0 and arr[j-1]!=arr[j]):
                    i+=1
                elif (i+1<n and arr[i+1]!=arr[i]) and (j-1>=0 and arr[j-1]==arr[j]):
                    j-=1
                else:
                    i+=1
                    j-=1
            elif abs(arr[i])>abs(arr[j]):
                i+=1
            elif abs(arr[i])<abs(arr[j]):
                j-=1
                
        return count
