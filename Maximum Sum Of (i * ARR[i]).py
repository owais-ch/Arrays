'''Maximum Sum Of (i * ARR[i]) Among All Possible Rotations Of An Array'''

def maxmValueAmongAllRotations(arr, n):
    pro=0
    for i in range(n):
        pro=pro+(arr[i]*i)
       
    maximum=pro
    total=sum(arr)
    
    j=n-1
    
    for i in range(n-1):
        total=total-arr[j]
        pro=pro-(arr[j]*(n-1))+total
        total+=arr[j]
        maximum=max(maximum,pro)
        j-=1
    return maximum
