'''
Majority Element II (GFG)
You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

Note: The answer should be returned in an increasing format.

Examples:

Input: arr[] = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Output: [5, 6]
Explanation: 5 and 6 occur more n/3 times.
Input: arr[] = [-5, 1, -5]
Output: -5
Explanation: -5 occurs more than n/3 times.
Input: arr[] = [1, 2, 3, 4, 5]
Output: []
Explanation: no candidate occur more than n/3 times.
'''

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        dict1=dict()
        
        n=len(arr)
        
        for i in range(n):
            if arr[i] not in dict1:
                dict1[arr[i]]=1
            else:
                dict1[arr[i]]+=1
                
        result_list=[]
        
        for i in dict1:
            if dict1[i]>n/3:
                result_list.append(i)
                
        return sorted(result_list)
