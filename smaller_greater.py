'''
Given an array, find an element before which all elements are smaller than it, and after which all are greater than it. Return the index of the element if there
is such an element, otherwise, return -1.

Examples:

Input: arr[] = {5, 1, 4, 3, 6, 8, 10, 7, 9}; 
Output: 4 
Explanation: All elements on left of arr[4] are smaller than it 
and all elements on right are greater.

Input: arr[] = {5, 1, 4, 4}; 
Output: -1 
Explanation : No such index exits.
'''

def element(arr):
    length=len(arr)
    
    maximum=arr[0]
    minimum=min(arr[2:])
    min_index=2+arr[2:].index(minimum)
    
    for i in range(1,length-1):
        if maximum<arr[i]<minimum:
            return arr[i]
        
        if i==length-2:
            break
        if arr[i]>maximum:
            maximum=arr[i]
        if i+1==min_index:
            minimum=min(arr[i+2:])
            min_index=i+2+arr[i+2:].index(minimum)
            
    return -1


