'''
Given array A[] of integers, the task is to complete the function findMaxDiff which finds the maximum absolute difference between nearest left and right 
smaller element of every element in array.If the element is the leftmost element, nearest smaller element on left side is considered as 0. Similarly if the 
element is the rightmost elements, smaller element on right side is considered as 0.

Examples:

Input : arr[] = {2, 1, 8}
Output : 1
Left smaller  LS[] {0, 0, 1}
Right smaller RS[] {1, 0, 0}
Maximum Diff of abs(LS[i] - RS[i]) = 1 
'''


class Solution:
    # Your task is to complete this function
    # Function should return an integer denoting the required answer
    def findMaxDiff(self, arr, n):
        stack=[0,arr[0]]
        list1=[]
        
        for i in range(n):
            if i==0:
                list1.append(0)
            else:
                while stack!=[]:
                    if stack[-1]<arr[i]:
                        list1.append(stack[-1])
                        stack.append(arr[i])
                        break
                    else:
                        stack.pop()
        
        stack=[0,arr[-1]]   
        list2=[0]*n
        
        for j in range(-1,-n-1,-1):
            if j==-1:
                list2[j]=0
            else:
                while stack!=[]:
                    if stack[-1]<arr[j]:
                        list2[j]=stack[-1]
                        stack.append(arr[j])
                        break
                    else:
                        stack.pop()
        
        maximum=-1
        
        for i in range(n):
            maximum=max(maximum,abs(list1[i]-list2[i]))
                
        return maximum
