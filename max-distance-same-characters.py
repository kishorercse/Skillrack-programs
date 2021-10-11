"""
The program must accept a string S as the input. The program must print the character along with its maximum distance to reach the same character as the output. If two or more characters have the same maximum distance then the program must print the first occurring character and it’s distance as the output. If there are no such characters in the string S then the program must print -1 as the output.

Boundary Condition:
3 <= Length of the S <= 10000

Input Format:
The first line contains S.

Output Format:
The first line contains the character along with the maximum distance.

Example Input/Output 1:
Input:
hellomadam

Output:
m4

Explanation:
In the string hellomadam, from the character l, the distance to reach the same character l is one.
In the string hellomadam, from the character m, the distance to reach the same character m is four.
In the string hellomadam, from the character a, the distance to reach the same character a is two.
The character m has the maximum distance 4. 
Hence the output is m4

Example Input/Output 2:
Input:
shy

Output:
-1
"""
s=input().strip()
l=len(s)
d={}
ans=-1
max_len=0
for i in range(l):
    t=-1
    try:
        d[s[i]][1]=i
        t=i-d[s[i]][0]
    except IndexError:
        d[s[i]].append(i)
        t=i-d[s[i]][0]
    except KeyError:
        d[s[i]]=[i]
    if t>max_len:
        max_len=t
        ans=s[i]
if ans!=-1:
    print(ans,max_len,sep='')
else:
    print(-1)
