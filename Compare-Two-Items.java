/*
The program must accept the name, weight and price of two items as the input. The program must print the string value "SAME" if both items have the same name and the same
weight or price. Else the program must print the string value "NOT SAME" as the output. Then the program must print the name, weight and price of the two items as shown in
the Example Input/Output section.

Note: Ignore the case when comparing the names of the items.

Your task is to define the class Item so that the program runs successfully.

Example Input/Output 1:
Input:
Mutton
2
2200
Mutton
2
1900

Output:
SAME
Mutton 2 2200
Mutton 2 1900

Explanation:
Both items have the same name and the same weight.

Example Input/Output 2:
Input:
mutton
3
2000
MUTTON
2
2000

Output:
SAME
mutton 3 2000
MUTTON 2 2000

Explanation:
Both items have the same name and the same price.

Example Input/Output 3:
Input:
Mutton
2
1800
Mutton
1
1000

Output:
NOT SAME
Mutton 2 1800
Mutton 1 1000

Example Input/Output 4:
Input:
Mutton
2
2200
Fish
2
1900

Output:
NOT SAME
Mutton 2 2200
Fish 2 1900
*/

import java.util.*;
class Item {
    String name;
    int weight, price;
    public Item (String name, int weight, int price) {
        this.name=name;
        this.weight=weight;
        this.price=price;
    }
    public boolean equals(Item obj) {
        if (name.equalsIgnoreCase(obj.name) && (weight==obj.weight || price==obj.price)) {
            return true;
        }
        return false;
    }
    public String toString() {
        return name+" "+weight+" "+price;
    }
}
public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Item item1 = new Item(sc.nextLine().trim(), sc.nextInt(), sc.nextInt());
        sc.nextLine();
        Item item2 = new Item(sc.nextLine().trim(), sc.nextInt(), sc.nextInt());
        System.out.println(item1.equals(item2) ? "SAME" : "NOT SAME");
        System.out.println(item1);
        System.out.println(item2);
    } // End of main() function
} // End of Hello class
