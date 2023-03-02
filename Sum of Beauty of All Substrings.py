'''
Given a string S, return the sum of beauty of all its substrings.
The beauty of a string is defined as the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of string "aaac" is 3 - 1 = 2.
Example 1:

Input:
S = "aaac"
Output:
3
Explanation: The substrings with non - zero beauty are ["aaac","aac"] where beauty of "aaac" is 2 and beauty of "aac" is 1.
'''
class Solution:
    def beautySum(self, s):
        total=0
        
        length=len(s)
        
        for i in range(length-1):
            dict1=dict({s[i]:1})
            count=1
            maximum=1
            
            for j in range(i+1,length):
                if s[j] not in dict1:
                    dict1[s[j]]=1
                    minimum=1
                    count+=1
                else:
                    dict1[s[j]]+=1
                    maximum=max(maximum,dict1[s[j]])
                    
                minimum=min(dict1.values())
                if count>=2:
                    total+=(maximum-minimum)
                    
        return total
