'''
Maximize The Array (GFG)

Given two integer arrays Arr1 and Arr2 of size N. Use the greatest elements from the given arrays to create a new array of size N such that it consists of only unique elements and the sum of all its elements is maximum.
The created elements should contain the elements of Arr2 followed by elements of Arr1 in order of their appearance.

Note: The input array will be given in such way, that every time it is possible to make a new arr by maintaing the following conditions.


Example 1:

Input:
N = 5
Arr1 = {7, 4, 8, 0, 1}
Arr2 = {9, 7, 2, 3, 6}
Output: 9 7 6 4 8
Explanation: 9, 7, 6 are from 2nd array
and 4, 8 from 1st array.
'''

class Solution:
    def maximizeArray(self, arr1, arr2, n):
        arr11=sorted(enumerate(set(arr1)),key=lambda x:x[1])
        arr22=sorted(enumerate(set(arr2)),key=lambda x:x[1])
        dict_index1=dict()
        dict_index2=dict()
        
        for i in range(n):
            if arr1[i] not in dict_index1:
                dict_index1[arr1[i]]=i
            if arr2[i] not in dict_index2:
                dict_index2[arr2[i]]=i
                
        length=0
        
        i,j=len(arr11)-1,len(arr22)-1
        list1=[]
        list2=[]
        dict1=dict()
        while i>=0 and j>=0:
            if arr11[i][1]>arr22[j][1]:
                if arr11[i][1] not in dict1:
                    list1.append(arr11[i])
                    dict1[arr11[i][1]]=1
                    length+=1
                i-=1
            elif arr11[i][1]<arr22[j][1]:
                if arr22[j][1] not in dict1:
                    list2.append(arr22[j])
                    dict1[arr22[j][1]]=1
                    length+=1
                j-=1
            else:
                if arr22[j][1] not in dict1:
                    list2.append(arr22[j])
                    dict1[arr22[j][1]]=1
                    length+=1
                i-=1
                j-=1
            
            if length==n:
                list2=[(dict_index2[k[1]],k[1]) for k in list2]
                list1=[(dict_index1[k[1]],k[1]) for k in list1]
                
                return [q[1] for q in sorted(list2,key=lambda x:x[0])]+[p[1] for p in sorted(list1,key=lambda x:x[0])]    
        
        if i<0:
            while j>=0:
                if arr22[j][1] not in dict1:
                    list2.append(arr22[j])
                    dict1[arr22[j][1]]=1
                    length+=1
                j-=1
                
                if length==n:
                    list2=[(dict_index2[k[1]],k[1]) for k in list2]
                    list1=[(dict_index1[k[1]],k[1]) for k in list1]
                    return [q[1] for q in sorted(list2,key=lambda x:x[0])]+[p[1] for p in sorted(list1,key=lambda x:x[0])]    
        elif j<0:
            while i>=0:
                if arr11[i][1] not in dict1:
                    list1.append(arr11[i])
                    dict1[arr11[i][1]]=1
                    length+=1
                i-=1
            
                if length==n:
                    list2=[(dict_index2[k[1]],k[1]) for k in list2]
                    list1=[(dict_index1[k[1]],k[1]) for k in list1]
                    return [q[1] for q in sorted(list2,key=lambda x:x[0])]+[p[1] for p in sorted(list1,key=lambda x:x[0])]    
        list2=[(dict_index2[k[1]],k[1]) for k in list2]
        list1=[(dict_index1[k[1]],k[1]) for k in list1]
          
        return [q[1] for q in sorted(list2,key=lambda x:x[0])]+[p[1] for p in sorted(list1,key=lambda x:x[0])]   
