"""
An array of N integers is passed as the input. The program must find the combination of integers forming a sequence whose length is more than 4 which satisfies the below conditions.
– The ith  index must satisfy arr[i] = arr[i-1] + arr[i-2]
– The length of the sequence must be the maximum possible
– If there are more than one sequences satisfying above two conditions, then print the sequence which contains the smaller value integers.

If there is no such combination of integers, then the program must print -1.

Boundary Condition(s):
1 <= N <= 25

Input Format:
The first line contains N.
The second line contains the N integer values separated by a space.

Output Format:
The first line contains the integer values in the sequence or -1.

Example Input/Output 1:
Input:
9
4 2 7 5 3 8 10 11 19

Output:
2 3 5 8

Explanation:
2 3 5 8 and 3 8 11 19 are the two sequences having same length. But as 2 3 5 8 contains the smaller values, it is printed as the output.

Example Input/Output 2:
Input:
4
1 5 6 10

Output:
-1

Explanation:
Here the sequence 1 5 6 length is not 4. Hence -1 is printed.
"""
n=int(input())
l=sorted(map(int,input().split()))
max_len=0
ans=[]
for i in range(n):
    for j in range(i+1,n):
        t=[l[i],l[j]]
        s=l[i]+l[j]
        length=2
        for k in range(j+1,n):
            if t[-1]+t[-2]==l[k]:
                t.append(l[k])
                s+=l[k]
                length+=1
        t.append(s)              # adding sum of t list to end of list for comparing with previous ans list
        if length>=4:
            if length>max_len:
                max_len=length
                ans=t[:]
            elif length==max_len and t[-1]<ans[-1]:
                ans=t[:]
if max_len==0:
    print(-1)
else:
    print(*ans[:-1])
