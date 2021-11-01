/*
The program must accept two integers X and Y as the input. The program must print the output based on the following conditions. 
- If both X and Y are divisible by 5, the program must print the sum of X and Y. 
- Else the program must add 5 as the unit digit of both X and Y. 
Then the program must print the sum of X and Y. 

Boundary Condition(s): 
1 <= X, Y <= 10^4 

Input Format: 
The first line contains X and Y separated by a space. 

Output Format: 
The first line contains the sum of X and Y based on the given conditions. 

Example Input/Output 1: 
Input: 
45 620 

Output: 
665 

Explanation:
X = 45 and Y = 620.
Both X and Y are divisible by 5. 
So their sum 665 is printed as the output. 

Example Input/Output 2:
Input: 
34 12 

Output: 
470 

Explanation:
X = 34 and Y = 12. 
Both X and Y are not divisible by 5. 
So the values of X and Y become 345 and 125. Now the their sum is 470, which is printed as the output.

Example Input/Output 3:
Input: 
97 45 

Output:
1430
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int x=sc.nextInt(), y=sc.nextInt();
		if (x%5==0 && y%5==0)
		    System.out.print(x+y);
		else
		    System.out.print(x*10+5 + y*10+5);

	}
}
