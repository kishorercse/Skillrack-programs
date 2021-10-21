"""

John is a pure Desi boy. And his one and only dream is to meet Santa Claus. He decided to decorate a Christmas tree for Santa on coming Christmas. John made an interesting Christmas tree that grows day by day.

The Christmas tree is comprised of the following:
– Parts
– Stand
Each Part is further comprised of Branches. 
Branches are comprised of Leaves.

How the tree appears as a function of days should be understood. Basis that print the tree as it appears on the given day. Below are the rules that govern how the tree appears on a given day. Write a program to generate such a Christmas tree whose input is the number of days.

Rules:
1) If the tree is one day old, you cannot grow. Print a message “You cannot generate christmas tree” 
2) Tree will die after 20 days. It should give a message “Tree is no more” 
3) Tree will have one part less than the number of days.
    E.g. On the 2nd day, the tree will have 1 part and one stand.
           On the 3rd day, the tree will have 2 parts and one stand.
           On the 4th day, the tree will have 3 parts and one stand and so on. 
4) Top-most part will be the widest and bottom-most part will be the narrowest. 
5) Difference in number of branches between top-most and second from the top will be 2.
6) Difference in number of branches between second from top and bottom-most part will be 1.

Below is an illustration of how the tree looks like on 4th day




Boundary Condition(s):
1 <= N <= 100

Input Format:
The first line contains the number of days.

Output Format:
The lines contain the Christmas tree or one of the mentioned messages.

Example Input/Output 1:
Input:
4

Output:
----*
---***
--*****
-*******
*********
---***
--*****
-*******
---***
--*****
----*
----*
Example Input/Output 2:
Input:
7

Output:
-------*
------***
-----*****
----*******
---*********
--***********
-*************
***************
------***
-----*****
----*******
---*********
--***********
-*************
------***
-----*****
----*******
---*********
--***********
------***
-----*****
----*******
---*********
------***
-----*****
----*******
------***
-----*****
-------*
-------*
"""
n=int(input())
if n==1:
    print("You cannot generate christmas tree")
elif n>20:
    print("Tree is no more")
else:
    t=1
    l=[]
    for i in range(n+1):
        s='-'*(n-i)+'*'*t
        print(s)
        l.append(s)
        t+=2
    stand=l.pop(0)
    l=l[:-1]
    t=n
    while t>2:
        for i in l:
            print(i)
        l=l[:-1]
        t-=1
    print(stand)
    print(stand)
