"""
The program must accept N integers as the input, but certain digits in some integers are denoted in words (in lower case). The program must find the integer values and print 
their sum as the output.
Note: The value of each integer less than or equal to 10^5.

Boundary Condition(s):
1 <= N <= 100

Input Format:
The first line contains N.
The second line contains N integers separated by a space, but certain digits in some integers are denoted in words.

Output Format:
The first line contains an integer representing the sum of N integers.

Example Input/Output 1:
Input:
4
10zero five6 75 2four9

Output:
480

Explanation:
10zero -> 100
five6 -> 56
75 -> 75
2four9 -> 249
100 + 56 + 75 + 249 = 480

Example Input/Output 2:
Input:
5
six38eight four70three 3seven4zero threefivethreeseven 15eight4

Output:
19952

Explanation:
six38eight -> 6388
four70three -> 4703
3seven4zero -> 3740
threefivethreeseven -> 3537
15eight4 -> 1584
6388 + 4703 + 3740 + 3537 + 1584 = 19952
"""
n=int(input())
l=input().split()
al=['zero','one','two','three','four','five','six','seven','eight','nine']
ans=0
for i in l:
    num=0
    s=''
    for ch in i:
        if ch.isdigit():
            num=num*10+int(ch)
        else:
            s+=ch
            if len(s)>=3:
                try:
                    ind=al.index(s)
                    if ind!=-1:
                        num=num*10+ind
                        s=''
                except ValueError:
                    pass
    ans+=num
print(ans)
