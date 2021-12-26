n=int(input())
l=list(map(int,input().split()))
k=int(input())
l=[[i,bin(i)[2:][-k:].lstrip('0')] for i in l]
res=[l[0][0]]
for i in range(1,n):
    if l[i-1][1]==l[i][1]:
        res[-1]+=l[i][0]
    else:
        res.append(l[i][0])
print(*res,)
