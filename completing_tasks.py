'''
Completing Tasks (GFG)
There are total n tasks given to a group of 5 students in a class. Three of those five students completed m tasks of their choices and left the group. Now the burden of completing remaining tasks is on the two students Tanya and Manya.
Suppose the n tasks are in an array form 1,2,3,...n. Tanya and Manya decided to complete their remaining tasks in the following manner :- First of the remaining task is done by Tanya and the next remaining one by Manya .
For example if n = 10 and m = 4 and the completed 4 tasks are {2, 3, 5, 7} then the reamining tasks are {1, 4, 6, 8, 9, 10} so, Tanya completes {1, 6, 9} tasks and Manya completes {4, 8, 10} tasks and thereby completing the n tasks given.

Given n, m and the indexes (1 for first task, 2 for second task and so on..) of completed tasks, find the tasks which Tanya and Manya have to complete.

Example 1:

Input:
n = 15, m = 6
arr[] = {2, 5, 6, 7, 9, 4}
Output: 
1 8 11 13 15 
3 10 12 14 
Explanation: The remaining tasks are :
{1, 3, 8, 10, 11, 12, 13, 14, 15}.
So Tanya should take these tasks :
{1, 8, 11, 13, 15}.
And Manya should take these tasks :
{3, 10, 12, 14}.
'''
from collections import Counter
# return [[tanya's tasks], [manya's tasks]]
class Solution:
    def solve(self, arr, n, m):

        dict1=Counter(arr)
        count=0
        list1,list2=[],[]
        for i in range(1,n+1):
            if i not in dict1:
                if count%2==0:
                    list1.append(i)
                else:
                    list2.append(i)
                count+=1
                
                    
        return list1,list2
    
        
        
        count=0
        list1=[]
        list2=[]
        arr=list(set(arr))
        arr.sort()
        j=0
        length=len(arr)
        for i in range(1,n+1):
            if j<length and arr[j]==i:
                j+=1
            else:
                count+=1
                if count%2!=0:
                    list1.append(i)
                else:
                    list2.append(i)
                    
        return list1,list2
