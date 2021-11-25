"""
The program accepts three array elements with the size of the arrays as A, B and C as the input. All the integers in the given arrays are sorted in ascending order. The program
must merge the three sorted arrays so that the integers in the resulting array are sorted in ascending order. The program must print the original indices(i.e., the indices 
before merging) of all the integers in the resulting array. The indices of the given three arrays must be denoted as given below
1st array: a0, a1, a2, ... a(A-1).
2nd array: b0, b1, b2, ... b(B-1).
3rd array: c0, c1, c2, ... c(C-1).

Boundary Condition(s):
1 <= A, B, C <= 100
1 <= Each integer value <= 10^6

Input Format:
The first line contains A.
The second line contains A integers separated by a space.
The third line contains B.
The fourth line contains B integers separated by a space.
The fifth line contains C.
The sixth line contains C integers separated by a space.

Output Format:
The first line contains the original indices of all the integers in the resulting array separated by a space.

Example Input/Output 1:
Input:
5
10 20 50 90 100
4
15 25 35 40
6
5 30 39 45 60 98 99

Output:
c0 a0 b0 a1 b1 c1 b2 c2 b3 c3 a2 c4 a3 c5 c6 a4

Explanation:
Here A=5, B=4 and C=6.
After merging the given 3 arrays, the resulting array becomes
5 10 15 20 25 30 35 39 40 45 50 60 90 98 99 100

Example Input/Output 2:
Input:
3
10 10 20
3
10 20 20
3
10 10 20

Output:
a0 a1 b0 c0 c1 a2 b1 b2 c2
"""
def merge(l1,l2,a,b):
    res=[]
    i=j=0
    while i<a and j<b:
        if l1[i][1]<=l2[j][1]:
            res.append(l1[i])
            i+=1
        else:
            res.append(l2[j])
            j+=1
    if i<a:
        res+=l1[i:]
    elif j<b:
        res+=l2[j:]
    return res
a=int(input())
l1=list(map(int,input().split()))
b=int(input())
l2=list(map(int,input().split()))
c=int(input())
l3=list(map(int,input().split()))
l1=[['a'+str(i),l1[i]] for i in range(a)]
l2=[['b'+str(i),l2[i]] for i in range(b)]
l3=[['c'+str(i),l3[i]] for i in range(c)]
res=merge(l1,l2,a,b)
res=merge(res,l3,a+b,c)
for i in res:
    print(i[0],end=' ')
