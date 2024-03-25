'''
Given an array of size N containing positive integers n and a number k,The absolute difference between values at indices i and j is |a[i] a[j]|. 
There are n*(n-1)/2 such pairs and you have to print the kth smallest absolute difference among all these pairs.
 
Example 1:

Input : 
N = 4
A[] = {1, 2, 3, 4}
k = 3
Output : 
1 
Explanation :
The possible absolute differences are :
{1, 2, 3, 1, 2, 1}.
The 3rd smallest value among these is 1.
'''

def kthDiff( arr, n, k):
    if n==1:
        return 32766
    list1=[]
    for i in range(n-1):
        for j in range(i+1,n):
            list1.append(abs(arr[i]-arr[j]))
    list1=sorted(list1)
    length=len(list1)
    if k>length:
        return list1[-1]
    #print(list1,length,k)
    return list1[k-1]
    
