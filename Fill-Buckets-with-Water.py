"""
There are N buckets arranged in a row. The amount of water in each bucket is passed as the input. All N buckets have the same capacity C which is also passed as the input. A
boy wants to fill as many buckets as possible based on the following conditions.
- He chooses the leftmost incomplete bucket(i.e., the bucket with less water than capacity), and he fills the remaining incomplete buckets from left to right using the water 
in the chosen bucket. Once the chosen bucket is empty, he removes that bucket from the row.
- Then he repeats the process of filling the buckets till all the buckets are stable.
Finally, the program must print the amount of water in the remaining buckets as the output.

Boundary Condition(s):
2 <= N <= 100
1 <= Amount of water in each bucket <= C <= 1000

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains C.

Output Format:
The first line contains the integer values representing the amount of water in the remaining buckets.

Example Input/Output 1:
Input:
5
5 8 3 7 9
10

Output:
10 2 10 10

Explanation:
Here N = 5 and C = 10.
Buckets = [5 8 3 7 9]
He chooses the 1st bucket and fills the 2nd and 3rd buckets. Then he removes the 1st bucket from the row as it becomes empty.
Buckets = [10 6 7 9]
He chooses the 2nd bucket and fills the 3rd and 4th buckets. Now there are 2 liters of water left in the 2nd bucket.
Buckets = [10 2 10 10]
Now all the buckets are stable, so he stops.

Example Input/Output 2:
Input:
5
10 10 8 8 8
10

Output:
10 10 4 10 10

Example Input/Output 3:
Input:
4
10 9 2 9
10

Output:
10 10 10

Example Input/Output 4:
Input:
6
1 1 1 1 1 1
10

Output:
6
"""
n=int(input())
l=list(map(int,input().split()))
c=int(input())
for i in range(n):
    if l[i]<c:
        for j in range(i+1,n):
            if l[j]<c:
                diff=c-l[j]
                if diff<l[i]:
                    l[i]-=diff
                    l[j]=c
                else:
                    l[j]+=l[i]
                    l[i]=0
                    break
for i in l:
    if i!=0:
        print(i,end=' ')
