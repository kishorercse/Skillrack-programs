"""
Manisha and Ranjani are in the same class and are friends. All students in the class write N exams. In order to motivate the students, the school announces that two students
can form a team and rearrange their marks in N exams as N pairs so that the sum of the absolute difference of these N pairs is minimum. Hence Manisha and Ranjani decides to
write a program which will calculate this minimum sum of absolute difference between the N pairs of marks. Help them by completing the program based on the details given below.

Input Format:
The first line will contain N.
The second line will contain scores obtained by Manisha in N exams separated by a space.
The third line will contain scores obtained by Ranjani in N exams separated by a space.

Output Format:
The first line will contain the minimum possible sum of the absolute difference between the N pairs of marks.

Boundary Conditions:
3 <= N <= 100

Example Input/Output 1:
Input:
5
2 2 2 2 2
3 3 3 3 3

Output:
5

Example Input/Output 2:
Input:
4
4 1 8 7
2 3 5 6

Output:
6

Explanation:
The minimum sum = (8-6) + (7-5) + (4-3) + (2-1) = 6
"""
n=int(input())
a=sorted(map(int,input().split()))
b=sorted(map(int,input().split()))
Sum=0
for i in range(n):
    Sum+=abs(a[i]-b[i])
print(Sum)
