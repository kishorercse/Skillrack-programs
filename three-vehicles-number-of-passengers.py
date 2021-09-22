"""
Output Format: 
The first line contains the integer values representing the number of passengers. 

Example Input/Output 1: 
Input: 
5 4 10 

Output: 
4 5 9 10 14 15 19 

Explanation: 

When just 1 car alone is used the filled capacity is 4 5 and 10. 
When Car 1 and 2 are filled, the count of passengers is 9. 
When Car 1 and 3 are filled, the count of passengers is 15. 
Similarly, for Car 2 and 3 it is 14. 
When all three cars are filled, the count is 19. 
The output is these count of passengers sorted in ascending order. 

Example Input/Output 2: 
Input: 
15 10 12 

Output: 
10 12 15 22 25 27 37
"""
l=list(map(int,input().split()))
l.append(sum(l))
for i in range(3):
    for j in range(i+1,3):
        l.append(l[i]+l[j])
print(*sorted(l))
