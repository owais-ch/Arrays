'''
Toppers Of Class(GFG)

There is a class of N students and the task is to find the top K marks scorers. You need to print the index of the toppers of the class which will be same as the index of the student in the input array (use 0-based indexing). 
First print the index of the students having highest marks then the students with second highest and so on. If there are more than one students having same marks then print their indices in ascending order.Suppose k = 2 and the students having highest marks have 
indices 0 and 5 and students having second highest marks have indices 6 and 7 then output will be 0 5 6 7.

Example 1:

Input:
N=5 K=3
arr[] = { 2, 2, 1, 3, 1 }
Output: 3 0 1 2 4
Explanation: Topper with 3 marks is present 
at 3rd index, 2 marks is present at 0th 
index and next at 1st index. 1 marks is present 
at 2 and 4.
'''
def kTop(a,n):        
    a.sort(key=lambda x:-x[0])
