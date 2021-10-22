"""
The program must accept N three-digit numbers as the input. The program must find the bit score for all N numbers and then print the number of pairs possible based on these 
calculated bit score. 1) Rule for calculating the bit score from three-digit number: From the 3-digit number, - extract the largest digit and multiply by 11 then - extract 
the smallest digit and multiply by 7 then - add both the result for getting bit score. 

Note: Bit score should be of 2 digits, if above results in a 3-digit bit score, simply 
ignore the most significant digit. 

Consider the following examples: Say the number is 286, the largest digit is 8 and the smallest digit is 2. Bit score = 8*11 + 2*7 = 102. Ignore the most significant digit as 
it is a 3-digit number, so the bit score becomes 02. Say the number is 123, the largest digit is 3 and the smallest digit is 1. Bit score = 3*11 + 1*7 = 40. 2) Rules for making 
pairs from above calculated bit scores: Conditions to make bit pair are
- Both bit scores should be in either odd position or even position to be eligible to form a pair. 
- Pairs can be only made if the most significant digits are same and at most two pairs can be made for a given significant digit. 

Boundary Condition(s): 
2 <= N <= 500 

Input Format: 
The first line contains N. 
The second line contains N integers separated by a space. 

Output Format: 
The first line contains an integer representing the number of pairs based on the given conditions. 

Example Input/Output 1: 
Input: 
8 
234 567 321 345 123 110 767 111 

Output: 
3 

Explanation: 
After getting the most and least significant digits of the numbers and applying the formula given in Rule 1, we get the bit scores of the numbers as 58 12 40 76 40 11 19 18. 
The number of possible pairs is 3. 
40 appears twice at odd positions 3 and 5 respectively. Hence this is one pair. 
12, 11, 18 are at even positions. Hence two pairs are possible from these three bit scores. 
Hence the output is 3 

Example Input/Output 2: 
Input: 
20 
666 231 186 752 821 390 596 316 565 945 794 213 759 846 116 896 263 898 318 972 

Output: 
7
"""
def bit(n):  
    return (11*int(max(n))+7*int(min(n)))%100
n=int(input())
l=input().split()
odd={}
even={}
for i in range(n):
    l[i]=bit(l[i])//10
    if i%2==0:      
        odd[l[i]]=odd.get(l[i],0)+1
    else:  
        even[l[i]]=even.get(l[i],0)+1
count=0
for i in range(10):
    x=0
    if even.get(i,0)>1:
        x+=even[i]//2+even[i]%2
    if odd.get(i,0)>1:
        x+=odd[i]//2+odd[i]%2
    count+=min(2,x)
print(count)
