'''
Ceil The Floor (GFG)

Given an unsorted array arr[] of integers and an integer x, find the floor and ceiling of x in arr[].

Floor of x is the largest element which is smaller than or equal to x. Floor of x doesn’t exist if x is smaller than smallest element of arr[].
Ceil of x is the smallest element which is greater than or equal to x. Ceil of x doesn’t exist if x is greater than greatest element of arr[].

Return an array of integers denoting the [floor, ceil]. Return -1 for floor or ceiling if the floor or ceiling is not present.

Examples:

Input: x = 7 , arr[] = [5, 6, 8, 9, 6, 5, 5, 6]
Output: 6, 8
Explanation: Floor of 7 is 6 and ceil of 7 is 8.
Input: x = 10 , arr[] = [5, 6, 8, 8, 6, 5, 5, 6]
Output: 8, -1
Explanation: Floor of 10 is 8 but ceil of 10 is not possible.
'''

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        x_floor=-1
        x_ceil=-1
        n=len(arr)
        
        for i in range(n):
            if arr[i]<x:
                if x_floor==-1:
                    x_floor=arr[i]
                else:
                    if arr[i]>x_floor:
                        x_floor=arr[i]
            
            elif arr[i]>x:
                if x_ceil==-1:
                    x_ceil=arr[i]
                else:
                    if arr[i]<x_ceil:
                        x_ceil=arr[i]
                        
            else:
                if x_floor==-1:
                    x_floor=arr[i]
                else:
                    if arr[i]>x_floor:
                        x_floor=arr[i]
                        
                if x_ceil==-1:
                    x_ceil=arr[i]
                else:
                    if arr[i]<x_ceil:
                        x_ceil=arr[i]
                return x_floor,x_ceil
                
        return x_floor,x_ceil
