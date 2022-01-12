"""
The program must accept an integer N as the input. The program must print a triangle of size N based on the following conditions.
- The edge between the top corner(inclusive) and the right corner of the triangle must be formed using the alphabet 'a'.
- The edge between the right corner(inclusive) and the left corner of the triangle must be formed using the alphabet 'b'.
- The edge between the left corner(inclusive) and the top corner of the triangle must be formed using the alphabet 'c'.
- The empty spaces in the triangle must be filled with asterisks.
Finally, the program must print the triangle pattern as shown in the Example Input/Output section.

Boundary Condition(s):
3 <= N <= 50

Input Format:
The first line contains N.

Output Format:
The first N lines contain the triangle pattern based on the given conditions.

Example Input/Output 1:
Input:
5

Output:
****a
***c*a
**c***a
*c*****a
c b b b b

Explanation:
Here N = 5, so the size of the triangle is 5.
Hence the output is
****a
***c*a
**c***a
*c*****a
c b b b b

Example Input/Output 2:
Input:
4

Output:
***a
**c*a
*c***a
c b b b

Example Input/Output 3:
Input:
6

Output:
*****a
****c*a
***c***a
**c*****a
*c*******a
c b b b b b
"""
n=int(input())
print('*'*(n-1),'a',sep='')
center=1
for i in range(2,n):
    print('*'*(n-i),'c','*'*center,'a',sep='')
    center+=2
print('c','b '*(n-1))
