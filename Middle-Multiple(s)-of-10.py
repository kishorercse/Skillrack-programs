"""
The program must accept two integers M and N as the input. The program must print the middle multiple of 10 among the multiples of 10 from M to N. If the number of multiples of 
10 is even, the program must print the middle two multiples of 10 as the output. If there is no multiple of 10 from X to Y, the program must print -1 as the output. 

Boundary Condition(s): 
1 <= M < N <= 10^5 

Input Format: 
The first line contains M and N separated by a space.

Output Format: 
The first line contains the integer value(s) as per the given conditions.

Example Input/Output 1:
Input:
45 96

Output:
70

Explanation: 
The multiples of 10 from 45 to 96 are 50, 60, 70, 80 and 90. 
Here the middle multiple of 10 is 70.
Hence the output is 70 

Example Input/Output 2: 
Input: 
110 140 

Output: 
120 130 Explanation: The multiples of 10 from 110 to 140 are 110, 120, 130 and 140. Here number of multiples of 10 is even. So the middle two multiples of 10 are 120 and 130. Hence the output is 120 130 Example Input/Output 3: Input: 1022 1029 Output: -1
"""
m,n=map(int,input().split())
if m%10!=0:
    m+=10-m%10
n-=n%10
d=(n-m)//10+1
if d==0:
    print(-1)
else:
    if d%2==0:
        d//=2
        print(m+10*(d-1),m+10*d)
    else:
        print(m+10*(d//2))
