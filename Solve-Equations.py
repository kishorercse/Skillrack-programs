"""
Given two equations EQN1 and EQN2 containing the values of x co-efficient, y co-efficient and the resulting constant, the program must print the value of x and y 
separated by a space.

Input Format:
The first line contains the equation EQN1.
The second line contains the equation EQN2.

Output Format:
The first line contains the value of x and y separated by a space.

Boundary Conditions:
1 <= Co-efficient values <= 1000

Example Input/Output 1:
Input:
5x+2y=14
-4y+3x=-2

Output:
2 2

Example Input/Output 2:
Input:
4Y-5X=17
3X+4Y=9

Output:
-1 3
"""
class Equation:
    def set_a(self,a):
        self.a=a
    def set_b(self,b):
        self.b=b
    def set_c(self,c):
        self.c=c
def getabc(s):
    r=Equation()
    t=''
    for i in s:
        if i.isdigit() or i in "+-":
            t+=i
        else:
            if i=='x':
                r.set_a(int(t))
            elif i=='y':
                r.set_b(int(t))
            t=''
    r.set_c(int(t))
    return r
eq1=getabc(input().strip().lower())
eq2=getabc(input().strip().lower())
x=(eq2.b*eq1.c-eq1.b*eq2.c)//(eq1.a*eq2.b-eq1.b*eq2.a)
y=(eq1.c-eq1.a*x)//eq1.b
print(x,y)
