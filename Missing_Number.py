'''
Missing Number (GFG)

Ritu has all numbers from 2 to n in an array, arr of length n-1 except one number. You have to return the missing number, Ritu doesn't have from 1 to n.

Note: Don't use Sorting

Examples:

Input: n = 4, arr = [1,  4,  3]
Output: 2     
Explanation: Ritu doesn't have the number 2
Input: n = 5, arr = [2,  5,  3,  1]
Output: 4
Explanation: Ritu doesn't have number 4 in her collection
Expected Time Complexity: O(n)
Expected Auxillary Space: O(1)
'''

class Solution:
    def missingNumber(self, n : int, arr : List[int]) -> int:
        return (n*(n+1)//2)-sum(arr)
