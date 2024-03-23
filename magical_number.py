'''
Magical Number (GFG)
Your friend loves magic and he has coined a new term - "Magical number". To perform his magic, he needs that magic number. You are given a sorted array arr of distinct integers. A number arr[i] is a magical number if arr[i] = i (0-based indexing).
You have to return the leftmost magical number present in the given array arr, if there is no magical number in the array arr then return -1

Example1:

Input:
N = 5
arr = {-2, -1, 2, 4, 6}
Output: 2
Explanation: there is only one magical number present at index 2 because arr[2] = 2.
'''
class Solution:
    def findMagicalNumber(self, N : int, arr : List[int]) -> int:
        low=0
        high=N-1
        
        while low<=high:
            mid=(low+high)//2
            
            if arr[mid]==mid:
                if mid-1<0:
                    return arr[mid]
                elif arr[mid-1]<mid-1:
                    return arr[mid]
                else:
                    high=mid-1
            elif arr[mid]>mid:
                high=mid-1
            elif arr[mid]<mid:
                low=mid+1
        
        return -1
