'''Smallest Subarray With K Distinct Elements'''

def smallestSubarrayWithKDistinct(arr: List[int], k: int) -> List[int]:
    n=len(arr)
    count=0
    dict1=dict()
    minimum=9999999
    i=0
    start=0
    list1=[]
    while i<n:
        if arr[i] not in dict1:
            dict1[arr[i]]=1
            
            count+=1
            if count==k:
                if i-start<minimum:
                    minimum=min(minimum,i-start)
                    list1=[start,i]
                j=start
                
                while count==k and j<i:
                    
                    dict1[arr[j]]-=1
                    if dict1[arr[j]]==0:
                        #print(dict1,j,i,minimum)
                        count-=1
                        dict1.pop(arr[j])
                        if i-j<minimum:
                            minimum=i-j
                            list1=[j,i]
                            
                            #i=j
                        start=j+1
                        #print('start=',start)
                        break
                    else:
                        #print(dict1,i,j)
                        if i-j<minimum:
                            minimum=i-j
                            list1=[j,i]
                    j+=1
                start=j+1
                
                i+=1
            else:
                i+=1
        else:
            dict1[arr[i]]+=1
            i+=1
        
    if minimum==9999999:
        return [-1]
    return list1
