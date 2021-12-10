"""
The program must accept an array of N integers and an integer T as the input. The program must modify the array T times based on the following conditions.
- The program must reduce the value of an integer by 1 at a time (left to right circularly).
- If an integer value reaches 0, then the program must start increasing the value by 1 till the integer reaches its original value. Then the program must decrement the value
to 0, then increment the value to its original value, and so on.
- After each modification, the program must print the integers in the revised array.

Boundary Condition(s):
2 <= N <= 25
1 <= Each integer value <= 50
1 <= T <= 10^4

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains T.

Output Format:
The first T lines, each contains N integers separated by a space representing the revised array.

Example Input/Output 1:
Input:
4
4 2 5 1
25

Output:
3 2 5 1
3 1 5 1
3 1 4 1
3 1 4 0
2 1 4 0
2 0 4 0
2 0 3 0
2 0 3 1
1 0 3 1
1 1 3 1
1 1 2 1
1 1 2 0
0 1 2 0
0 2 2 0
0 2 1 0
0 2 1 1
1 2 1 1
1 1 1 1
1 1 0 1
1 1 0 0
2 1 0 0
2 0 0 0
2 0 1 0
2 0 1 1
3 0 1 1

Example Input/Output 2:
Input:
5
4 3 2 1 4
30

Output:
3 3 2 1 4
3 2 2 1 4
3 2 1 1 4
3 2 1 0 4
3 2 1 0 3
2 2 1 0 3
2 1 1 0 3
2 1 0 0 3
2 1 0 1 3
2 1 0 1 2
1 1 0 1 2
1 0 0 1 2
1 0 1 1 2
1 0 1 0 2
1 0 1 0 1
0 0 1 0 1
0 1 1 0 1
0 1 2 0 1
0 1 2 1 1
0 1 2 1 0
1 1 2 1 0
1 2 2 1 0
1 2 1 1 0
1 2 1 0 0
1 2 1 0 1
2 2 1 0 1
2 3 1 0 1
2 3 0 0 1
2 3 0 1 1
2 3 0 1 2
"""
n=int(input())
arr=list(map(int,input().split()))
t=int(input())
check=[-1]*n
revArr=arr[:]
ind=0
while t>0:
    revArr[ind]+=check[ind]
    if (revArr[ind]==0 or revArr[ind]==arr[ind]):
        check[ind]*=-1
    print(*revArr)
    ind=(ind+1)%n
    t-=1
