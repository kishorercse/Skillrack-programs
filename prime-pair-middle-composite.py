"""
The program must accept an integer N as the input. The program must find two consecutive prime integers X and Y,
where the middle integer in the range (X,Y) is equal to N (i.e., N is a composite integer which is equidistant from
two consecutive primes X and Y). If there is no such prime pair, then the program must print -1 as the output.

Boundary Condition(s):
2 <= N <= 10^5

Input Format:
The first line contains N.

Output Format: 
The first line contains X and Y separated by a space or -1. 

Example Input/Output 1: 
Input: 
6 

Output: 
5 7 

Explanation: 
Here N = 6, which is a composite integer. 
So the prime pair is (5, 7). 6-5 = 7-6 = 1. 

Example Input/Output 2: 
Input: 
473 

Output: 
467 479 

Example Input/Output 3: 
Input: 
10 

Output: 
-1
"""
def prime(a,b):
    f1=f2=-1
    if a<=1:
        f1=False
    if b<=1:
        f2=False
    if a==2 or a==3:
        f1=True
    if a==2 or b==3:
        f2=True
    if f1!=-1 and f2!=-1:
        return (f1,f2)
    if (a!=2 and a%2==0) or (a!=3 and a%3==0):
        f1=False
    if (b!=2 and b%2==0) or (b!=3 and b%3==0):
        f2=False
    if f1!=-1 and f2!=-1:
        return (f1,f2)
    i=5
    while i*i<=b:
        if a%i==0 or a%(i+2)==0:
            f1=False
        if b%i==0 or b%(i+2)==0:
            f2=False
        if f1!=-1 and f2!=-1:
            break
        i+=6
    if f1==-1:
        f1=True
    if f2==-1:
        f2=True
    return (f1,f2)
n=int(input())
if (prime(n,n)==(True,True)):
    print(-1)
else:
    x=n-1-n%2
    y=n+1+n%2
    while x>1:
        a,b=prime(x,y)
        if a and b:
            print(x,y)
            break
        elif a or b:
            print(-1)
            break
        x-=2
        y+=2
    else:
        print(-1)
