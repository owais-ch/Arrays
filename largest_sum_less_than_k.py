'''
Pair with largest sum which is less than K in the array

Given an array arr of size N and an integer K. The task is to find the pair of integers in the array such that their sum is maximum but less than K.

Note:Out of every possible pair, find pair with a maximum absolute difference.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow.
The first line of each test case contains N and K, where N is the number of elements in the array and K is the bound. The second line of each test case contains the array elements.

Output:
Print the pair with the maximum sum less than K.

Your task:
You don't have to take input. Complete the function Max_Sum(), which takes the array, N and K as parameters and returns the pair of integer in sorted manner first element of pair is minimum  if exist else return pair of zeros (0,0). The printing is done by the driver code. 

Constraints:
1 ≤ T ≤ 10
0 ≤ N ≤ 105
0 ≤ K ≤ 106
0 ≤ arr[i] ≤ 105

Example:
Input:
2
6 10
2 3 4 6 8 10
6 0
2 3 4 6 8 10
Output:
3 6
0 0
'''
def Max_Sum(arr,n,k):
    arr.sort()
    
    i,j=0,n-1
    maximum=-1
    indexz=[0,0]
    while i<j:
        if arr[i]+arr[j]>k:
            j-=1
        elif arr[i]+arr[j]<k:
            if arr[i]+arr[j]>maximum:
                maximum=arr[i]+arr[j]
                indexz=[arr[i],arr[j]]
            i+=1
        else:
            
            j-=1
        
    return indexz
