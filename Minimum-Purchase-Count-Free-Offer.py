"""
A shop sells N items. Due to a festival offer, a customer if he purchases an item which is of price P, he will also get items whose price is either P+1 or P+2 or P+3 or P+4. 
Given the price of N items, the program must print the minimum number of times the customer must purchase to get one count purchased in all the available items making use of 
this offer.

Input Format:
The first line will contain N.
The second line will contain the prices of the N items, with the values separated by a space.

Output Format:
The first line will contain the minimum purchase count.

Boundary Conditions:
3 <= N <= 10000
The price of the items will be from 1 to 1000.

Example Input/Output 1:
Input:
4
1 2 5 5

Output:
1

Explanation:
If the customer buys the item with price as 1, then he will get the three items priced 2,5,5 also free as they are within the range P+4.
Hence the customer needs to buy only once.

Example Input/Output 2:
Input:
11
1 2 5 7 19 20 12 11 9 15 19

Output:
4

Explanation:
When the customer buys item with price as 1, he will get items with price as 2 and 5 free.
When he buys item with price 7, he will get items with price as 9 and 11 free.
When he buys item with price 12, he will get items with price as 15 free.
He then buys item with price 19 and gets the item with the price as 20 free.
"""
n=int(input())
l=sorted(map(int,input().split()))
flags={}
i=0
ans=0
while i<n:
    if flags.get(l[i],1)!=-1:
        flags[l[i]]=-1
        for p in range(l[i]+1,l[i]+5):
            flags[p]=-1
        ans+=1
    i+=1
print(ans)
