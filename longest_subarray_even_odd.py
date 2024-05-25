'''
Longest Subarray Of Evens And Odds (GFG)

You are given an array of size n. Find the maximum possible length of a subarray such that its elements are arranged alternately either as even and odd or odd and even .

Example 1:

Input:
n = 5
a[] = {10,12,14,7,8}
Output: 3
Explanation: The max length of subarray
is 3 and the subarray is {14 7 8}. Here 
the array starts as an even element and 
has odd and even elements alternately.
Example 2:

Input:
n = 2
a[] = {4,6}
Output: 1
Explanation: The array contains {4 6}. 
So, we can only choose 1 element as 
that will be the max length subarray.
'''
class Solution:
    #Function to find the length of longest subarray of even and odd numbers.
    def maxEvenOdd(self,arr,n):
        count=1
        maximum=1
        for i in range(n-1):
            if arr[i]%2==0 and arr[i+1]%2!=0:
                count+=1
            elif arr[i]%2!=0 and arr[i+1]%2==0:
                count+=1
            else:
                maximum=max(maximum,count)
                count=1
        if count>1:
            maximum=max(maximum,count)
            
        return maximum


