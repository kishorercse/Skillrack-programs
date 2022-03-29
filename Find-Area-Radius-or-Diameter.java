/*
The program must accept an integer Q as the input. If the value of Q is 1, then the radius of a circle is passed as the input. If the value of Q is 2, then the 
diameter of a circle is passed as the input. The program must print the area of the circle with the precision up to 2 decimal places as the output.

Your task is to fill in the missing lines of code in the class Circle so that the program runs successfully.

Example Input/Output 1:
Input:
1
5

Output:
78.57

Explanation:
Here the value of Q is 1 and the radius of a circle is 5.
The area of the circle with the precision up to 2 decimal places is 78.57 ((22/7) * 5 * 5).

Example Input/Output 2:
Input:
2
7.5

Output:
44.20
*/
import java.util.*;

class Circle {

    private double radius;

    public Circle(int radius) {
        this.radius = radius;
    }
    public Circle(double diameter) {
        this.radius=diameter/2;
    }
    public double getArea() {
        return 22*radius*radius/7;
    }
}

public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int Q = Integer.parseInt(sc.nextLine().trim());
        Circle circle = null;
        if (Q == 1) {
            int radius = Integer.parseInt(sc.nextLine().trim());
            circle = new Circle(radius);
        } else if (Q == 2) {
            double diameter = Double.parseDouble(sc.nextLine().trim());
            circle = new Circle(diameter);
        }
        System.out.print(String.format("%.2f", circle.getArea()));
    }
} 
