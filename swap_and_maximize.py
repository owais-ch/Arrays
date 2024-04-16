'''
Swap ans Maximize
Given an array a[ ] of N elements. Consider array as a circular array i.e. element after an is a1. The task is to find maximum sum of the absolute difference between consecutive elements with rearrangement of array elements allowed
i.e. after any rearrangement of array elements find |a1 – a2| + |a2 – a3| + …… + |an-1 – an| + |an – a1|.

Example 1:

Input:
N = 4
a[] = {4, 2, 1, 8}
Output: 
18
Explanation: Rearrangement done is {1, 8, 
2, 4}. Sum of absolute difference between 
consecutive elements after rearrangement = 
|1 - 8| + |8 - 2| + |2 - 4| + |4 - 1| = 
7 + 6 + 2 + 3 = 18.
'''
def maxSum(arr,n):
    arr.sort()
    
    mid=n//2
    i=0
    j=n-1
    
    total=0
    
    while i<j:
        if i==0:
            total+=(abs(arr[i]-arr[j]))
        else:
            total+=abs(arr[i]-arr[j+1])+abs(arr[i]-arr[j])
            
        i+=1
        j-=1
        
    if n%2!=0:
        total+=abs(arr[mid]-arr[mid+1])
        
    total+=abs(arr[0]-arr[mid])
    
    return total
        
