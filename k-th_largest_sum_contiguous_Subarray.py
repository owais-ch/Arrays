'''
K-th Largest Sum Contiguous Subarray (GFG)

You are given an array Arr of size N. You have to find the K-th largest sum of contiguous subarray within the array elements.
In other words, over all subarrays, find the subarray with k-th largest sum and return its sum of elements.
'''
 

class Solution:
    def kthLargest(self, N, K, Arr):
        list1=[]
        for i in range(N-1):
            total=Arr[i]
            list1.append(total)
            for j in range(i+1,N):
                total+=Arr[j]
                list1.append(total)
        list1.append(Arr[N-1])
        list1=sorted(list1,key=lambda x:-x)
        
        length=len(list1)
        
        if length<K:
            return list1[-1]
        
        return list1[K-1]
