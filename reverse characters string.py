s=list(input().strip())
l=len(s)
for i in range(0,l-l%2,2):
    s[i],s[i+1]=s[i+1],s[i]
print(*s[::-1],sep='')
