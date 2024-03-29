'''
CodeMart is a shopping platform and it is distributing gift vouchers to its esteemed users. The voucher can be redeemed by providing a fixed amount of shopping credits to the platform. One credit is sent by a user to the platform by doing one occurance in CodeMart. 
Since there is a huge rush of people you are required to manage the users on the basis of first come first serve. The user which came first and has exactly k occurrences at last is given the voucher first. You are given an array arr[ ] with the id's of N users in
chronological order of their occurances . You are required to print the id of the user which will be given the voucher first. If no such user meets the condition print "-1".

Example 1:

Input:
N = 7 
K = 2
arr[] = {1, 7, 4, 3, 4, 8, 7} 
Output: 7
Explanation: Both 7 and 4 occur 2 times.
But 7 is the first that occurs 2 times. 
'''
from collections import OrderedDict
class Solution:
    def firstElement(self, arr, n, k): 
        dict1=OrderedDict()
        
        for i in range(n):
            if arr[i] not in dict1:
                dict1[arr[i]]=1
            else:
                dict1[arr[i]]+=1
                
        for i in dict1:
            if dict1[i]==k:
                return i
        return -1
