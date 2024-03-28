'''
Roll the characters of a String (GFG)
Given a string S and an array roll where roll[i] represents rolling first roll[i] characters in the string, the task is to apply every roll[i] on the string and output the final string. Rolling means increasing the ASCII value of character, like rolling z would result in a, rolling b would result in c, etc.

Example 1:

Input: s = "bca"
roll[] = {1, 2, 3} 
Output: eeb
Explanation: arr[0] = 1 means roll 
first character of string -> cca
arr[1] = 2 means roll 
first two characters of string -> dda
arr[2] = 3 means roll
first three characters of string -> eeb
So final ans is "eeb".
'''
class Solution:
    def findRollOut(self, s, roll, n):
        dict1=dict(zip(list('abcdefghijklmnopqrstuvwxyz'),[i for i in range(1,27)]))
        dict2=dict(zip([i for i in range(1,27)],list('abcdefghijklmnopqrstuvwxyz')))
        dict1['z']=0
        dict2[0]='z'
        maximum=max(roll)
        list2=[0 for i in range(1,n+1)]
        
        for i in range(n):
            list2[roll[i]-1]+=1
            
        #print(list2)    
        
        total=0    
        
        for i in range(-1,-n-1,-1):
            total+=list2[i]
            list2[i]=total
            
        #print(list2)    
        
        list1=[]
        for i in range(n):
            #print((dict1[s[i]],list2[i]))
            list1.append(dict2[(dict1[s[i]]+list2[i])%26])
            
        return ''.join(list1)
