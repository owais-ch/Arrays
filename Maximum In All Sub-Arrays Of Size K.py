'''Maximum In All Sub-Arrays Of Size K'''

def getMaximumOfSubarrays(arr, k):
    length=len(arr)
    
    if arr==sorted(arr,reverse=True):
        return arr[:length-k+1]
    
    maximum=max(arr[:k])
    indexz=arr[:k].index(maximum)
    
    
    
    list1=[0]*(length-k+1)
    list1[0]=maximum
    
    for i in range(1,length-k+1):
        if arr[i+k-1]>maximum:
            maximum=arr[i+k-1]
            indexz=i+k-1
            list1[i]=maximum
        elif indexz<i:
            maximum=max(arr[i:i+k])
            indexz=indexz+1+arr[i:i+k].index(maximum)
            list1[i]=maximum
        else:
            list1[i]=maximum

    return list1
