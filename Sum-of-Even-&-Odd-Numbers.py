"""
N numbers will be passed as input to the program. The program must print the sum of even numbers followed by the sum of odd numbers.

Input Format:
First line contains total number of test cases, denoted by T
Next 2*T lines, contain the test case values for T test cases. Each test case will have
- N in the first line indicating the count of numbers
- N integer values separated by one or more space(s)


Output Format:
2T lines containing the output values for T test cases. Each test case output will have
- Sum of even numbers in the first line
- Sum of odd numbers in the second line


Boundary Conditions / Constraints:
1 <= T <= 25
1 <= N <= 100
0 <= Value of N Numbers <= 9999999

Example Input/Output 1:
Input:
3
4
2 5 4 11
5
2 4 6 8 10
4
101 22 66 17

Output:
6
16
30
0
88
118
"""
t=int(input())
while t>0:
    n=int(input())
    l=list(map(int,input().split()))
    even=odd=0
    for i in l:
        if i%2==0:
            even+=i
        else:
            odd+=i
    print(even,odd,sep='\n')
    t-=1
