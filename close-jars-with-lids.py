"""
The program must accept N integers as the input. Each odd integer represents a jar. Each even integer represents a lid.
A jar X can be closed with lid X+1. The program must print the number of jars that can be closed with lid as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^9

Input Format:
The first line contains N.
The second line contains N integer values separated by a space.

Output Format:
The first line contains an integer value representing the number of jars that can be closed with a lid.

Example Input/Output 1: 
Input: 
6
1 2 4 3 10 11 

Output: 2 

Explanation:
1, 3 and 11 represent the jars.
2, 4 and 10 represent the lids.
Jar 1 can be closed with lid 2.
Jar 3 can be closed with lid 4.

Example Input/Output 2:
Input:
4 
100 101 102 103 

Output:
1
"""
int(input())
l=list(map(int,input().split()))
d={}
count=0
for i in l:
    d[i]=d.get(i,0)+1
for i in d:
    if i%2!=0:
        try:
            while d[i+1]>0 and d[i]>0:
                d[i+1]-=1
                d[i]-=1
                count+=1
        except KeyError:
            pass
print(count)
