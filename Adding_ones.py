'''
Adding Ones (GFG)

You start with an array A of size N. Initially all elements of the array A are zero. You will be given K positive integers. Let j be one of these integers, you have to add 1 to all A[i], where i ≥ j. 
Your task is to print the array A after all these K updates are done.

Note: Indices in updates array are given in 1-based indexing. That is updates[i] are in range [1,N].

Example 1:

Input:
N = 3, K = 4
1 1 2 3
Output:
2 3 4
Explanation:
Initially the array is {0, 0, 0}. After the
first 1, it becomes {1, 1, 1}. After the
second 1 it becomes {2, 2, 2}. After 2, 
it becomes {2, 3, 3} and 
After 3 it becomes, {2, 3, 4}. 
'''

class Solution:
    def update(self, a, n, updates, k):
        for i in range(k):
            a[updates[i]-1]=a[updates[i]-1]+1
            
        for i in range(1,n):
            a[i]=a[i]+a[i-1]
          
        return a[:]
