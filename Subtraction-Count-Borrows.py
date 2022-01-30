"""
The program must accept two integers X and Y (where X >= Y) as the input. The program must print the number of borrows needed when subtracting Y from X as the output.

Boundary Condition(s):
1 <= Y <= X <= 10^8

Input Format:
The first line contains X.
The second line contains Y.

Output Format:
The first line contains an integer representing the number of borrows needed when subtracting Y from X.

Example Input/Output 1:
Input:
9643
9171

Output:
1

Explanation:
Here X=9643 and Y=9171.
The unit digit 1 can subtract from the unit digit 3 and hence NO borrows.
The tenth digit 7 cannot subtract from the tenth digit 4. So borrows 1 from the hundredth digit 6.
The hundredth digit 1 can subtract from the hundredth digit 5 and hence NO borrows.
The thousandth digit 9 can subtract from the thousandth digit 9 and hence NO borrows.
Total number of borrows is 1, which is printed as the output.

Example Input/Output 2:
Input:
4506
129

Output:
2

Explanation:
Here X=4506 and Y=129.
The unit digit 9 cannot subtract from the unit digit 6. The digit 6 cannot borrow 1 from the tenth digit as it was already 0.
The digit 6 borrows 1 from the hundredth digit, Now the hundredth digit becomes 4 and the tenth digit becomes 9. So the borrows count is 2.
The tenth digit 2 can subtract from the tenth digit 9 and hence NO borrows.
The hundredth digit 1 can subtract from the hundredth digit 4 and hence NO borrows.
Total number of borrows is 2, which is printed as the output.
"""
x=list(map(int,input().strip()))
y=int(input())
borrows=0
ind=-1
while y>0:
    if x[ind]<y%10:
        borrows+=1
        if x[ind-1]==0:
            p=ind-1
            while x[p]==0:
                x[p]=9
                borrows+=1
                p-=1
            x[p]-=1
        else:
            x[ind-1]-=1
    y//=10
    ind-=1
print(borrows)
