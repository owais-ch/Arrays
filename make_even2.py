'''
Given an array arr[] of size N, the task is to make all array elements even by replacing a pair of adjacent elements with their sum.

Examples:

Input: arr[] = { 2, 4, 5, 11, 6 }
Output: 1
Explanation:
Replacing a pair (arr[2], arr[3]) with their sum ( = 5 + 11 = 16) modifies arr[] to { 2, 4, 16, 16, 6 } 
Since all array elements are even, the required output is 1.

Input: arr[] = { 1, 2, 4, 3, 11 } 
Output: 3
Explanation: 
Replacing the pair (arr[3], arr[4]) and replacing them with their sum ( = 3 + 11 = 14) modifies arr[] to { 1, 2, 4, 14, 14 }
Replacing the pair (arr[0], arr[1]) and replacing them with their sum ( = 1 + 2 = 3) modifies arr[] to { 3, 3, 4, 14, 14 }
Replacing the pair (arr[0], arr[1]) with their sum ( = 3 + 3 = 6) modifies arr[] to { 6, 6, 4, 14, 14 }. 
Therefore, the required output is 3.
'''

def make_even2(arr):
    length=len(arr)
    
    count=0
    i=0
    
    while i<length:
        if arr[i]%2!=0 and arr[i+1]%2!=0:
            count+=1
            if i==length-2:
                return count
            i+=2
        elif arr[i]%2!=0 and arr[i+1]%2==0:
            count+=2
            if i==length-2:
                return count
            i+=2
        else:
            if i==length-1 and arr[i]%2==0:
                return count
            elif arr[i]%2==0 and arr[i+1]%2==0 and i==length-2:
                return count
            i+=1
            
    if arr[length-1]%2!=0:
        count+=2
        
    return count
