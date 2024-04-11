'''
Top k numbers in a stream (GFG)

Given N numbers in an array, your task is to keep at most the top K numbers with respect to their frequency.

In other words, you have to iterate over the array, and after each index, determine the top K most frequent numbers until that iteration and store them in an array in decreasing order of frequency. An array will be formed for each iteration and stored in an array of arrays. If the total number of distinct elements is less than K, then keep all the distinct numbers in the array. If two numbers have equal frequency, place the smaller number first in the array.

Example 1:

Input:
N=5, K=4
arr[] = {5, 2, 1, 3, 2} 
Output: 
5 
2 5 
1 2 5 
1 2 3 5 
2 1 3 5 
Explanation:
Firstly there was 5 whose frequency
is max till now. So resulting sequence is {5}.
Then came 2, which is smaller than 5 but
their frequencies are same so resulting sequence is {2, 5}.
Then came 1, which is the smallest among all the
numbers arrived, so resulting sequence is {1, 2, 5}.
Then came 3 , so resulting sequence is {1, 2, 3, 5}
Then again 2, which has the highest
frequency among all numbers, 
so resulting sequence {2, 1, 3, 5}.
'''
import math

class Solution:
    def kTop(self,arr, N, K):
        dict1=dict()
        list1=[]
        list2=[]
        maximum=-math.inf
        
        for i in range(N):
            if arr[i] not in dict1:
                dict1[arr[i]]=1
            else:
                dict1[arr[i]]+=1
                
            maximum=max(maximum,dict1[arr[i]])
            
            if i==0:
                list1.append(arr[i])
            else:
                if dict1[arr[i]]>maximum:
                    if dict1[arr[i]]>1:  
                        list1.remove(arr[i])
                    list1=list1+[arr[i]]
                elif dict1[arr[i]]==maximum:
                    if dict1[arr[i]]>1:  
                        list1.remove(arr[i])
                    list1[:]=list1+[arr[i]]
                else:
                    if dict1[arr[i]]>1:  
                        list1.remove(arr[i])
                    list1.append(arr[i])
            
            list1=sorted(list1,key=lambda x:[-dict1[x],x])
            list3=list1[:K]
            
            list2.append(list3.copy())
            
        return list2
