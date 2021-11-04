"""
(Id-12690) Author: SkillRack The program must accept N integers as the input. For each integer X among the N integers, the program must shift the largest digit in X to the left. If the largest digit occurs more than once in an integer, the program must shift the last occurring largest digit to the left. Then the program must print the sum of the N modified integers as the output. Boundary Condition(s): 1 <= N <= 100 1 <= Each integer value <= 10^5 Input Format: The first line contains N. The second line contains N integers separated by a space. Output Format: The first line contains an integer representing the sum of the N modified integers. Example Input/Output 1: Input: 4 4613 234 6969 2990 Output: 25822 Explanation: Here N = 4. After shifting the largest digit in each integer to the left, the integers become 6413 423 9696 9290. The sum of the 4 modified integers is 25822. So 25822 is printed as the output. Example Input/Output 2: Input: 7 62 511 808 264 590 5 3453 Output: 8375
"""
def shift(a):
    mx='0'
    for i in range(len(a)):
        if a[i]>=mx:
            mx=a[i]
            ind=i
    return int(a[ind]+a[:ind]+a[ind+1:])
n=int(input())
l=input().split()
s=0
for i in l:
    s+=shift(i)
print(s)
