"""
The program must accept 3 integer values, A, B and C. Then the program must print Yes 
if when B and C merged together (in any order) is equal to the square of A. 
Else the program must print No. 

Boundary Condition(s): 
1 <= A, B, C <= 10^4 

Input Format: 
The first line contains A, B and C separated by a space. 

Output Format: 
The first line contains Yes or No. 

Example Input/Output 1:
Input: 
15 2 25 

Output:
Yes 

Explanation: 
2 and 25 when merged forms 225 which is a square of 15. 

Example Input/Output 2: 
Input: 
15 25 2 

Output: 
Yes 

Explanation: 
25 and 2 when merged forms 252. But 252 is not a square of 15. 
So we merge in the reverse order. 
2 and 25 merged gives 225 which is a square of 15. 
So Yes is printed. 

Example Input/Output 3: 
Input: 
54 30 16 

Output:
No
"""
a,b,c=input().split()
a=int(a)**2
x=int(b+c)
y=int(c+b)
if a==x or a==y:
    print("Yes")
else:
    print("No")
