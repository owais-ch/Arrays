'''
Transform the array (GFG)
Given an array arr[] of size N containing integers, zero is considered an invalid number, and rest all other numbers are valid. If two nearest valid numbers are equal then double the value of the first one and make the second number as 0. At last move all the valid numbers on the left.

Example 1:

Input: N = 12
arr[] = {2, 4, 5, 0, 0, 5, 4, 8, 6, 0, 
                                 6, 8}
Output:  2 4 10 4 8 12 8 0 0 0 0 0
Explanation: After performing above 
given operation we get array as,
2 4 10 0 0 0 4 8 12 0 0 8, then shifting
all zero's to the right, we get resultant
array as - 2 4 10 4 8 12 8 0 0 0 0 0 
'''

class Solution:
    def valid(self,arr, n): 
        i,j=0,1
        
        while j<n:
            if arr[i]==0 and arr[j]!=0:
                i=j
                j=j+1
            elif arr[j]==0 and arr[i]!=0:
                j+=1
            elif arr[i]==0 and arr[j]==0:
                j+=1
            elif arr[i]==arr[j] and arr[i]>0:
                #print('i=',i,arr[i],'j=',j,arr[j])
                arr[i]=2*arr[i]
                arr[j]=0
                #i+=1
                j+=1
            elif arr[i]>0 and arr[j]>0 and arr[i]!=arr[j]:
                i=j
                j+=1
            
            
        i,j=0,0
        
        while j<n:
            if arr[j]!=0:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                
            j+=1
            
        return arr
