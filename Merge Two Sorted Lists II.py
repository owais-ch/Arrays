'''Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.

TIP: C users, please malloc the result into a new array and return the result.

If the number of elements initialized in A and B are m and n respectively, the resulting size of array A after your code is executed should be m + n

Example :

Input : 
         A : [1 5 8]
         B : [6 9]

Modified A : [1 5 6 8 9]'''

class Solution:
    def merge(self, A, B):
        length1=len(A)
        length2=len(B)

        i=0
        j=0
        list1=[]
        while i<length1 and j<length2:
            if A[i]<B[j]:
                list1.append(A[i])
                i+=1
            elif A[i]>B[j]:
                list1.append(B[j])
                j+=1
            elif A[i]==B[j]:
                list1.extend([A[i],B[j]])
                i+=1
                j+=1

        if j<length2:
            list1.extend(B[j:])
        elif i<length1:
            list1.extend(A[i:])
        A[:]=list1
        return A
