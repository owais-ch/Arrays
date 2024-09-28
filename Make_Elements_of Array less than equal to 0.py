'''
Minimum operations required to make all elements of Array less than equal to 0

Given an array arr[] consisting of N positive numbers, the task is to find the minimum number of operations required to make all elements of the array less than or equal to 0.
In each operation, one has to pick the minimum positive element from the array and subtract all the elements of the array from that number.

Examples:


Input: arr[] = {1, 2, 4, 2, 2, 5, 6}
Output: 5
Explanation: The explanation is mentioned in the diagram below: 
'''

class Solution:
    def Make_arr_Zero(self, arr, n):
        # Use a set to track distinct positive elements
        positive_values = set()
        
        for num in arr:
            if num > 0:
                positive_values.add(num)
        
        # The number of distinct positive elements is the number of operations
        return len(positive_values)

obj=Solution()
print("minim um_operations= ",obj.Make_arr_Zero([1, 2, 4, 2, 2, 5, 6],7))
