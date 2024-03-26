'''
Ishaan and Sticks
Ishaan has a craving for sticks. He has N sticks. He observes that some of his sticks are of the same length, and thus he can make squares out of those.
He wants to know how big a square he can make using those sticks as sides. Since the number of sticks is large, he can't do that manually. Can you tell him the maximum area of the biggest square that can be formed?
Also, calculate how many such squares can be made using the sticks.

Example 1:

â€‹Input : arr[ ] = {2, 2, 2, 9, 2, 2, 2, 2, 2}
Output : 4 2
Explanation:
2 squares of side 2 are formed.
return maximum area and number of square.
'''

from collections import Counter

def square (arr, n) : 
    dict1=Counter(arr)
    
    maximum=0
    max_area=0
    
    for i in dict1:
        if dict1[i]/4>=1 and i**2>max_area:
                max_area=i**2
                maximum=dict1[i]//4
    
    if max_area==0 and maximum==0:
        return [-1]
    return max_area,maximum
