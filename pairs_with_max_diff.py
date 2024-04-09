'''
Count the pairs with maximum difference (GFG)

Given an array a[ ] of N elements, the task is to find the number of ways to choose pairs {a[i], a[j]} such that their absolute difference is maximum.

Example:

Input:
N = 5
a[] = {3, 2, 1, 1, 3}
Output:
4
Explanation:
The maximum difference you can find is 2
which is from 3 - 1 = 2.
Number of ways of choosing it:
1) Choosing the first and third element
2) Choosing the first and fourth element
3) Choosing the third and fifth element
4) Choosing the fourth and fifth element
Hence, the answer is 4.
'''
import math

def countPairs(arr,n):
    maximum=max(arr)
    minimum=min(arr)
    count_max=0;count_min=0
    
    for i in range(n):
        if arr[i]==maximum:
            count_max+=1
        elif arr[i]==minimum:
            count_min+=1
    
    if maximum==minimum:
        return (count_max*(count_max-1))//2
        
    return count_max*count_min
            
