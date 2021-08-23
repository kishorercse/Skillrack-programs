n=0
l=[]
while True:
    try:
        l.append(int(input()))
        n+=1
    except:
        break
for i in range(2,n//2+1):
    if n%i==0:
        t=max(n//i,i)
        break
else:
    t=1
while l:
    print(sum(l[:t]),end=' ')
    l=l[t:]
