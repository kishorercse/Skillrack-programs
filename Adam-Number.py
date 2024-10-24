"""
A number is said to be an Adam number if the reverse of the square of the number is equal to the square of the reverse of the number.  
For example, 12 is an Adam number because the reverse of the square of 12 is the reverse of 144, which is 441, and the square of the reverse 
of 12 is the square of 21, which is also 441.
"""
def reverse(n):
    return int(str(n)[::-1])
n=int(input())
a=n**2
b=reverse(reverse(n)**2)
if a==b:
    print("Adam Number")
else:
    print("Not Adam Number")
