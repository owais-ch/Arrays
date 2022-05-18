'''
B. Triple
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Given an array a of n elements, print any value that appears at least three times or print -1 if there is no such value.

Input
The first line contains an integer t (1≤t≤104) — the number of test cases.

The first line of each test case contains an integer n (1≤n≤2⋅105) — the length of the array.

The second line of each test case contains n integers a1,a2,…,an (1≤ai≤n) — the elements of the array.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅105.

Output
For each test case, print any value that appears at least three times or print -1 if there is no such value.'''

num_test=int(input())
 
for i in range(num_test):
    length=int(input())
    arr=list(map(int,input().split(' ')))
 
    arr.sort()
    count=1
    countz=0
    
    for i in range(length-1):
        if arr[i]==arr[i+1]:
            count+=1
            if count>=3:
                print(arr[i])
                countz=1
                break
        else:   
            count=1
    if countz==0:
        print(-1)
