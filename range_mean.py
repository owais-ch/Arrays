'''
Mean of range in array (GFG)

Given an array of n integers and q queries. Write a program to find floor value of mean in range l to r for each query in a new line.
Queries are given by an array queries[] of size 2*q. Here queries[2*i] denote l and queries[2*i+1] denote r for i-th query (0<= i <q).

Example 1:

Input : Arr[] = {1, 2, 3, 4, 5}, Q = 3
queries[] = {0, 2, 1, 3, 0, 4}
Output : 2 3 3
Explanation:
Here we can see that the array of 
integers is [1, 2, 3, 4, 5].
Query 1: L = 0 and R = 2
Sum = 6
Integer Count = 3
So, Mean is 2
'''
class Solution:  
    def findMean(self, arr, queries, n, q): 
        list1=[]
        
        total=0
        
        for i in range(n):
            total+=arr[i]
            list1.append(total)
        #print(list1)
        list2=[]    
        for i in range(q//2):
            start=queries[2*i]
            end=queries[2*i+1]
            if start!=0:
                start=start-1
                mean1=(list1[end]-list1[start])//(end-start)
            else:
                mean1=(list1[end])//(end+1)
            
            list2.append(mean1)
            
        return list2
