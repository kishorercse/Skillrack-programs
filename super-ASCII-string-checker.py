"""
The program must accept N string values as the input. For each string S among the N string values, the program must print Yes if it is a super ASCII string. Else the program must print No as the output. A string is said to be a super ASCII string if and only if the count of each character in the string is equal to its super ASCII value. The super ASCII value of ‘a‘ is 1, ‘b‘ is 2, ‘c‘ is 3,… ‘z‘ is 26.
Note: Each string contains only lower case alphabets.

Boundary Condition(s):
1 <= N <= 100
1 <= Length of each string <= 400

Input Format:
The first line contains N.
The next N lines, each containing a string.

Output Format:
The first N lines, each containing Yes or No.

Example Input/Output 1:
Input:
2
abcbcc
dcddd

Output:
Yes
No

Explanation:
In the first string “abcbcc“,
The count of the alphabet ‘a’ is 1. The super ASCII value of ‘a’ is also 1.
The count of the alphabet ‘b’ is 2. The super ASCII value of ‘b’ is also 2.\
The count of the alphabet ‘c’ is 3. The super ASCII value of ‘c’ is also 3.
Here the string “abcbcc” is a super ASCII string. So Yes is printed.
In the second string “dcddd“,
The count of the alphabet ‘d’ is 4. The super ASCII value of ‘d’ is also 4.
The count of the alphabet ‘c’ is 1. The super ASCII value of ‘c’ is 3.
Here the string “dcddd” is NOT a super ASCII string. So No is printed.

Example Input/Output 2:
Input:
3
bdcdcd
fafffff
zzzzzzzzzzzzzzzzzzzzzzzzzz

Output:
No
Yes
Yes
"""
n=int(input())
for i in range(n):
    s=input().strip()
    d={}
    for i in s:
        d[i]=d.get(i,0)+1
    for i in s:
        if ord(i)-96!=d[i]:
            print("No")
            break
    else:
        print("Yes")
