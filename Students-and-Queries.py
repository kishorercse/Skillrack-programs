"""
There are N students in a class. The program must accept the roll number and the marks in three subjects(A, B, C) of each student as the input. The program also
accepts Q queries as the input. Each query contains two lines, where the first line contains a character CH and the second line contains a string S representing
a condition. The value of CH can be any one of the following.
* - It indicates all four fields (Roll Number, A, B and C).
A - It indicates the field A (the marks in the subject A).
B - It indicates the field B (the marks in the subject B).
C - It indicates the field C (the marks in the subject C).
The string S contains the subject name (A, B or C), an operator (>, < or =) and an integer value. For each query, the program must print the details of the students
based on the character CH and the condition S. If there are no students for the given query, then the program must print -1 as the output.
Note: For each query, the details of the students must be printed in the order of their occurrence.

Boundary Condition(s):
1 <= N, Q <= 100
1 <= Roll Number, Marks in each subject (A, B, C) <= 100

Input Format:
The first line contains N.
The next N lines, each contains the roll number and the marks in three subjects(A, B, C) of each student.
The N+2nd line contains Q.
The next Q pairs of lines, each contains the character CH in the first line and the string S in the second line.

Output Format:
The lines contain the details of the students based on the character CH and the condition S or -1.

Example Input/Output 1:
Input:
4
1 50 60 80
2 99 64 90
3 70 90 80
4 60 70 95
3
*
A>50
A
B<70
*
B=95

Output:
2 99 64 90
3 70 90 80
4 60 70 95
50
99
-1

Explanation:
1st query: CH = * and the condition is A>50.
All four fields of the students who scored more than 50 marks in the subject A are printed.
2 99 64 90
3 70 90 80
4 60 70 95

2nd query: CH = A and the condition is B<70.
The marks in the subject A of the students who scored less than 70 marks in the subject B are printed.
50
99

3rd query: CH = B and the condition is B=95.
There are no students having 95 marks in the subject B.
So -1 is printed.

Example Input/Output 2:
Input:
6
7 81 22 32
5 79 35 40
3 32 95 27
4 58 40 52
8 35 68 84
2 22 36 39
7
C
B>90
A
A<35
*
B>25
C
C<50
B
A=50
B
C>40
A
C=40

Output:
27
32
22
5 79 35 40
3 32 95 27
4 58 40 52
8 35 68 84
2 22 36 39
32
40
27
39
-1
40
68
79
"""
n=int(input())
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
q=int(input())
for _ in range(q):
    ch=input().strip()
    s=input().strip()
    sub=sym=num=''
    for i in s:
        if i.isalpha():
            sub+=i
        elif i.isnumeric():
            num+=i
        else:
            sym+=i
    if sym=='=':
        sym+='='
    if sub=='A':
        x=1
    elif sub=='B':
        x=2
    elif sub=='C':
        x=3
    if ch=='*':
        a,b=0,4
    elif ch=='A':
        a,b=1,2
    elif ch=='B':
        a,b=2,3
    else:
        a,b=3,4
    flag=False
    for i in range(n):
        if eval(str(l[i][x])+sym+str(num)):
            print(*l[i][a:b])
            flag=True
    if flag==False:
        print(-1)
