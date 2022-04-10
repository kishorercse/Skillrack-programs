/*
The program must accept two string values S1 and S2 representing two sentences as the input. The program must print YES if the two sentences are shadows of each other.
Else the program must print NO as the output. If two sentences are shadows of each other, then the following conditions must be true.
- The number of words in both sentences must be equal.
- The length of each word that occurs in the same position in both sentences must be equal, but the corresponding words must not share any common characters.

Boundary Condition(s):
1 <= Length of S1, S2 <= 1000

Input Format:
The first line contains S1.
The second line contains S2.

Output Format:
The first line contains YES or NO.

Example Input/Output 1:
Input:
four ten history
tent was damaged

Output:
YES

Explanation:
The two string values S1 and S2 contain 3 words each.
The length of each word S1 is equal to the length of the corresponding word in the same position in S2.
The words four and tent have no common characters.
The words ten and was have no common characters.
The words history and damaged have no common characters.
So YES is printed as the output.

Example Input/Output 2:
Input:
hat mat tiger elephant
run gun water keyboard

Output:
NO

Example Input/Output 3:
Input:
mobile camera
army ant nano

Output:
NO
*/
import java.util.*;
public class Hello {
    public static boolean isShadow(String arr1[], String arr2[]) {
        int l1=arr1.length, l2=arr2.length;
        if (l1!=l2)
            return false;
        for(int i=0;i<l1;i++) {
            int a=arr1[i].length(), b=arr2[i].length();
            if (a!=b)
                return false;
            for(int j=0;j<a;j++) {
                if (arr1[i].contains(""+arr2[i].charAt(j))) {
                    return false;
                }
            }
        }
        return true;
    }
    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String arr1[]=sc.nextLine().split(" "), arr2[]=sc.nextLine().split(" ");
		if (isShadow(arr1,arr2)) {
		    System.out.print("YES");
		}else {
		    System.out.print("NO");
		}
	}
}
