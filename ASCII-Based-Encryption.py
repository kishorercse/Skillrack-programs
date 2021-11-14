"""
The program must accept a string S as the input. The program must encrypt the string S based on the following encryption technique. 
- Replace each vowel in S by the unit digit of its ASCII value. 
- Replace each consonant in S by the tenth digit of its ASCII value. 
- Replace each non-alphabet in S by the sum of digits in its ASCII value. 
Then the program must print the encrypted string as the output. 

Boundary Condition(s):
1 <= Length of S <= 100 

Input Format:
The first line contains S. 

Output Format: 
The first line contains the encrypted string. 

Example Input/Output 1:
Input:
India#2020 

Output: 
310578512512 

Explanation: 
I is a vowel. So the unit digit of its ASCII (73) is printed as the output.
n is a consonant. So the tenth digit of its ASCII (110) is printed as the output.
d is a consonant. So the tenth digit of its ASCII (100) is printed as the output.
i is a vowel. So the unit digit of its ASCII (105) is printed as the output. 
a is a vowel. So the unit digit of its ASCII (97) is printed as the output. 
# is a non-alphabet. So the sum of digits in its ASCII (35) is printed as the output. 
2 is a non-alphabet. So the sum of digits in its ASCII (50) is printed as the output. 
0 is a non-alphabet. So the sum of digits in its ASCII (48) is printed as the output. 
2 is a non-alphabet. So the sum of digits in its ASCII (50) is printed as the output. 
0 is a non-alphabet. So the sum of digits in its ASCII (48) is printed as the output. 

Example Input/Output 2:
Input:
SkillRack@123

Output: 
805008790101356
"""
def sumOfDig(n):
    t=0
    while n>0:
        t+=n%10
        n//=10
    return t
s=input().strip()
for i in s:
    if i in "AEIOUaeiou":
        print(ord(i)%10,end='')
    elif i.isalpha():
        print(ord(i)//10%10,end='')
    else:
        print(sumOfDig(ord(i)),end='')
