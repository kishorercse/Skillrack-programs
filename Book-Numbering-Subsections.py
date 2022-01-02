"""
There are N chapters in a book. Each chapter has a certain number of sections and each section has a certain number of subsections. The number of chapters and the number of 
sections in each chapter and the number of subsections in each section are passed as the input. The program must print the number given to each subsection in the book as shown
in the Example Input/Output section.

Boundary Condition(s):
1 <= N <= 15
1 <= Number of sections in each chapter <= 10
1 <= Number of subsections in each section <= 10

Input Format:
The first line contains N.
The lines contain the number of sections and subsections in the book.

Output Format:
The lines contain the number given to each subsection in the book.

Example Input/Output 1:
Input:
4
-2
--5
--3
-3
--4
--1
--2
-2
--6
--3
-1
--4

Output:
1.1.1
1.1.2
1.1.3
1.1.4
1.1.5
1.2.1
1.2.2
1.2.3
2.1.1
2.1.2
2.1.3
2.1.4
2.2.1
2.3.1
2.3.2
3.1.1
3.1.2
3.1.3
3.1.4
3.1.5
3.1.6
3.2.1
3.2.2
3.2.3
4.1.1
4.1.2
4.1.3
4.1.4

Explanation:
There are 4 chapters in the books.
1st chapter: 2 sections (5 subsections and 3 subsections)
2nd chapter: 3 sections (4 subsections, 1 subsection and 2 subsections)
3rd chapter: 2 sections (6 subsections and 3 subsections)
4th chapter: 1 section (4 subsections)

Example Input/Output 2:
Input:
3
-1
--2
-3
--3
--1
--1
-2
--2
--2

Output:
1.1.1
1.1.2
2.1.1
2.1.2
2.1.3
2.2.1
2.3.1
3.1.1
3.1.2
3.2.1
3.2.2
"""
n=int(input())
for ch in range(1,n+1):
    t=int(input()[1:])
    for sec in range(1,t+1):
        x=int(input()[2:])
        for sub in range(1,x+1):
            print(ch,sec,sub,sep='.')
