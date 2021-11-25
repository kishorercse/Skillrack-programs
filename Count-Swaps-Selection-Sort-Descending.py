"""
The program must accept N integers as the input. The program must print the number of swaps required when sorting the given N integers in descending order using selection sort 
as output.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the number of swaps required.

Example Input/Output 1:
Input:
5
50 20 10 40 30

Output:
2

Explanation:
The given 5 integers are 50 20 10 40 30.
After the 1st swap in selection sort -> 50 40 10 20 30.
After the 2nd swap in selection sort -> 50 40 30 20 10.
So the count 2 is printed as the output.

Example Input/Output 2:
Input:
6
2 4 5 1 3 6

Output:
4
"""
n=int(input())
l=list(map(int,input().split()))
swaps=0
for i in range(n):
    max_ind=i
    for j in range(i+1,n):
        if l[j]>l[max_ind]:
            max_ind=j
    if i!=max_ind:
        swaps+=1
        l[i],l[max_ind]=l[max_ind],l[i]
print(swaps)
