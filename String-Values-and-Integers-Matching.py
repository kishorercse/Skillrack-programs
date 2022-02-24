"""
The program must accept N pairs where each pair contains a string value and an integer value. Each string on the left side matches an integer value on the right side. For each 
string on the left side, the program must print the position of the matching integer on the right side.

Note: All the integers on the right side are always unique.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The next N lines, each contains a string and an integer separated by a space.

Output Format:
The first line contains N integers separated by a space representing the matching positions.

Example Input/Output 1:
Input:
4
onezero 223
eight 10
twotwothree 59
fivenine 8

Output:
2 4 1 3

Explanation:
1st string onezero matches the 2nd integer 10.
2nd string eight matches the 4th integer 8.
3rd string twotwothree matches the 1st integer 223.
4th string fivenine matches the 3rd integer 59.

Example Input/Output 2:
Input:
3
sixsevenzero 1000
twothree 23
onezerozerozero 670

Output:
3 2 1
"""
def to_num(s):
    arr=["zero","one","two","three","four","five","six","seven","eight","nine"]
    t=''
    res=0
    for i in s:
        t+=i
        if len(t)>=3:
            try:
                ind=arr.index(t)
                t=''
                res=res*10+ind
            except ValueError:
                pass
    return res
n=int(input())
strings=[]
num=[]
for _ in range(n):
    a,b=input().split()
    strings.append(to_num(a))
    num.append(int(b))
for i in strings:
    print(num.index(i)+1,end=' ')
