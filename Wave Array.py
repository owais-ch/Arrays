'''Given an array of integers,  sort the array into a wave like array and return it, 

In other words, arrange the elements into a sequence such that  a1 >= a2 <= a3 >= a4 <= a5.....

Example

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
NOTE : If there are multiple answers possible, return the one thats lexicographically smallest. 

So, in example case, you will return [2, 1, 4, 3]'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()

        length=len(A)
        list1=[]
        list2=[]

        for i in range(length):
            if i%2==0:
                list1.append(A[i])
            else:
                list2.append(A[i])
        
        list3=[]

        count1=0
        count2=0

        for i in range(length):
            if i%2==0:
                if count2<len(list2):
                    list3.append(list2[count2])
                    count2+=1
                elif count1<len(list1):
                    list3.append(list1[count1])
                    count1+=1
            else:
                if count1<len(list1):
                    list3.append(list1[count1])
                    count1+=1
                elif count2<len(list2):
                    list3.append(list2[count2])
                    count2+=1
        
        return list3
