'''Smallest greater elements in whole array
Given an array A of N length. We need to calculate the next smallest greater element for each element in a given array. If the next greater element is not available in a given array then we need to fill -10000000 at that index place.

Example 1:

Input : arr[] = {13, 6, 7, 12}
Output : _ 7 12 13 
Explanation:
Here, at index 0, 13 is the greatest value 
in given array and no other array element 
is greater from 13. So at index 0 we fill 
'-10000000'.'''

def greaterElement (arr,  n) : 
    list1=sorted(enumerate(arr),key=lambda x:x[1])
    list2=[-10000000]*n
    
    for i in range(n):
        j=i+1
        while j<n:
            if list1[j][1]>list1[i][1]:
                list2[list1[i][0]]=list1[j][1]
                break
            j+=1
           
    return list2
