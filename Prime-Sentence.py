"""
The program must accept a string S representing a sentence as the input. The program must find the sentence value of S based on the following conditions.
- All 26 alphabets from a to z or from A to Z have values are from 1 to 26 respectively.
- All 10 digits from 0 to 9 have values are from 0 to 9 respectively.
- All the other characters have the value 0.
- The sentence value is obtained by summing up all the numeric values of every single character in S.
Then the program must print the output based on the following conditions.
- If the sentence value is a prime number, then the program must print "Prime".
- If the sentence value is a prime number after removing exactly one word in the sentence, then the program must print "Almost Prime".
- Otherwise, the program must print "Composite".

Boundary Condition(s):
1 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The first line contains a string value based on the given conditions.

Example Input/Output 1:
Input:
Lift dog

Output:
Prime

Explanation:
Lift -> (12+9+6+20) -> 47
dog -> (4+15+7) -> 26
So the sentence value is 73 (47+26), which is a prime number.
Hence the output is Prime.

Example Input/Output 2:
Input:
Is 24 the answer?

Output:
Almost Prime

Explanation:
Is -> (9+19) -> 28
24 -> (2+4) -> 6
the -> (20+8+5) -> 33
answer? -> (1+14+19+23+5+18+0) -> 80
So the sentence value is 147 (28+6+33+80), which is not a prime number.
If the word "answer?" is removed, the sentence value becomes 67, which is a prime number.
Hence the output is Almost Prime.

Example Input/Output 3:
Input:
Hello World!

Output:
Composite
"""
def isprime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True
s=input().strip().lower().split()
l=[]
val=0
for i in s:
    t=0
    for j in i:
        if j.isalpha():
            t+=ord(j)-96
        elif j.isdigit():
            t+=int(j)
    l.append(t)
    val+=t
if isprime(val):
    print("Prime")
else:
    for i in l:
        if isprime(val-i):
            print("Almost Prime")
            break
    else:
        print("Composite")
