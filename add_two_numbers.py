'''
Add two numbers represented by two arrays (GFG)

Given two array A[0….N-1] and B[0….M-1] of size N and M respectively, representing two numbers such that every element of arrays represent a digit. For example, A[] = { 1, 2, 3} and B[] = { 2, 1, 4 } represent 123 and 214 respectively. 
The task is to find the sum of both the numbers.

Example 1:

Input : A[] = {1, 2}, B[] = {2, 1}
Output : 33
Explanation:
N=2, and A[]={1,2}
M=2, and B[]={2,1}
Number represented by first array is 12.
Number represented by second array is 21
Sum=12+21=33
'''

class Solution:
    def calc_Sum (self, arr,  n, brr, m) : 
        length1=len(arr)
        length2=len(brr)
        
        rem=0
        
        if length1>=length2:
            i,j=n-1,m-1
            
            while i>=0 and j>=0:
                value=arr[i]+brr[j]+rem
                arr[i]=value%10
                rem=value//10
                i-=1
                j-=1
            
            while i>=0:
                value=arr[i]+rem
                arr[i]=value%10
                rem=value//10
                i-=1
                
            if rem>0:
                arr[0:0]=[rem]
            return int(''.join(map(str,arr)))
        
        else:
            i,j=n-1,m-1
            
            while i>=0 and j>=0:
                value=arr[i]+brr[j]+rem
                brr[j]=value%10
                rem=value//10
                i-=1
                j-=1
                
            while j>=0:
                value=brr[j]+rem
                brr[j]=value%10
                rem=value//10
                j-=1
                
            if rem>0:
                brr[0:0]=[rem]
            return int(''.join(map(str,brr)))
