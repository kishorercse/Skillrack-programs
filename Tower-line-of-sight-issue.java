/*
Four towers A, B, C, D are to be erected. Tower A is to communicate with tower C. Tower B is to communicate with tower D. Line of sight issue can occur under the following 
conditions 
- when tower B or D is in the straight line connecting A and C 
- when tower A or C is in the straight line connecting B and D 
The program must accept the co-ordinates of all four towers and print yes or no depending on whether Line of sight issue will occur or not. 

Input Format: 
The first line will contain X and Y co-ordinates of tower A separated by a space. 
The second line will contain X and Y co-ordinates of tower B separated by a space. 
The third line will contain X and Y co-ordinates of tower C separated by a space. 
The fourth line will contain X and Y co-ordinates of tower D separated by a space 

Output Format: 
The first line will contain yes or no (smaller case) 

Boundary Conditions:
The value of the co-ordinates will be from -500 to 500.

Example Input/Output 1: 
0 0
0 -2
2 0
0 2 

Output:
yes 

Example Input/Output 2: 
Input: 
0 0 
0 -2 
2 0 
0 -5 

Output: 
no
*/
import java.util.*;
public class Hello {
    
    public static boolean checkIntersection(int x1, int y1, int x2, int y2, int x, int y){
        // Checking if Distance between (x1,y1) and (x2,y2) is equal to sum of distances between ((x1,y1) and (x,y)) and ((x2,y2) and (x,y))
        return Math.sqrt(Math.pow(x-x1,2)+Math.pow(y-y1,2))+Math.sqrt(Math.pow(x-x2,2)+Math.pow(y-y2,2))==Math.sqrt(Math.pow(x2-x1,2) + Math.pow(y2-y1,2));
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
		int ax=sc.nextInt(), ay=sc.nextInt(), bx=sc.nextInt(), by=sc.nextInt(), cx=sc.nextInt(), cy=sc.nextInt() , dx=sc.nextInt(), dy=sc.nextInt();
		
		if (checkIntersection(ax,ay,cx,cy,bx,by) || checkIntersection(ax,ay,cx,cy,dx,dy) || checkIntersection(bx,by,dx,dy,ax,ay) || checkIntersection(bx,by,dx,dy,cx,cy))
		    System.out.print("yes");
		else
		    System.out.print("no");

	}
}
