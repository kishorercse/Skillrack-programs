"""
The program must accept two string values F1 and F2 representing the names of two text files as the input. The file F1 contains the id and name of N employees and 
the file F2 contains the id and designation of the N employees. The program must print the id, name and designation of the N employees from the given two files as
the output. The ids of the employees must be printed in sorted order.

Note:
- Both files are always in the same folder where the program executes.
- Both the files have the same number of lines/records.

Boundary Condition(s):
5 <= F1, F2 <= 30
1 <= N <= 50
1 <= Each employee's id <= 100
1 <= Length of each employee's name and designation <= 30

Input Format:
The first line contains F1.
The second line contains F2.

Output Format:
The first N lines contain the id, name and designation of the N employees separated by a space.

Example Input/Output 1:
Input:
empNames.txt
empDesignation.txt

Output:
10 Catherine Trainee
20 Anitha HR
30 Pravin SDE
40 Hector Manager

Explanation:
Here empNames.txt is present in the same folder where the program executes and the file contains the following 5 lines.
4
10 Catherine
20 Anitha
40 Hector
30 Pravin

Here empDesignation.txt is present in the same folder where the program executes and the file contains the following 5 lines.
4
40 Manager
30 SDE
10 Trainee
20 HR

Example Input/Output 2:
Input:
names.txt
designation.txt

Output:
9 John Trainee
12 Jhanvi Trainee
17 Bhuvana Manager
25 Pravin SDE
34 Mambo HR

Explanation:
Here names.txt is present in the same folder where the program executes and the file contains the following 6 lines.
5
12 Jhanvi
25 Pravin
34 Mambo
9 John
17 Bhuvana

Here designation.txt is present in the same folder where the program executes and the file contains the following 6 lines.
5
34 HR
17 Manager
9 Trainee
25 SDE
12 Trainee
"""
f1=input().strip()
f2=input().strip()
l=[]
with open(f1) as file:
    n=int(file.readline())
    for _ in range(n):
        i,s=file.readline().split()
        l.append([int(i),s])
with open(f2) as file:
    n=int(file.readline())
    for _ in range(n):
        i,d=file.readline().split()
        i=int(i)
        for e in l:
            if e[0]==i:
                e.append(d)
l.sort(key=lambda x:x[0])
for i in l:
    print(*i)
