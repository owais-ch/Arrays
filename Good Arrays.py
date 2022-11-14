'''Good Arrays'''

def goodArrays(a, n) :
    total=sum(a)
    total_odd=sum([a[i] for i in range(n) if i%2!=0])
    total_even=total-total_odd
    
    tot_even=0
    tot_odd=0
    
    count=0
    
    for i in range(n):
        even=tot_even+total_odd-tot_odd
        
        if i%2==0:
            tot_even+=a[i]
        else:
            tot_odd+=a[i]
            
        odd=tot_odd+total_even-tot_even
        
        
        if even==odd:
            count+=1
        
        
    return count
