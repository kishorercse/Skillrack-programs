s=input().strip()
t=''
flag=False
for i in s:
    if i==' ':
        if t:
            print(t,end=' ')
        t=''
        flag=True
    elif i==',':
        flag=False
    elif flag:
        t+=i
print(t)
