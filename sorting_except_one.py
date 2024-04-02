'''
Sorting all array elements except one (GFG)

Given an array A of positive integers, sort the array in ascending order such that element at index K in unsorted array stays unmoved and all other elements are sorted.

Example 1:

â€‹Input : arr[ ] = {10, 4, 11, 7, 6, 20} 
        and K = 2
Output : 4 6 11 7 10 20
Explanation:
Sort an array except an index 2 So, 
4 6 11 7 10 20 
'''

def sortExceptK (arr, n, k) : 
    value=arr.pop(k)
    arr.sort()
    arr.insert(k,value)
    
    return ' '.join(list(map(str,arr)))
