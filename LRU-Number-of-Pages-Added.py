"""
The program must accept N integers representing the N page requests and the size S of an LRU (Least Recently Used) cache as the input. After R requests the size of
the LRU cache is increased by X. The values of R and X are also passed as the input. The program must print the number of pages added in the cache when processing 
the N requests as the output.

Boundary Condition(s):
1 <= R < N <= 1000
1 <= Each integer value <= 1000
1 <= S, X <= 100

Input Format:
The first line contains N.
The second line contains N integer values separated by a space.
The third line contains S, R and X separated by a space.

Output Format:
The first line contains the number of pages added in the cache when processing the N requests.

Example Input/Output 1:
Input:
12
1 2 1 3 1 4 5 1 2 6 3 2
3 4 2

Output:
7

Explanation:
Here N = 12, S = 3, R = 4 and X = 2.
Initially, the cache is empty.
Page 1 is requested, so 1 is added to the cache. Now the cache contains 1.
Page 2 is requested, so 2 is added to the cache. Now the cache contains 2, 1.
Page 1 is requested again, but 1 is already in the cache. Now the cache contains 1, 2.
Page 3 is requested, so 3 is added to the cache. Now the cache contains 3, 1, 2.
Now 4 requests have been processed, so the size of cache has increased by 2.
Page 1 is requested again, but 1 is already in the cache. Now the cache contains 1, 3, 2.
Page 4 is requested, so 4 is added to the cache. Now the cache contains 4, 1, 3, 2.
Page 5 is requested, so 5 is added to the cache. Now the cache contains 5, 4, 1, 3, 2.
Page 1 is requested again, but 1 is already in the cache. Now the cache contains 1, 5, 4, 3, 2.
Page 2 is requested again, but 2 is already in the cache. Now the cache contains 2, 1, 5, 4, 3.
Page 6 is requested, so 6 is added to the cache. Now the cache contains 6, 2, 1, 5, 4.
Page 3 is requested again, but 3 is not in the cache. So 3 is added to the cache. Now the cache contains 3, 6, 2, 1, 5.
Page 2 is requested again, but 2 is already in the cache. Now the cache contains 2, 3, 6, 1, 5.
7 pages are added to the cache when processing the 12 requests. So 7 is printed as the output.

Example Input/Output 2:
Input:
15
7 8 10 8 7 6 6 4 2 1 1 10 9 3 4
5 10 1

Output:
10
"""
n=int(input())
req=list(map(int,input().split()))
s,r,x=map(int,input().split())
cache=[]
added=0
for i in range(n):
    try:
        cache.remove(req[i])
        cache.insert(0,req[i])
    except ValueError:
        cache.insert(0,req[i])
        added+=1
    if len(cache)>s:
        cache=cache[:s]
    if (i+1)==r:
        s+=x
print(added)
