'''
K-th missing element (GFG)
Geek wanted to construct a simple sequence of n integers, [1, 2, 3, ... n].
Given an increasing sequence a[], we need to find the K-th smallest missing element in the increasing sequence. If no k-th missing element is there, output -1.

Example 1:

Input : arr[ ] = {1, 3, 4, 5, 7} and K = 2
Output : 6
Explanation:
K = 2, We need to find the 2nd missing 
number in the array. Missing numbers are 
2 and 6. So 2nd missing number is 6.
'''

def KthMissingElement (arr, n, K) : 
    low=0
    high=n-1
    count=0
    start=arr[0]-1
    
    while low<=high:
        mid=(low+high)//2
          
        if arr[mid]-(mid+1+start)==K and arr[mid]-arr[mid-1]!=1:
            return arr[mid]-1
        elif mid==n-1 and arr[mid]-n==K:
            return arr[mid]-1
        elif mid+1+start==arr[mid]:
            low=mid+1
        elif arr[mid]-(mid+1+start)<K:
            low=mid+1
        elif arr[mid]-(mid+1+start)>=K:
            high=mid
            
        count+=1
        if mid==low and low==high:
            break
       
    if arr[mid]-(mid+1+start)>K:
        for p in range(arr[mid],arr[mid-1],-1):
            if p-(mid+start)==K:
                return p
    return -1
        
