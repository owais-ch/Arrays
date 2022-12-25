'''Given an array of integers of size, N. Assume ‘0’ as the invalid number and all others as a valid number. Write a program that modifies the array in such a way that 
if the next number is a valid number and is the same as the current number, double the current number value and replace the next number with 0. After the modification, 
rearrange the array such that all 0’s are shifted to the end and the sequence of the valid number or new doubled number is maintained as in the original array.

Example 1:

â€‹Input : arr[ ] = {2, 2, 0, 4, 0, 8}
Output : 4 4 8 0 0 0
Explanation:
At index 0 and 1 both the elements are same.
So, we can change the element at index 0 to 
4 and element at index 1 is 0 then we shift 
all the values to the end of the array. 
So, array will become [4, 4, 8, 0, 0, 0].
'''

class Solution:
    def modifyAndRearrangeArr (self, arr,  n) : 
        for i in range(n-1):
            if arr[i]==arr[i+1] and arr[i]!=0:
                arr[i]=arr[i]*2
                arr[i+1]=0
                
        j=0
        for i in range(n):
            if arr[i]!=0:
                arr[i],arr[j]=arr[j],arr[i]
                j+=1
        return arr
