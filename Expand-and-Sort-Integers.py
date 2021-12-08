"""
The program must accept N integers as the input. The program must expand each integer to a maximum value by repeating any one of the digits D in the integer D times. Finally, 
the program must sort those revised integers and print them as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value < 10^8

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains N Integers separated by a space representing the sorted integers.

Example Input/Output 1:
Input:
4
512 123 782 90

Output:
12333 5555512 7888888882 9999999990

Explanation:
512 -> 5555512 or 512 or 5122 -> 5555512 is the maximum value.
123 -> 123 or 1223 or 12333 -> 12333 is the maximum value.
782 -> 777777782 or 7888888882 or 7822 -> 7888888882 is the maximum value.
90 -> 9999999990 or 9 -> 9999999990 is the maximum value.
So the expanded values are sorted and printed as the output.

Example Input/Output 2:
Input:
5
404 34 525 48185 51

Output:
34444 444404 555551 5555525 488888888185
"""
n=int(input())
l=input().split()
for i in range(n):
    mx=mxi=-1
    for j in range(len(l[i])):
        if int(l[i][j])>mx:
            mx=int(l[i][j])
            mxi=j
    l[i]=int(l[i][:mxi]+str(mx)*mx+l[i][mxi+1:])
print(*sorted(l))
