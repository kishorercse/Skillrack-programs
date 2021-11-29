"""
The program must accept a string S containing only alphabets and two integers N, K as the input. The program must toggle the case of alphabets starting from the first sliding 
window of size N based on the following conditions.
- If the number of vowels in a sliding window is greater than or equal to K, then the program must toggle the case of alphabets in the window and move to the next 
non-overlapping window. Else the program must move to the next sliding window to check vowels.
- The program must repeat the above process till it reaches the last sliding window or there is no next non-overlapping window.
Finally, the program must print the revised string S as the output.

Boundary Condition(s):
1 <= Length of S <= 100
1 <= K <= N <= Length of S

Input Format:
The first line contains S.
The second line contains N and K separated by a space.

Output Format:
The first line contains the revised string S.

Example Input/Output 1:
Input:
Organization
5 2

Output:
oRGANIZATIon

Explanation:
Here N = 5 and K = 2.
1st sliding window is Organ.
There are 2 vowels in the window. So the case of the alphabets in the window has toggled.
Organ -> oRGAN

The next non-overlapping sliding window is izati.
There are 3 vowels in the window. So the case of the alphabets in the window has toggled.
izati -> IZATI

There is no next non-overlapping window. Hence the output is oRGANIZATIon.

Example Input/Output 2:
Input:
ORGANIZATION
3 2

Output:
ORGaniZatiON

Example Input/Output 3:
Input:
SkillRackOctal
4 2

Output:
SkillRACKoctal
"""
def vowelCount(s):
    c=0
    for i in s:
        if i in "AEIOUaeiou":
            c+=1
    return c
s=input().strip()
n,k=map(int,input().split())
l=len(s)
i=0
while i<l:
    if l-i>=n and vowelCount(s[i:i+n])>=k:
        print(s[i:i+n].swapcase(),end='')
        i+=n
    else:
        print(s[i],end='')
        i+=1
