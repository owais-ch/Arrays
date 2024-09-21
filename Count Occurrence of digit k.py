'''
Count Occurrence of digit k (GFG)

Given an array arr[]. Your task is to return an integer denoting the total number of times digit k appears in the array.

Examples:

Input: k=1, arr[] = [11, 12, 13, 14, 15]
Output: 6 
Explanation: Here, digit 1 appears in the whole array 6 times.
'''

class Solution:
    def num(self, k, arr):
        count=0
        
        n=len(arr)
        
        for i in range(n):
            count+=str(arr[i]).count(str(k))
            
        return count
