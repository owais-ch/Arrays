'''
Find Leftover Elements (GFG)

Given an array arr, the size is reduced by 1 element at each step. In the first step, the maximum element would be removed, while in the second step, 
the minimum element of the remaining array would be removed, in the third step again the maximum, and so on. Continue this till the array contains only one element. And find the final element remaining in the array.

Examples:

Input:arr[] = [7, 8, 3, 4, 2, 9, 5]
Ouput: 5
Explanation:In first step '9' would be removed, in 2nd step '2' will be removed, in third step '8' will be removed and so on. So the last remaining element would be '5'.  
'''

class Solution:
    def leftElement(self,arr) -> int:
        arr.sort()
        n=len(arr)
        
        if n%2==0:
            return arr[n//2-1]
            
        return arr[n//2]
