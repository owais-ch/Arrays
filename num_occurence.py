'''Number of occurrence (GFG)

Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.

Example 1:

Input:
N = 7, X = 2
Arr[] = {1, 1, 2, 2, 2, 2, 3}
Output: 4
Explanation: 2 occurs 4 times in the
given array.'''

class Solution:
	def count(self,arr, n, x):
        if x>arr[-1] or x<arr[0]:
            return 0

        def binary_left(a,end):
            low=0
            high=end

            while low<=high:
                mid=(low+high)//2

                if arr[mid]==x and mid-1>=0 and arr[mid-1]!=x:
                    return mid
                elif arr[mid]==x and mid-1<0:
                    return mid
                elif arr[mid]!=x and arr[mid+1]==x:
                    return mid+1
                elif arr[mid]==x:
                    high=mid-1
                elif arr[mid]<x:
                    low=mid+1

        def binary_right(a,start):
            low=start
            high=n-1

            while low<=high:
                mid=(low+high)//2

                if arr[mid]==x and mid+1<n and arr[mid+1]!=x:
                    return mid
                if arr[mid]==x and mid+1>=n:
                    return mid
                elif arr[mid]!=x and arr[mid-1]==x:
                    return mid-1
                elif arr[mid]>x:
                    high=mid-1
                elif arr[mid]==x:
                    low=mid+1

        low=0
        high=n-1

        while low<=high:
            mid=(low+high)//2

            if arr[mid]==x:
                left=binary_left(arr,mid)
                right=binary_right(arr,mid+1)
                if left==None:
                    return n-right+1
                elif right==None:
                    return n-left
                
                return right-left+1
            elif arr[mid]>x:
                high=mid-1
            elif arr[mid]<x:
                low=mid+1
                
        return 0
