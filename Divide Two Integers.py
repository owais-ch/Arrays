'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
'''

class Solution:
    def divide(self, dividend: int, divid: int) -> int:
        #dividend=2147483648
        if dividend==-2147483648 and divid==-1:
            return 2147483647
        valx=1
        valy=1
        if divid<0:
            divid=abs(divid)
            valx=-1
        if dividend<0:
            dividend=abs(dividend)
            valy=-1
        arr=list(map(int,str(dividend)))

        length=len(arr)

        i=0
        list1=[]

        value=''

        while i<length:
            start=0
            end=arr[i]
            value+=str(arr[i])
            count=0
            if divid<=int(value):
                end=int(value)
                value2=value
                
                while start<=end:
                    start+=divid
                    if start<=end:
                        count+=1
                    else:
                        start-=divid
                        value=str(end-start)
                        break
                    end-=divid
                    if start<=end:
                        count+=1
                    else:
                        end+=divid
                        value=str(end-start)
                        break
                    #print(count)
                if value2==value:
                    value=''
            list1.append(count)
            i+=1
            
        final=int(''.join(list(map(str,list1))))
        
        if (valx>0 and valy>0) or (valx<0 and valy<0):
            return final
        else:
            return -final
