"""
Given an odd value of N, the program must print multi layered rhombus pattern in diamond shapes whose side contains N, N-2, ... 1 slashes respectively as shown below in the 
examples.

Input Format:
The first line contains N.

Output Format:
The  multi layered rhombus pattern in diamond shapes whose side contains N, N-2, ... 1 slashes respectively. Hash symbol is used as a filler for other values.

Boundary Conditions:
1 <= N <= 101 and N is odd.

Example Input/Output 1:
Input:
5

Output:
####/\####
###/##\###
##/#/\#\##
#/#/##\#\#
/#/#/\#\#\
\#\#\/#/#/
#\#\##/#/#
##\#\/#/##
###\##/###
####\/####

Example Input/Output 2:
Input:
11

Output:
##########/\##########
#########/##\#########
########/#/\#\########
#######/#/##\#\#######
######/#/#/\#\#\######
#####/#/#/##\#\#\#####
####/#/#/#/\#\#\#\####
###/#/#/#/##\#\#\#\###
##/#/#/#/#/\#\#\#\#\##
#/#/#/#/#/##\#\#\#\#\#
/#/#/#/#/#/\#\#\#\#\#\
\#\#\#\#\#\/#/#/#/#/#/
#\#\#\#\#\##/#/#/#/#/#
##\#\#\#\#\/#/#/#/#/##
###\#\#\#\##/#/#/#/###
####\#\#\#\/#/#/#/####
#####\#\#\##/#/#/#####
######\#\#\/#/#/######
#######\#\##/#/#######
########\#\/#/########
#########\##/#########
##########\/##########
"""
n=int(input())
m=[]
for i in range(n):
    s=''
    f=0
    for j in range(n):
        if j==n-i-1 or (f==1 and j%2==t):
            print('/',end='')
            f=1
            t=j%2
            s='\\'+s
        else:
            print('#',end='')
            s='#'+s
    m.insert(0,s[::-1]+s.replace('\\','/'))
    print(s)
for i in m:
    print(i)
