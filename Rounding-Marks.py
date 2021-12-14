"""
In a college, each student receives marks M in any of the subjects in the range from 0 to 100.  
- If the difference between the marks and the next multiple of 5 is less than 3, then round the marks up to the next multiple of 5.
- If the difference between the marks and the next multiple of 5 is more than or equal to 3, then leave the marks as it is.
- If the marks obtained is less than or equal to 37, then leave the marks as it is.

Input Format:
The first line will contain the value of N which represents the count of the test cases.
Next N lines will contain the marks from M(1) to M(N)

Output Format:
N lines containing the rounded marks value, one line each for the marks from M(1) to M(N)

Constraints:
2 <= N <= 100

Example Input/Output 1:
Input:
4
83
57
48
33

Output:
85
57
50
33
"""
n=int(input())
while n > 0:
    m=int(input())
    if m>37:
        diff=5-m%5
        if diff<3:
            m+=diff
    print(m)
    n-=1
