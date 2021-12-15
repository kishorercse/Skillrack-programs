"""
A book can be turned either from front or from the back. When we open a book always we have the page 1 always on the right. The book pages must always be turned one by one 
instead of multiple pages at once. Each page has two sides, front and back. Hence the last page may have only front side depending on the total number of pages N in the book
(If N is even, it will have both sides printed else if N is odd only the front side will be printed).

Now Manoj wants to navigate to a page P in the book by turning the least minimum pages either from front or back. Please help Manoj by completing the program as per the given
requirement.

Input Format:
The first line will contain the value of N which represents the total number of pages in the book.
The second line will contain the value of P which represents the page to be navigated.

Output Format:
The first line will contain the integer value which is the least minimum pages to be turned either from front or back.

Constraints:
1 <= N <= 10000
1 <= P <= N

Example Input/Output 1:
Input:
8
6

Output:
1

Explanation:
From front, after turn 1, pages 2 & 3 are visible. After turn 2, pages 4 & 5 are visible. In the third turn pages 6 & 7 are visible. So 3 turns are required from front.
From back the last page back side is page 8. So after turn 1, pages 6 & 7 are visible. So 1 turn is required from the back.
The minimum of 3 and 1 (which is 1) is printed as the output.


Example Input/Output 2:
Input:
12
4

Output:
2

Explanation:
From front, after turn 1, pages 2 & 3 are visible. After turn 2, pages 4 & 5 are visible. So 2 turns are required from front.
From back the last page back side is page 12. So after turn 1, pages 10 & 11 are visible. After turn 2, pages 8 & 9 are visible. After turn 3, pages 6 & 7 are visible.
Only after turn 4, pages 4 and 5 are visible. So 4 turns are required from the back.
The minimum of 2 and 4 (which is 2) is printed as the output.
"""
n=int(input())
p=int(input())
front=p//2
back=(n-p+(n%2==0))//2
print(min(front,back))
