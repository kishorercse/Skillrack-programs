"""
A man is running a super market and he observes the pattern of customer buying peanuts in packs of 1 kg, 2 kgs, 3 kgs till N kgs. So based on the buying pattern and his
observation he can price the packs of 1 kg, 2 kgs, ... N kgs  at rupees P(1), P(2), P(3), ... P(N) respectively. What is the maximum revenue he can earn when selling N kgs of 
peanuts based on the given pricing?

Input Format:
The first line contains N.
The second line contains the integer value denoting the price for 1 kg pack, 2 kgs pack till N kgs pack with each value separated by a space.

Output Format:
The first line contains the maximum revenue he can earn by packing and selling the N kgs peanuts based on the given pricing.

Boundary Conditions:
1 <= N <= 999

Example Input/Output 1:
Input:
4
120 250 360 490

Output:
500

Explanation:
While selling 4 kgs of peanuts, the maximum revenue of Rs.500 is obtained when he packs the 4 kgs as 2 kgs + 2kgs and sells them at Rs. 250 each.

Example Input/Output 2:
Input:
4
120 240 360 490

Output:
490

Explanation:
While selling 4 kgs of peanuts, the maximum revenue of Rs.490 is obtained when he packs the 4 kgs as a single 4 kgs pack and sells it ar Rs.490
"""
n=int(input())
l=[0]+list(map(int,input().split()))
mx=-1
for i in range(1,n+1):
    if n%i==0:
        mx=max(l[i]*(n//i),mx)
    else:
        mx=max(l[i]*(n//i)+l[n%i],mx)
print(mx)
