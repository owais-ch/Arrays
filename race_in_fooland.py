'''
Race in Fooland (GFG)
Fooland city has a special multi-lane running track. Lanes are numbered from 1 to Tracks. The lanes have N horizontal barriers lying on it (due to some digging and construction work). The ith barrier cover lanes from Li1 to Li2 (both inclusive).
Also, the barriers may overlap. The athletes can’t run on the lanes on which barriers are present because they aren’t allowed to switch lanes anytime in the race. (Once a particular lane is allotted to an athlete he/she can’t switch his/her lane anytime during the race and there can be only one athlete on each lane.)

Now the race has to be organised tomorrow itself and the digging work could not be finished on time. The race would have to be organised on the same track only because Fooland city doesn’t have any other track. Help organizers in finding out how many athletes can run in a single race so that none of them would have to switch lanes.

Example 1:

Input:
N = 5, Track = 20
Li = {(1 3), (5 8), (8 13), 
           (14 15), (9 12)}

Output:
6

Explanation:
The barriers cover lanes from
 1 to 3, 5 to 8, 8 to 13, 
14 to 15 and 9 to 12. Hence, 
barriers are present on the 
lanes: {1, 2, 3, 5, 6, 7, 8,
 9, 10, 11, 12, 13, 14, 15}.

Hence, the lanes which doesn't
come under any barriers are 
{4, 16, 17, 18, 19, 20}.
So, there are 6 lanes on which
athletes can run – {4, 16, 17,
    18, 19, 20}
'''
from itertools import chain

class Solution:
    def emptyLanes(self, a, n, tracks):
        a.sort(key=lambda x:[x[0],x[1]])
        
        start=a[0][0]
        end=a[0][1]
        
        for i in range(1,n):
            if a[i][0]<end:
                a[i][0]=end  ###a[i-1][1]
                start=a[i][0]
                if a[i][1]<end:
                    a[i]=None
                else:
                    end=a[i][1]
            else:
                start=a[i][0]
                end=a[i][1]
        
        j=0
        
        for i in range(n): 
            if a[i]!=None:
                a[j],a[i]=a[i],a[j]
                j+=1

        a=a[:j]
        length=len(a)
        count=0
        
        total=tracks
        
        for i in range(length):
            if count==0:
                if i>0 and a[i][0]==a[i-1][1]:
                    total=total-(a[i][1]-a[i][0])
                else:
                    total=total-(a[i][1]-a[i][0]+1)
                count+=1
            else:
                if i>0 and a[i][0]==a[i-1][1]:
                    total=total-(a[i][1]-a[i][0])
                else:
                    total=total-(a[i][1]-a[i][0]+1)
                
        return total
 
