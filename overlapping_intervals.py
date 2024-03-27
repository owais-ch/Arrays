'''
Overlapping Intervals (GFG)

Given a collection of Intervals, the task is to merge all of the overlapping Intervals.

Example 1:

Input:
Intervals = {{1,3},{2,4},{6,8},{9,10}}
Output: {{1, 4}, {6, 8}, {9, 10}}
Explanation: Given intervals: [1,3],[2,4]
[6,8],[9,10], we have only two overlapping
intervals here,[1,3] and [2,4]. Therefore
we will merge these two and return [1,4],
[6,8], [9,10].
'''
class Solution:
	def overlappedInterval(self, Intervals):
		Intervals.sort(key=lambda x:[x[0],x[1]])
		length=len(Intervals)
        
        start=Intervals[0][0];end=Intervals[0][1]
        list1=[]
        
        for i in range(1,n):
            if Intervals[i][0]>end:
                list1.append([start,end])
                start=Intervals[i][0]
                end=Intervals[i][1]
            elif start<=Intervals[i][0]<=end and Intervals[i][1]>end:
                end=Intervals[i][1]
            elif start<=Intervals[i][0]<=Intervals[i][1]<=end:
                pass
        if list1==[]:
            list1.append([start,end])
        elif start>list1[-1][-1]:
            list1.append([start,end])
        elif end>=list1[-1][-1]:
            list1.append([start,end])
        return list1
