"""
The program must accept a string S as the input. The string S contains only asterisks(*), hash symbols(#), hyphens(-) and the alphabet(L).
- Each asterisk represents a charging point for laptops.
- Each hash symbol represents a wall.
- Each hyphen represents an empty space.
- Each alphabet L represents a laptop.
For each laptop, the program must print the distance between the laptop and the nearest charging point. If there is no charging point for a laptop, then the program must print
-1 for that laptop. If there is a wall between the laptop and the charging point, the laptop cannot be connected to that charging point.

Note: There will be at least one occurrence of L in the string S.

Boundary Condition(s):
1 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The first line contains the integer values representing the distance between the laptop and the nearest charging point.

Example Input/Output 1:
Input:
*-*---L--*---*-L

Output:
3 2

Explanation:
For the 1st laptop, the nearest charging point is present on the right side.
The distance between the 1st laptop and the nearest charging point is 3.

For the 2nd laptop, the nearest charging point is present on the left side.
The distance between the 2nd laptop and the nearest charging point is 2.

Hence the output is
3 2

Example Input/Output 2:
Input:
L----L*--*---#-*--L-#--*--#---L

Output:
6 1 3 -1
"""
s=input().strip()
l=len(s)
ch=-1
for i in range(l):
    if s[i]=='L':
        ind=i+1
        ans=9999
        if ch!=-1:
            ans=i-ch
        while ind<l:
            if s[ind]=='#':
                break
            elif s[ind]=='*':
                ans=min(ans,ind-i)
            ind+=1
        if ans==9999:
            print(-1,end=' ')
        else:
            print(ans,end=' ')
    elif s[i]=='*':
        ch=i
    elif s[i]=='#':
        ch=-1
