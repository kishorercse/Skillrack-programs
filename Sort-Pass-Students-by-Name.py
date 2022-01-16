"""
A list of N students name and their marks in three subjects are passed as the input. The average of the 3 subjects must be greater than or equal to 40 and also the total marks 
must be greater than or equal to 150 for the student to pass. Print the names of the students who have passed, with the names sorted in ascending order.

Input Format:
The first line contains N, the number of students.
The following N lines contains Name and marks of each student in three subjects separated by space.

Output Format:
Print the names of the students who passed (with the names sorted in ascending order).

Example Input/Output 1:
Input:
3
Ram 45 65 45
Geetha 60 30 50
Soundarya 80 90 80

Output:
Ram
Soundarya
"""
n=int(input())
m=[]
for _ in range(n):
    t=input().split()
    t[1:]=map(int,t[1:])
    s=sum(t[1:])
    a=s//3
    if a>=40 and s>=150:
        m.append(t)
m.sort(key=lambda x:x[0])
for i in m:
    print(i[0])
