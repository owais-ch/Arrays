'''
Problem 4: Transform Array by Adding a Constant
You are given an array A of size n and an integer d. In one operation, you can:

Add or subtract d to any element of the array.
Determine the minimum number of operations required to make all elements of the array equal.
'''

class Solution:
    def transform_arr(self,arr,n,x):
        arr.sort()

        for i in range(1,n):
            if (arr[i]-arr[i-1])%x!=0:
                return -1
            
        middle_index=n//2

        count=0

        for i in range(n):
                count+=abs(arr[middle_index]-arr[i])//x
        return count
    
        
obj=Solution()
print("minimum_number of operations for the transformation is ",obj.transform_arr([1,7,13,25,37,55],6,3))


