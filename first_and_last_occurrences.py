'''
First and last occurrences of x (GFG)
Given a sorted array arr containing n elements with possibly some duplicate, the task is to find the first and last occurrences of an element x in the given array.
Note: If the number x is not found in the array then return both the indices as -1.


Example 1:

Input:
n=9, x=5
arr[] = { 1, 3, 5, 5, 5, 5, 67, 123, 125 }
Output:  
2 5
Explanation: 
First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5. 
'''
class Solution:
    def find(self,arr, n, x):
        def binary_left_search(arrx,length):
            low=0;high=length-1
            count=0
            while low<=high:
                mid=(low+high)//2
                
                if arrx[mid]==x:
                    if mid-1>=0 and arrx[mid-1]!=x:
                        return mid
                    elif mid-1>=0 and arr[mid-1]==x:
                        high=mid-1
                    elif mid-1<0:
                        return 0
                    elif mid-1==0 and arr[mid]==arr[mid-1]:
                        return 0
                elif arrx[mid]<x:
                    low=mid+1
                else:
                    high=mid-1
               
                 
        def binary_right_search(arrx,start,n):
            low=start;high=len(arrx)-1
            count=0
            while low<=high:
                mid=(low+high)//2

                if arrx[mid]==x:
                    if mid+1<n and arrx[mid+1]!=x:
                        return mid
                    elif mid+1<n and arrx[mid+1]==x:
                        low=mid+1
                    elif mid+1>=n:
                        return mid
                    elif mid+1==n-1 and arr[mid]==arr[mid+1]:
                        return n-1
                elif arrx[mid]<x:
                    low=mid+1
                else:
                    high=mid-1
                
        low=0;high=n-1
        
        first,last=None,None
        count=0
        while low<=high:
            mid=(low+high)//2
            
            if arr[mid]==x:
                if mid-1>=0 and arr[mid-1]!=x:
                    first=mid
                elif mid-1<0:
                    first=0
                elif mid-1==0 and arr[mid]==arr[mid-1]:
                    first=mid-1
                else:
                    first=binary_left_search(arr[:mid],mid)
                    
                if mid+1<n and arr[mid+1]!=x:
                    last=mid
                elif mid+1>=n:
                    last=mid
                elif mid+1==n-1 and arr[mid]==arr[mid+1]:
                    last=n-1
                else:
                    last=binary_right_search(arr,mid+1,n)
        
            elif arr[mid]<x:
                low=mid+1
            else:
                high=mid-1
            if first!=None and last!=None:
                return first,last
            
            
        return [-1,-1]
