'''Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.'''

from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        list1=list(map(lambda x:Counter(x),words))
        
        length=len(words)
        
        list2=[]
        
        for j in list1[0]:
            minimum=999999
            decider=0
            for i in range(1,length):
                if j in list1[i]:
                    minimum=min(minimum,min(list1[0][j],list1[i][j]))
                    decider=1
                else:
                    decider=0
                    break
                    
            if decider==1:
                list2.extend([j]*minimum)
                
        return list2
