"""
The program must accept an array of N integers as the input with some integers missing. The missing integers are denoted by the asterisks. The program must replace the asterisks
with positive integer values so that the array becomes palindrome with a minimum sum. Then the program must print the palindromic array as the output. If it is not possible to 
make the array palindrome, then the program must print -1 as the output.
Note: There will be at least one asterisk in the given array.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains integers and asterisks separated by a space.

Output Format:
The first line contains the palindromic array or -1 based on the given conditions.

Example Input/Output 1:
Input:
6
10 * 30 30 20 *

Output:
10 20 30 30 20 10

Explanation:
Here N = 6.
To make the array palindrome with the minimum sum, the first asterisk must be replaced with 20 and the second asterisk must be replaced with 10.
Hence the output is
10 20 30 30 20 10

Example Input/Output 2:
Input:
5
* 3 * 3 *

Output:
1 3 1 3 1

Example Input/Output 3:
Input:
7
30 * 10 10 15 * 30

Output:
-1
"""
n=int(input())
l=input().split()
i,j=0,n-1
while i<=j:
    if l[i]=='*' and l[j]=='*':
        l[i]=l[j]=1
    elif l[i]=='*':
        l[i]=l[j]
    elif l[j]=='*':
        l[j]=l[i]
    else:
        if l[i]!=l[j]:
            print(-1)
            break
    i+=1
    j-=1
else:
    print(*l)
