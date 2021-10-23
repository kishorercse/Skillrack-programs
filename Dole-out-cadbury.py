"""
In a school, a teacher is assigned to distribute the Cadbury to the students for Independence Day. The teacher has a box full of Cadbury with different width and height. He can only distribute the largest square shape Cadbury. So if he has a Cadbury of length 10 and width 5, then he needs to break the Cadbury in 5×5 square and distribute to the first student and then the remaining 5×5 square to the next student in the queue. The program must accept four integers P, Q, R and S representing the minimum length, maximum length, minimum width and maximum width of Cadbury in the box as the input. The program must print the total number of students who will get the Cadbury as the output.

Boundary Condition(s):
1 <= P < Q <= 1500
1 <= R < S <= 1500
 
Input Format:
The first line contains P, Q, R and S separated by a space.

Output Format:
The first line contains the total number of students who will get the Cadbury.

Example Input/Output 1:
Input:
5 6 3 4

Output:
14

Explanation:
There are four possible sizes of Cadbury.
5×3, 5×4, 6×3 and 6×4.

The size of the first Cadbury is 5×3.
The first student gets 3×3. The size of the remaining Cadbury is 2×3.
The next student gets 2×2. The size of the remaining Cadbury is 2×1.
The next two students get 1×1 each.
So 4 students can get the Cadbury from the 5×3 Cadbury.
 
The size of the second Cadbury is 5×4.
The first student gets 4×4. The size of the remaining Cadbury is 1×4.
The next four students get 1×1 each.
So 5 students can get the Cadbury from the 5×4 Cadbury.

The size of the third Cadbury is 6×3.
The first two students get 3×3 each.
So 2 students can get the Cadbury from the 6×3 Cadbury.

The size of the fourth Cadbury is 6×4.
The first student gets 4×4. The size of the remaining Cadbury is 2×4.
The next two students get 2×2 each.
So 3 students can get the Cadbury from the 6×4 Cadbury.

Hence 14 students can get the Cadbury from the box. So 14 is printed as the output.

Example Input/Output 2:
Input:
1 3 10 12

Output:
67
"""
p,q,r,s=map(int,input().split())
res=0
for i in range(p,q+1):
    for j in range(r,s+1):
        a,b=i,j
        c=0
        while a and b:
            if a>b:
                c+=a//b
                a=a%b
            else:
                c+=b//a
                b=b%a
        res+=c
print(res)
