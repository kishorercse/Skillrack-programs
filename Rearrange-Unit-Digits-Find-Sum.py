"""
The program must accept N integers as the input, but the first digit of each integer denotes the unit digit of the previous integer. Consider the previous integer of the 1st 
integer as the Nth integer. The program must rearrange the unit digits to the respective integers, and then print their sum as the output.

Boundary Condition(s):
2 <= N <= 100
10 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains an integer representing the sum of the N revised integers.

Example Input/Output 1:
Input:
4
614 5273 41 278

Output:
3677

Explanation:
Here N = 4.
After rearranging the unit digits to the respective integers, the integers become
614 5273 41 278 -> 145 2734 12 786
145 + 2734 + 12 + 786 = 3677.

Example Input/Output 2:
Input:
3
010 020 5500

Output:
5305

Explanation:
Here N = 3.
After rearranging the unit digits to the respective integers, the integers become
010 020 5500 -> 100 205 5000
100 + 205 + 5000 = 5305.
"""
n=int(input())
l=input().split()
res=0
for i in range(n-1):
    res+=int(l[i][1:]+l[i+1][0])
res+=int(l[n-1][1:]+l[0][0])
print(res)
