'''
Distinct Difference (GFG)

Given an array A[] of length N. For each index, i (1<=i<=N), find the difference between the number of distinct elements in the left and right side in the of the current element in the array. 

Example 1:

Input:
N = 3
arr[] = {4, 3, 3}
Output: {-1, 0, 2}
Explanation: For index i=1, there are 0 distinct element in the left side of it, and 1 distinct element(3) in it's right side. So difference is 0-1 = -1. 

Similarly for index i=2, there is 1 distinct element (4) in left side of it, and 1 distinct element(3) in it's right side. So difference is 1-1 = 0.

Similarly for index i=3, there are 2 distinct elements (4 and 3) in left side of it, and 0 distinct elements in it's left side. So difference is 2-0 = 2.
'''
class Solution:
    def getDistinctDifference(self, N, arr):
        set1=set()
        set2=set()
        
        list1,list2=[0]*N,[0]*N
        
        i,j=0,N-1
        count1,count2=0,0
        
        while i<N and j>=0:
            if arr[i] not in set1:
                set1.add(arr[i])
                count1+=1
            
            list1[i]=count1
            i+=1
            
            if arr[j] not in set2:
                set2.add(arr[j])
                count2+=1
            
            list2[j]=count2
            j-=1
        
        list3=[]
        
        for i in range(N):
            if i==0:
                list3.append(0-list2[1])
            elif i==N-1:
                list3.append(list1[N-2])
            else:
                list3.append(list1[i-1]-list2[i+1])
        
        return list3
