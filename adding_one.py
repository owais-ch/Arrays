'''
Given a non-negative integer(without leading zeroes) represented as an array A of N digits. Your task is to add 1 to the number (increment the number by 1).
The digits are stored such that the most significant digit is at the starting index of the array.

Example 1:

Input:
N = 4
A[] = {5, 6, 7, 8}
Output: 5 6 7 9
Explanation: 5678 + 1 = 5679
'''
class Solution:
    def addOne(self,arr, n):
        rem=0
        
        for i in range(n-1,-1,-1):
            if i==n-1:
                total=a[i]+rem+1
            else:
                total=a[i]+rem
                
            value=total%10
            rem=total//10
            arr[i]=value
            
        if rem!=0:
            arr[0:0]=[rem]
            
        return arr
