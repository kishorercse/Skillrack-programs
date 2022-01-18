"""
The program must accept two integer arrays A1 and A2 as the input. The program must print YES if both arrays have the same size and the same digits used to form integers. Else
the program must print NO as the output. Then the program must print the sum of integers in the arrays A1 and A2 as the output.

Note: The maximum size of both arrays A1 and A2 is 100.

Boundary Condition(s):
1 <= Each integer value <= 10^8

Input Format:
The first line contains integer values separated by a space representing the array A1.
The second line contains integer values separated by a space representing the array A2.

Output Format:
The first line contains YES or NO.
The second line contains the sum of integers in the arrays A1 and A2 separated by a space only if YES is printed.

Example Input/Output 1:
Input:
12 801 6 8100
88 61000 1 21

Output:
YES
8919 61110

Explanation:
Both arrays A1 and A2 have an equal size 4.
The same digits are used in both arrays.
So YES is printed as the output.
The sum of integers in A1 is 8919.
The sum of integers in A2 is 61110.

Example Input/Output 2:
Input:
16 98 12 98 456 21
12 456 9898 16 21

Output:
NO

Example Input/Output 3:
Input:
71 571
757 71

Output:
NO

Explanation:
Both arrays A1 and A2 have an equal size 2.
The 2 integers in A1 are formed using two 7s, two 1s and one 5.
The 2 integers in A2 are formed using three 7s, one 1 and one 5.
Hence NO is printed as the output.
"""
a=input().split()
b=input().split()
n1=len(a)
n2=len(b)
if n1==n2:
    countA=[0]*10
    x=0
    for i in a:
        x+=int(i)
        for j in i:
            t=int(j)
            countA[t]+=1
    countB=[0]*10
    y=0
    for i in b:
        y+=int(i)
        for j in i:
            t=int(j)
            countB[t]+=1
    if all(countA[i]==countB[i] for i in range(10)):
        print("YES")
        print(x,y)
    else:
        print("NO")
else:
    print("NO")
