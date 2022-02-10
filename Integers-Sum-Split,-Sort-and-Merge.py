"""
The program must accept N integers as the input, where each integer contains a pipe symbol. The program must find the sum of the given N integers as S1. Then the program must
split each integer in two parts based on the pipe symbol. Then the program must sort the resulting N*2 integers and concatenate every two integers. Then the program must find
the sum of N resulting integers as S2. Finally, the program must print the values of S1 and S2 as the output.

Boundary Condition(s):
1 <= N <= 100
10 <= Each integer value <= 10^6

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the values of S1 and S2 separated by a space.

Example Input/Output 1:
Input:
4
12|3 98|54 23|02 8|76

Output:
13155 10887

Explanation:
Here N = 4.
S1 = 123 + 9854 + 2302 + 876 = 13155.

After dividing each integer two parts, the integers become
12 3 98 54 23 2 8 76

After sorting the 8 integers, the integers become
2 3 8 12 23 54 76 98

After merging every two integers, the integers become
23 812 2354 7698

S2 = 23 + 812 + 2354 + 7698 = 10887.

Example Input/Output 2:
Input:
6
3|38 57|00 1|1 5|36 389|9 74|52

Output:
17936 83357
"""
n=int(input())
l=input().split()
l2=[]
s1=s2=0
for i in range(n):
    a=int(''.join(l[i].split('|')))
    s1+=a
    a,b=l[i].split('|')
    l2.append(int(a))
    l2.append(int(b))
l2.sort()
for i in range(0,2*n,2):
    s2+=int(str(l2[i])+str(l2[i+1]))
print(s1,s2)
