"""
A farmer wishes to track during each harvest if he has broken previous best or worst records. The yield (in certain units) is passed as input to the program and the program 
must print how many times he broke his best record along with the number of times he broke his worst record.

Input Format:
The first line will contain the value of N which represents the units harvested in a specific yield.
The second line will contain the units harvested in N yields separated by a space.

Output Format:
The first line will contain the number of times he broke his best record followed by the number of times he broke his worst record, each separated by a space.

Constraints:
3 <= N <= 100

Example Input/Output 1:
Input:
10
3 4 21 36 10 28 30 5 24 42

Output:
4 0

Explanation:
The best yield breaking records are for 4, 21, 36, 42. Hence 4 is printed.
The worst yield breaking record is 0 as none of the yields was less than 3 (which happens to be the first yield).


Example Input/Output 1:
Input:
9
10 5 20 20 4 5 2 25 1

Output:
2 4

Explanation:
The best yield breaking records are for 20, 25. Hence 2 is printed.
The worst yield breaking records are for 5, 4, 2, 1. Hence 4 is printed.
"""
n=int(input())
l=list(map(int,input().split()))
mx=-1
mn=999999
best=worst=0
for i in l:
    if i>mx:
        mx=i
        best+=1
    if i<mn:
        mn=i
        worst+=1
print(best-1,worst-1)
