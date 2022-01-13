def reverse(n):
    return int(str(n)[::-1])
n=int(input())
a=n**2
b=reverse(reverse(n)**2)
if a==b:
    print("Adam Number")
else:
    print("Not Adam Number")
