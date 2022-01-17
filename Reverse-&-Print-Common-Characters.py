"""
Two string values S1 and S2 are passed as the input. Reverse string S2 and print the letters which are same in a given index. The letters in S1 and S2 will be in lower case.

Input Format:
The first line contains S1.
The second line contains S2.

Output Format:
The first line contains the letters which are common after S2 is reversed.

Boundary Conditions:
2 <= Length of S1, S2 <= 500

Example Input/Output 1:
Input:
energy
genuine

Output:
en

Explanation:
After reversing S2, we get
energy
eniuneg
The letters common comparing indices are en (in the first two positions)
"""
a=input().strip()
b=input().strip()
i,j=0,len(b)-1
l=len(a)
while j>=0 and i<l:
    if a[i]==b[j]:
        print(a[i],end='')
    i+=1
    j-=1
