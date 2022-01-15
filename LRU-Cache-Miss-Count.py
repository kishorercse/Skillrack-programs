"""
The least recently used (LRU) cache algorithm evicts the element from the cache that was least recently used when the cache is full. After an element is requested from the 
cache, it should be added to the cache (if not there) and considered the most recently used element in the cache whether it is newly added or was already existing.

Initially, the cache is empty. Implement the function lruCountMiss so that the function returns an integer indicating the number of cache misses M using the LRU cache algorithm 
execution for the given input.

Assume that the array pages always have pages numbered from 0 to 50. (A hit means the requested page is already existing in the cache and a miss means the requested page is not 
found in the cache).

Input Format:
The first line contains the cache size S and the number of page requests N separated by a space.
The second line containing the N pages being requested from the cache.

Output Format:
The first line contains the miss count M.

Boundary Conditions:
2 <= S <= N
2 <= N <= 100

Example Input/Output 1:
Input:
3 16
7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0

Output:
11

Example Input/Output 2:
Input:
2 9
2 3 1 3 2 1 4 3 2

Output:
8
"""
def lruCountMiss(size, pages):
    miss=0
    filled=0
    present=[0]*51
    cache=[]
    for i in pages:
        if present[i]==0:
            miss+=1
            present[i]=1
            filled+=1
            if filled>size:
                present[cache.pop(0)]=0
                filled-=1
        else:
            cache.remove(i)
        cache.append(i)
    return miss
s,n=map(int,input().split())
pages=list(map(int,input().split()))
print(lruCountMiss(s,pages))
