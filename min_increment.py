'''
Given an array arr[] consisting of N positive integers, the task is to find the minimum number of increments required to make the array arr[] alternating
sequence of even and odd numbers.

Examples:

Input: arr[] = {1, 4, 6, 8, 9, 5}
Output: 2
Explanation:
Incrementing arr[2] modifies arr[] to {1, 4, 7, 8, 9, 5}.
Incrementing arr[5] by 1 modifies arr[] to {1, 4, 7, 8, 9, 6}.

Input: arr[] = {3, 5, 7, 9, 4, 2}
Output: 3
Explanation:
Incrementing arr[0] by 1 modifies arr[] to {4, 5, 7, 9, 4, 2}.
Incrementing arr[2] by 1 modifies arr[] to {4, 5, 8, 9, 4, 2}.
Incrementing arr[5] by 1 modifies arr[] to {4, 5, 8, 9, 4, 3}.
'''

def min_increment(arr,n):
    count1=0
    count2=0
    
    for i in range(n):
        if i%2==0 and arr[i]%2==0:  
            count1+=1
        elif i%2!=0 and arr[i]%2!=0:
            count1+=1
        elif i%2==0 and arr[i]%2!=0:
            count2+=1
        elif i%2!=0 and arr[i]%2==0:
            count2+=1
            
    return min(count1,count2)
