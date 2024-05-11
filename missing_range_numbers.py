'''
Missing ranges of numbers (GFG)

Given an array Arr of N positive integers, find the missing elements (if any) in the range 0 to max of Arri.

Example 1:

Input:
N = 5
Arr[] = {62, 8, 34, 5, 332}
Output: 0-4 6-7 9-33 35-61 63-331
Explanation: Elements in the range 0-4, 6-7, 
9-33, 35-61 and 63-331 are not present.

Example 2:

Input:
N = 4
Arr[] = {13, 0, 32, 500}
Output: 1-12 14-31 33-499
Explanation: Elements in the range 1-12, 
14-31 and 33-499 are not present.
'''

import math

class Solution:
    def findMissing(self, arr, n):
        if n==1 and arr[0]==0:
            return -1
            
        arr.sort()
        
        start=0
           
        list2=[]
        for i in range(n):
            if i==0:
                gap_start=0
                gap_end=arr[i]
                list2.append([gap_start,gap_end])
            else:
                gap_start=arr[i-1]
                gap_end=arr[i]  
                list2.append([gap_start,gap_end])
                
        string1=''
        
        for i in range(n):
            if i==0:
                begin=0
                end=list2[i][1]
                start_element=begin
                end_element=end-1
                if end_element>start_element:
                    string1=string1+'{}-{} '.format(start_element,end_element)
                elif end_element==start_element:
                    string1=string1+'{} '.format(start_element)
            else:
                begin=list2[i-1][1]
                end=list2[i][1]
                
                start_element=begin+1
                end_element=end-1
                if end_element>start_element:
                    string1=string1+'{}-{} '.format(start_element,end_element)
                elif end_element==start_element:
                    string1=string1+'{} '.format(start_element)
                
        
        return string1
