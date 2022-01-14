"""
There are N chocolates in a row. The weight of each chocolate is passed as the input. A boy can eat chocolates based on the following conditions.
- The boy wants to eat as many chocolates as possible in a day.
- The boy can eat a chocolate if the weight of the chocolate is greater than the weight of the chocolate on its left.
The program must print the number of days he can eat the chocolates as the output.

Boundary Condition(s):
2 <= N <= 1000
1 <= Weight of each chocolate <= 10^5

Input Format:
The first line contains N.
The second line contains N integers separated by a space representing the weights of the N chocolates.

Output Format:
The first line contains an integer representing the number of days the boy can eat the chocolates.

Example Input/Output 1:
Input:
5
30 60 20 70 50

Output:
2

Explanation:
There are 5 chocolates in the row [30 60 20 70 50]

1st day: He can eat the 2nd and 4th chocolates.
Now there are 3 chocolates left [30 20 50].

2nd day: He can eat the 3rd chocolate.
Now there are 2 chocolates left [30 20].

3rd day: He cannot eat any chocolate.

Hence 2 is printed as the output.

Example Input/Output 2:
Input:
15
14 18 10 24 17 16 22 21 19 12 23 25 20 11 15

Output:
5

Explanation:
There are 15 chocolates in the row [14 18 10 24 17 16 22 21 19 12 23 25 20 11 15]
After the 1st day: [14 10 17 16 21 19 12 20 11]
After the 2nd day: [14 10 16 19 12 11]
After the 3rd day: [14 10 12 11]
After the 4th day: [14 10 11]
After the 5th day: [14 10]
6th day: He cannot eat any chocolate.
"""
n=int(input())
l=list(map(int,input().split()))
ch=0
d=-1
a=[]
f=True
while f:
    f=False
    a=[l[0]]
    for i in range(1,n-ch):
        if l[i]>l[i-1]:
            f=True
            ch+=1
        else:
            a.append(l[i])
    d+=1
    l=a[:]
print(d)
