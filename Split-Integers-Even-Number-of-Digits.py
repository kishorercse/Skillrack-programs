"""
The program must accept an integer N as the input. The program must split the integer into two equal halves if the number of digits in the integer is even. Then the
program must repeat the process on the resulting integers till there is no integer with an even number of digits. The leading zeroes must not be considered after each
split operation. Finally, the program must print the resulting integers in sorted order.

Boundary Condition(s):
1 <= N <= 10^18

Input Format:
The first line contains N.

Output Format:
The first line contains the integer values based on the given conditions.

Example Input/Output 1:
Input:
1024

Output:
0 1 2 4

Explanation:
N = 1024.
1st split: 10, 24
2nd split: 1, 0, 2, 4
So the resulting four integers are printed in sorted order.

Example Input/Output 2:
Input:
50000006

Output:
0 0 5 6

Explanation:
N = 50000006.
1st split: 5000, 6
2nd split: 50, 0, 6
3rd split: 5, 0, 0, 6
So the resulting four integers are printed in sorted order.

Example Input/Output 3:
Input:
923456

Output:
456 923
"""
l=[int(input())]
flag=True
while flag:
    flag=False
    t=[]
    for i in l:
        s=str(i)
        a=len(s)
        if a%2==0:
            a//=2
            t.append(int(s[:a]))
            t.append(int(s[a:]))
            flag=True
        else:
            t.append(i)
    l=t[:]
print(*sorted(l))
