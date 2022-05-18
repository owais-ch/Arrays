'''Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.'''

from collections import Counter

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dict1=Counter(arr)
        
        for i in dict1:
            if i*2 in dict1:
                if i==i*2 and dict1[i]>1:
                    return True
                elif i!=i*2:
                    return True
            
        return False
