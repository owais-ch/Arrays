'''
Total Cuts (GFG)
You are given an array A of N integers and an integer K, and your task is to find the total number of cuts that you can make such that for each cut these two conditions are satisfied
1. A cut divides an array into two parts equal or unequal length (non-zero).
2. Sum of the largest element in the left part and the smallest element in the right part is greater than or equal to K.

Example 1:

Input:
N=3
K=3
A[]={1,2,3}
Output:
2
Explanation:
Two ways in which array is divided to satisfy above conditions are:
{1} and {2,3} -> 1+2>=3(satisfies the condition)
{1,2} and {3} -> 2+3>=3(satisfies the condition)
'''

class Solution:
    def totalCuts(self, N, K,arr) -> int:
        if N==1:
            return 0
            
        left_max_array=[0]*N
        right_min_array=[0]*N
        
        i=0
        j=N-1
        while i<N and j>-1:
            if i==0:
                left_max_array[i]=arr[i]
                maximum=arr[i]
            else:
                if arr[i]>maximum:
                    left_max_array[i]=arr[i]
                    maximum=arr[i]
                else:
                    left_max_array[i]=maximum
                    
            if j==N-1:
                right_min_array[j]=arr[j]
                minimum=arr[j]
            else:
                if arr[j]<minimum:
                    right_min_array[j]=arr[j]
                    minimum=arr[j]
                else:
                    right_min_array[j]=minimum
                    
            j-=1
            i+=1
        
        count=0
        
        for i in range(N):
            if i<N-1:
                if left_max_array[i]+right_min_array[i+1]>=K:
                    count+=1
                    
        return count
