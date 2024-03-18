'''Hands of Straights (GFG)
Alice has some cards, each card has one number written on it. She wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
Given an integer array hand of size N where hand [ i ] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

Example 1:

Input:
N = 9
groupSize = 3
hand[ ] = {1, 2, 3, 6, 2, 3, 4, 7, 8}
Output: true
Explanation: 
Alice's hand can be rearranged as {1, 2, 3} , {2, 3, 4}, {6, 7, 8}. There are three groups with size 3. Each group has 3 consecutive cards.
'''
import math
from collections import Counter,OrderedDict
class Solution:
    def isStraightHand(self,N, groupSize, hand):
        if groupSize==1:
            return  True
        elif N%groupSize!=0:
            return False
    
        hand.sort()
        minimum=hand[0]
        
        dict1=OrderedDict(Counter(hand))
        total=sum(dict1.values())
        num_elements=len(dict1)
           
        count=0
        start=hand[0]
        value=start
        
        while total!=0:
            if count==0:
                dict1[value]-=1
                if dict1[value]==0:
                    start=value+1
                count+=1
                value+=1
                total-=1
            else:
                if value not in dict1:
                    return False
                elif dict1[value]==0:
                    return False
                else:
                    dict1[value]-=1
                    count+=1
                    total-=1
                    
                    if dict1[value]==0 and value==start:
                        start+=1
                    elif dict1[value]==0 and value!=start:
                        return False
                    
                    if count==groupSize:
                        count=0
                        value=start

                        while value not in dict1 and total!=0:
                            value+=1
                    else:
                        value+=1
        if count>0:
            return False
        return True
