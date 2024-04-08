'''
Palindromic Series (GFG)

Adobe wants to play a game. He is given a number N. He has to create a alphabetical string in lower case from that number and tell whether the string is palindrome or not. a = 0 , b = 1….. and so on.  For eg : If the number is 61 the substring “gb” will be printed till 7 (6+1) characters i.e. “gbgbgbg” and check if palindrome or not. Adobe is weak in concepts of palindrome and strings, help him in winning the game.
Note: No number will start with zero. Consider alphabets ' a to j ' only i.e. single digit numbers from 0 to 9.

Example 1:

â€‹Input : N = 61
Output : YES
Explanation:
N = 61 the substring “gb” will be 
printed till 7 (6+1) characters i.e. 
“gbgbgbg” and it is palindrome. return 
true.
'''
def pallan (n) : 
    dict1=dict(zip([i for i in range(26)],'abcdefghijklmnopqrstuvwxyz'))
    
    num_list=list(map(int,list(str(n))))
    
    length1=sum(num_list)
    length2=len(num_list)
    
    string=''.join(list(map(lambda x:dict1[x],num_list)))
    
    times=length1//length2
    rem=length1%length2
    
    string=string*times+string[0:rem]
    
    if string==string[::-1]:
        return True
        
    return False
