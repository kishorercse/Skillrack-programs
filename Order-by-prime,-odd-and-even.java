/*
A set of numbers of size N which are separated by one or more spaces will be passed as input. The program should print the prime numbers first followed by odd numbers and
finally even numbers. Each of these categories, prime numbers, odd numbers and even numbers must be sorted in ascending order among themselves. The numbers which are prime must
be excluded from the list of odd and even numbers (In the case of even numbers only 2 is prime as well as even)

Input Format:
First line will contain the set of numbers separated by one or more spaces.

Output Format:
First line will contain the prime numbers, odd numbers, even numbers in the same order sorted in ascending order. The numbers must be separated exactly by one space.

Constraints:
Size of the set N will be from 2 to 20.

Example Input/Output 1:
Input:
4 5 9 22 11 2 15

Output:
2 5 11 9 15 4 22


Example Input/Output 2:
Input:
611953 494147 493137 493133 493138

Output:
493133 494147 611953 493137 493138

Explanation:
493133 494147 611953 are prime numbers.


*/
import java.util.*;
public class Hello {
    
    public static boolean isprime(int n)
    {
        if (n<=1)
            return false;
        if (n<=3)
            return true;
        if (n%2==0 || n%3==0)
            return false;
        int i=5;
        while (i*i<=n)
        {
            if (n%i==0 || n%(i+2)==0)
                return false;
            i+=6;
        }
        return true;
    }
    public static void print(ArrayList<Integer> al)
    {
        Collections.sort(al);
        for(int i:al)
            System.out.print(i+" ");
    }
    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		ArrayList<Integer> prime=new ArrayList<>(), even=new ArrayList<>(), odd=new ArrayList<>();
		while(sc.hasNextInt())
		{
		    int t=sc.nextInt();
		    if (isprime(t))
		        prime.add(t);
		    else if(t%2==0)
		        even.add(t);
		    else
		        odd.add(t);
		}
		print(prime);
		print(odd);
		print(even);
		

	}
}
