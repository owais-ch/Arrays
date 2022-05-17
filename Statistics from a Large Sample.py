'''You are given a large sample of integers in the range [0, 255]. Since the sample is so large, it is represented by an array count where count[k] is the number of times that k appears in the sample.

Calculate the following statistics:

minimum: The minimum element in the sample.
maximum: The maximum element in the sample.
mean: The average of the sample, calculated as the total sum of all elements divided by the total number of elements.
median:
If the sample has an odd number of elements, then the median is the middle element once the sample is sorted.
If the sample has an even number of elements, then the median is the average of the two middle elements once the sample is sorted.
mode: The number that appears the most in the sample. It is guaranteed to be unique.
Return the statistics of the sample as an array of floating-point numbers [minimum, maximum, mean, median, mode]. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input: count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: [1.00000,3.00000,2.37500,2.50000,3.00000]
Explanation: The sample represented by count is [1,2,2,2,3,3,3,3].
The minimum and maximum are 1 and 3 respectively.
The mean is (1+2+2+2+3+3+3+3) / 8 = 19 / 8 = 2.375.
Since the size of the sample is even, the median is the average of the two middle elements 2 and 3, which is 2.5.
The mode is 3 as it appears the most in the sample.'''

class Solution:
    def sampleStats(self, count):
        length=256
    
        total_sum=0
        totalz=0
        
        max_count=0
        first=0
        medianz=0
        start=0
        end=0
        dict1={}
        dict2={}
        total_end=0
        for i in range(length):
            if count[i]>0:
                
                total_sum+=count[i]*i
                totalz+=count[i]
                if first==0:
                    minimum=i
                    first=1
                maximum=i
                end+=count[i]
                dict1[i]=start
                dict2[i]=end
                start=end+1
                total_end=end
                
                
                        
                    
            if count[i]>=max_count:
                max_count=count[i]
                mode=i
                
        if total_end%2==0:
            position=total_end/2
            count=0
            for i in dict1:
                if position>=dict1[i] and position<=dict2[i]:
                    medianz=i
                    count+=1
                if position+1>=dict1[i] and position+1<=dict2[i]:
                    medianz+=i
                    count+=1
                    
                if count==2:
                    break
            medianz=medianz/2
        else:
            position=total_end//2+1
            for i in dict1:
                if position>=dict1[i] and position<=dict2[i]:
                    medianz=i
                    break
                
            
        mean=total_sum/totalz       
        return [minimum,maximum,mean,medianz,mode]
