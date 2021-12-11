"""
Anita works in Hentrum, a FOREX shop which converts US dollars to Indian Rupee. Anita wants to write a program that will convert the amount to be paid in Indian Rupee given 
the USD count C and the exchange rate R to BUY.
Please help her by completing the program.

Input Format:
First line contains total number of test cases, denoted by T
Next T lines will contain C and R for a test case separated by one or more space(s).

Output Format:
T lines containing the Indian Rupee amount to be paid rounded and padded up to 2 decimal places.

Boundary Conditions / Constraints:
1 <= T <= 25
1 <= C <= 100000
0.01 <= R <= 100.00

Example Input/Output 1:
Input:
4
10 62
562 66.54
100 67.105
1 69.148

Output:
620.00
37395.48
6710.50
69.15
"""
t=int(input())
while t>0:
    c,r=map(float,input().split())
    print("%.2f"%(c*r))
    t-=1
