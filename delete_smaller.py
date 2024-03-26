'''
Delete array elements which are smaller than next or become smaller
Given an array arr[] and a number k. The task is to delete k elements which are smaller than next element (i.e., we delete arr[i] if arr[i] < arr[i+1]) or become smaller than next because next element is deleted.

Example 1:

â€‹Input : arr[ ] = {20, 10, 25, 30, 40} 
        and K = 2
Output : 25 30 40
Explanation:
First we delete 10 because it follows 
arr[i] < arr[i+1]. Then we delete 20 
because 25 is moved next to it and it 
also starts following the condition.
'''

def deleteElement (arr, n, k) : 
    p=0
    i=1
    while p<k and i<n:
        if arr[i-1]<arr[i]:
            arr.pop(i-1)
            n-=1
            p+=1
            i=i-1
        else:
            i+=1
        if i==0:
            i=1
        if p==k:
            break
        
    return arr
    
