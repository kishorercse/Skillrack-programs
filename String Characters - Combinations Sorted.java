/*
The program must accept a string S as the input. The program must print the combinations of the characters in the string S in sorted order.

Boundary Condition(s):
2 <= Length of S <= 15

Input Format:
The first line contains the string S.

Output Format:
The lines containing the string values representing the combinations of the characters in the string S in sorted order.

Example Input/Output 1:
Input:
abc

Output:
a
ab
abc
ac
b
bc
c

Example Input/Output 2:
Input:
virus

Output:
i
ir
irs
iru
irus
is
iu
ius
r
rs
ru
rus
s
u
us
v
vi
vir
virs
viru
virus
vis
viu
vius
vr
vrs
vru
vrus
vs
vu
vus
*/
import java.util.*;
public class Main {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String s=sc.next();
		int len=s.length();
		List<String> al=new ArrayList<>();
		for(int ctr=1;ctr< (1<<len);ctr++) {
		    StringBuilder sb=new StringBuilder();
		    for(int bmi=0;bmi<len;bmi++) {
		        if ((ctr&(1<<bmi))!=0) {
		            sb.append(s.charAt(bmi));
		        }
		    }
		    System.out.println(sb);
		    al.add(sb.toString());
		}
		Collections.sort(al);
		for(String a:al) {
		    System.out.println(a);
		}

	}
}
