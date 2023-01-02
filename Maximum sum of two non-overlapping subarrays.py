import math
def maxSumTwoSubarray(arr, N, K):
    first=sum(arr[:K])
    list1=[first]
    
    for i in range(1,N-K+1):
        first=first-arr[i-1]+arr[i+K-1]
        list1.append(first)
        
    length2=len(list1)
    
    maximum=-math.inf
    
    if K>length2:
        return -1000000000
    
    max_value=max(list1[K:])
    indexz=K+list1[K:].index(max_value)
    
    for i in range(length2-K):
        
        if indexz-i>=K:
            #print(list1[i],max_value)
            maximum=max(maximum,list1[i]+max_value)
        else:
            max_value=max(list1[i+K:])
            indexz=i+K+list1[i+K:].index(max_value)
            maximum=max(maximum,list1[i]+max_value)
    
    if indexz-i>=K:
        maximum=max(maximum,list1[i]+max_value)        
    return maximum
