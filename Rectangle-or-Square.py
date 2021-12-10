"""
Vignesh is very much interested in Geometry and he was reading about Rectangles and Squares. He wanted a program which will print Rectangle or Square based on the perimeter P 
and the area A provided.
Please help Vignesh by completing the program for him. (Eventhough Square is a Rectangle, if length is equal to breadth, the output must be Square).

Input Format:
First line contains total number of test cases, denoted by T
Next T lines, contains P and A separated by one or more space(s).


Output Format:
Rectangle or Square

Boundary Conditions / Constraints:
1 <= T <= 25
4 <= P <= 9999999
1 <= A <= 9999999
All values will be postive integers and no floating point values. Only valid Rectangle or Square measurements will be provided as input.


Example Input/Output 1:
Input:
3
4 1
24 32
24 36

Output:
Square
Rectangle
Square

Explanation:
The first line in the input denotes there are 3 test cases.
For 4 1, it is a Square whose side is 1 unit.
For 24 32, it is a Rectangle with length = 8 units and breadth = 4 units.
For 24 36, it is a Square whose side is 6 units.
"""
t=int(input())
while t > 0:
    p,a=map(int,input().split())
    l=(p+(p*p-16*a))//4
    br=a//l
    if l==br:
        print("Square")
    else:
        print("Rectangle")
    t-=1
