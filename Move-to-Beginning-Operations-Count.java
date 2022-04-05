/*
The program must accept a string S and two integers X, Y as the input. The program must perform the following two operations alternately on the given string S until
the string becomes the original string.
- Move the last X characters to the beginning.
- Move the last Y characters to the beginning.
Finally, the program must print the number of operations performed on the given string S as the output.

Boundary Condition(s):
1 <= Length of S <= 100
1 <= X, Y <= Length of S

Input Format:
The first line contains S.
The second line contains X and Y separated by a space.

Output Format:
The first line contains an integer representing the number of operations performed on the given string S.

Example Input/Output 1:
Input:
high
1 2

Output:
3

Explanation:
Here X = 1 and Y = 2.
1st operation: high -> hhig
2nd operation: hhig -> ighh
3rd operation: ighh -> high

Example Input/Output 2:
Input:
SkillRack
3 1

Output:
13

Explanation:
Here X = 3 and Y = 1.
1st operation: SkillRack -> ackSkillR
2nd operation: ackSkillR -> RackSkill
3rd operation: RackSkill -> illRackSk
4th operation: illRackSk -> killRackS
5th operation: killRackS -> ckSkillRa
6th operation: ckSkillRa -> ackSkillR
7th operation: ackSkillR -> llRackSki
8th operation: llRackSki -> illRackSk
9th operation: illRackSk -> kSkillRac
10th operation: kSkillRac -> ckSkillRa
11th operation: ckSkillRa -> lRackSkil
12th operation: lRackSkil -> llRackSki
13th operation: llRackSki -> SkillRack
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next(), t = s;
		int x = sc.nextInt(), y = sc.nextInt(), count = 0, len = s.length();
		do {
		    if (count%2==0) {
		        t=t.substring(len-x)+t.substring(0,len-x);
		    }
		    else {
		        t=t.substring(len-y)+t.substring(0,len-y);
		    }
		    count++;
		}while(!t.equals(s));
		System.out.print(count);

	}
}
