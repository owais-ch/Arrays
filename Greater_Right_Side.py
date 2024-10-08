'''
Greater on Right Side (GFG)

You are given an array arr. Replace every element with the next greatest element (the greatest element on its right side) in the array. Note: There is no element next to the last element, so replace it with -1.

Example:

Input: arr[] = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 5, 5, 2, -1]
Explanation: For 16 the greatest element 
on its right is 17. For 17 it's 5. 
For 4 it's 5. For 3 it's 5. For 5 it's 2. 
For 2 it's -1(no element to its right). 
'''

class Solution:
	def nextGreatest(self,arr):
	    n=len(arr)
	    
  		for i in range(-1,-n-1,-1):
  		    if i==-1:
  		        maximum=arr[i]
  		        arr[i]=-1
  		    else:
  		        temp=arr[i]
  		        arr[i]=maximum
  		        if temp>arr[i]:
  		            maximum=temp
  		            
      return arr
