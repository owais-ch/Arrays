'''
Missing Intervals (GFG)
Given a sorted array A[] of N distinct integers from 0 to 99999. Find all the integer intervals missing from the given list.
Note: There is always atleast 1 number missing.


Example 1:

Input:
N = 4
A = {1,5,67,88}
Output:
0,2-4,6-66,68-87,89-99999
Explanation:
All the missing Intervals are printed.
'''
class Solution:
    def printMissingIntervals(self, a , n):
        list1=[]
        
        for i in range(n):
            if i==0:
                end=a[i]
                start=0
                if end-start==1:
                    #list1.append(str(start))
                    list1.extend([start,start])
                elif end-start>1:
                    #list1.append(str(start)+'-'+str(end-1))
                    list1.extend([start,end-1])
                start=end+1
            else:
                end=a[i]
                
                if end-start==1:
                    #list1.append(str(start))
                    list1.extend([start,start])
                elif end-start>1:
                    #list1.append(str(start)+'-'+str(end-1))
                    list1.extend([start,end-1])
                    
                start=end+1
        #list1.append(str(start)+'-'+str(99999))
        if a[-1]!=99999:
            list1.extend([start,99999])
        return list1
