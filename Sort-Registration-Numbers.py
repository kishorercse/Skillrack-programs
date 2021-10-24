"""
The program must accept the registration numbers of N students as the input. The format of the registration number is YYDDNNN, where YY represents the last digits of the year of 
graduation, DD represents the shortcode of the department name and NNN represents the roll number. The program must sort the registration numbers based on the following conditions. 
- The year of graduation YY must be sorted in descending order. 
- The department short code DD in each graduation year must be in sorted order. 
- The roll numbers in each department must be sorted ascending order. 
Finally, the program must print the sorted registration numbers as the output. 

Boundary Condition(s):
2 <= N <= 50 

Input Format: 
The first line contains N. 
The next N lines, each contains the registration number of a student.

Output Format: 
The first N lines contain the sorted registration numbers of the N students. 

Example Input/Output 1:
Input: 
18 
20EC001
20EC002 
20EC003 
19IT001 
19IT002 
19IT003 
20CS002 
20CS003 
20CS001 
20IT002 
20IT001 
20IT003 
21CS001 
21CS003 
21CS002 
19EE004 
19EE005 
19EE006 

Output: 
21CS001 
21CS002 
21CS003 
20CS001 
20CS002 
20CS003 
20EC001 
20EC002 
20EC003 
20IT001 
20IT002 
20IT003 
19EE004 
19EE005 
19EE006 
19IT001 
19IT002 
19IT003 

Explanation: 
Here N=18. 
After sorting the given 18 registration numbers based on the year, department and roll number, the registration numbers become 
21CS001
21CS002
21CS003
20CS001
20CS002
20CS003
20EC001
20EC002
20EC003
20IT001
20IT002
20IT003
19EE004
19EE005
19EE006
19IT001
19IT002
19IT003

Example Input/Output 2:
Input:
8
20CS008 
20CS003 
19CS002 
19IT009 
19CS006 
20IT007 
19CS004 
19CS001 

Output: 
20CS003 
20CS008 
20IT007 
19CS001 
19CS002 
19CS004 
19CS006 
19IT009 
"""
n=int(input())
l=sorted([input().strip() for _ in range(n)],key=lambda x:(-int(x[:2]),x[2:4],int(x[4:])))
print(*l,sep='\n')
