from collections import Counter

'''Given a string 's'. The task is to find the smallest window length that contains all the characters of the given string at least one time.
For eg. A = aabcbcdbca, then the result would be 4 as of the smallest window will be dbca'''

class Solution:
    def findSubString(self, str1):
        length=len(str1)
        dict1=Counter(str1)
        k=len(dict1)
        
        dict2=dict()
        count=0
        start=0
        minimum=99999
        for i in range(length):
            if count<k:
                j=start
                while j<length:
                    if str1[j] not in dict2:
                        dict2[str1[j]]=1
                        count+=1
                    else:
                        dict2[str1[j]]+=1
                        
                    if count==k:
                        #j+=1
                        break
                    j+=1
            if count==k:            
                minimum=min(minimum,j-i+1)
                #print(dict2,i,j) 
                start=j+1
                
            dict2[str1[i]]-=1
            if dict2[str1[i]]==0:
                dict2.pop(str1[i])
                count-=1
               
        return minimum
