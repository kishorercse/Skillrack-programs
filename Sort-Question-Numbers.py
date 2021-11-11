"""
There are Q questions in a book. Each question has a number in the format X.Y.Z, where X represents the chapter number, Y represents the section number and Z represents the 
subsection number. Q question numbers are passed as the input. The program must sort the question numbers based on the chapter number, section number and subsection number 
in ascending order. Finally, the program must print the sorted question numbers as the output.

Boundary Condition(s): 
2 <= N <= 100 
1 <= X, Y, Z <= 20 

Input Format:
The first line contains N.
The next N lines, each contains a question number(in the format X.Y.Z). 

Output Format: 
The first N lines contain the sorted question numbers(in the format X.Y.Z). 

Example Input/Output 1: 
Input:
7
4.2.3
2.5.1
1.4.6
2.5.7
4.2.1
1.4.2
2.1.3

Output: 
1.4.2 
1.4.6 
2.1.3 
2.5.1 
2.5.7 
4.2.1 
4.2.3 

Explanation:
Here N=7. 
After sorting the given 7 question numbers in ascending order, the question numbers become 
1.4.2 
1.4.6 
2.1.3 
2.5.1 
2.5.7 
4.2.1 
4.2.3 

Example Input/Output 2:
Input:
12
14.6.2
14.3.2
10.5.3
10.5.2
10.5.1
13.5.1
12.5.1
11.5.1
10.6.6
10.6.5
10.6.4
14.5.2

Output:
10.5.1
10.5.2
10.5.3
10.6.4
10.6.5
10.6.6
11.5.1
12.5.1
13.5.1
14.3.2
14.5.2
14.6.2
"""
n=int(input())
l=sorted([list(map(int,input().split('.'))) for _ in range(n)])
for i in l:
    print(*i,sep='.')
