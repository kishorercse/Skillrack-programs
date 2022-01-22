"""
The program must accept an array of N integers of an equal number of digits, but some digits at the end of an integer are missing and those missing digits are appended to some 
other integer in the array. The program must find those two integers and make the integers with an equal number of digits. Then the program must print the N integers and their 
sum as the output.

Boundary Condition(s):
2 <= N <= 1000
1 <= Each integer value <= 10^8

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the N revised integers separated by a space.
The second line contains the sum of the N revised integers.

Example Input/Output 1:
Input:
5
645 12 814 2476 459

Output:
645 126 814 247 459
2291

Explanation:
Here N = 5.
2nd integer: 12 -> One digit is missing.
4th integer: 2476 -> One digit is appended.
So 12 becomes 126 and 2476 becomes 247.
645 + 126 + 814 + 247 + 459 = 2291.

Example Input/Output 2:
Input:
8
7424 1865074 8322 1181 3 7674 1718 4157

Output:
7424 1865 8322 1181 3074 7674 1718 4157
35415
"""
n=int(input())
l=input().split()
length=0
for i in l:
    length+=len(i)
each=length//n
less=more=-1
for i in range(n):
    if len(l[i])>each:
        more=i
        if less!=-1:
            break
    elif len(l[i])<each:
        less=i
        if more!=-1:
            break
diff=len(l[more])-each
l[less]+=l[more][-diff:]
l[more]=l[more][:-diff]
print(*l)
print(sum(map(int,l)))
