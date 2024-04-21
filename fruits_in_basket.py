'''
Fruit Into Baskets (GFG)

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits of size N, where fruits[i]  is the type of fruit the ith tree produces.
You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow :

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of the baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.


Example 1:

Input:
N = 3
fruits [ ] = { 2, 1, 2 }
Output: 3
Explanation: We can pick from all three trees. 
'''

class Solution:
    def sumSubarrayMins(self, n, arr):
        count=0
        maximum=0
        diff_count=0
        
        type1=arr[0]
        index1=0
        type2=None
        index2=None
        
        for i in range(1,n):
            if arr[i]!=type1:
                type2=arr[i]
                index2=i
                break
            else:
                index1=i
        
        count=i+1
        
        if type2==None:
            return n
            
        for j in range(i+1,n):
            if arr[j]==type1:
                count+=1
                index1=j
            elif arr[j]==type2:
                count+=1
                index2=j
            else:
                maximum=max(maximum,count)
                if index1>index2:
                    count=j-index2
                    type2=arr[j]
                    index2=j
                elif index1<index2:
                    count=j-index1
                    
                    type1=type2
                    index1=index2
                    
                    type2=arr[j]
                    index2=j
            
        maximum=max(maximum,count)
        
        return maximum
        
