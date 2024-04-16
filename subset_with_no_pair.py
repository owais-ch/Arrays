'''
Subset with no pair sum divisible by K (GFG)

Given an array of integers the task is to find maximum size of a subset such that sum of each pair of this subset is not divisible by K.
 

Example 1:

Input : 
arr[] = [3, 7, 2, 9, 1]       
K = 3
Output : 
3
Explanation:
Maximum size subset whose each pair sum
is not divisible by K is [3, 7, 1] because,
3+7 = 10,   
3+1 = 4,   
7+1 = 8 
These all are not divisible by 3.
It is not possible to get a subset of size
bigger than 3 with the above-mentioned property.
'''

def subsetPairNotDivisibleByK(a, N, K):
    a=[i%K for i in a]
    
    dict1=dict()
    count=0
    for i in range(N):
        if a[i] not in dict1:
            dict1[a[i]]=1
        else:
            dict1[a[i]]+=1
            
    else_total=0
    
    for i in range(K//2+1):
        if i in dict1:
            if i==0:
                count+=1
            else:
                if K-i in dict1 and K-i==i:
                    count+=1
                elif K-i in dict1:
                    count+=max(dict1[i],dict1[K-i])
                else:
                    count+=dict1[i]
                    #else_total+=1
        elif K-i in dict1:
            count+=dict1[K-i]
                    
                  
    return count
