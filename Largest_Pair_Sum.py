'''
Largest Pair Sum (GFG)
Find the largest pair sum in an array of distinct integers.

Examples :

Input: arr[] = [12, 34, 10, 6, 40]
Output: 74
Explanation: Sum of 34 and 40 is the largest,i.e, 34+40=74.
'''

class Solution:
    def pairsum(self, arr : List[int]) -> int:
        n=len(arr)
        
        maximum=-1
        second_maximum=-1
        
        for i in range(n):
            if i==0:
                maximum=arr[i]
            else:
                if arr[i]>maximum:
                    second_maximum=maximum
                    maximum=arr[i]
                elif arr[i]>second_maximum:
                    second_maximum=arr[i]
                    
        return maximum+second_maximum
