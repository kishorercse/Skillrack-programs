"""
The program must accept two string values S1 and S2. If S2 is a stretched string of S1, the program must
print Yes. Else the program must print No. A stretch is to repeat each character in string the same number
of times. Also no additional characters must be present in S2.

Boundary Condition(s):
1 <= Length of S1, S2 <= 1000

Input Format:
The first line contains S1.
The second line contains S2.

Output Format:
The first line contains Yes or No

Example Input/Output 1:
Input:
cake 
cccaaakkkeee 

Output: 
Yes 

Explanation:
Here each character in S2 is repeated 3 times and no additional characters.
Hence S2 is a stretched version of S1. 

Example Input/Output 2: 
Input:
cake
ccaaaakkkeee 

Output:
No

Example Input/Output 3:
Input:
cake
ccaakkeess

Output: 
No

Explanation:
Here s is an additional character. 
Hence S2 is not a stretched version of S1. 

Example Input/Output 4: 
Input:
eel 
eeeeeelll 

Output:
Yes
"""
a=input().strip()
b=input().strip()
x=len(a)
y=len(b)
if y%x!=0:
    print("No")
else:
    t=y//x
    s=''
    for i in a:
        s+=i*t
    if s==b:
        print("Yes")
    else:
        print("No")
