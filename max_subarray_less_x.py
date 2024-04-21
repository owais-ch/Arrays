''' Maximum sum of subarray less than or equal to x (GFG)

Given an array arr[] of integers of size N and a number X, the task is to find the sum of subarray having maximum sum less than or equal to the given value of X.

Example 1:

Input: N = 5, X = 11
arr[] = {1, 2, 3, 4, 5} 
Output:  10
Explanation: Subarray having maximum 
sum is {1, 2, 3, 4}.
 
Example 2:

Input: N = 5, X = 7
arr[] = {2, 4, 6, 8, 10} 
Output:  6
Explanation: Subarray having maximum 
sum is {2, 4} or {6}.
'''
class Solution:
    def findMaxSubarraySum(self, arr, n, k):
        maximum=0
        total=0
        
        i,j=0,0
        
        while i<n:
            if total+arr[i]<=k:
                total+=arr[i]
                maximum=max(maximum,total)
            else:
                total+=arr[i]
                while j<=i:
                    total-=arr[j]
                    
                    if total<=k:
                        maximum=max(maximum,total)
                        j+=1
                        break
                    j+=1
            
            #print(total)            
            i+=1
        maximum=max(maximum,total)
       
        return maximum
