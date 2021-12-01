/*
N persons visit a palace. The name, gender(M-Male or F-Female) and age of the N persons are passed as the input. The program must find the number of males and number of females
visited the palace in each age. For each age (ascending order), the program must print the age, the number of males, the number of females and the names of the persons. In each
age group, the names of the persons must be printed in the order of their occurrence.

Your task is to define the class Palace so that the program runs successfully.

Example Input/Output 1:
Input:
7
Hector M 25
Arun M 25
Lavanya F 25
Oliver M 22
Catherine F 24
Jhanvi F 23
Kavin M 23

Output:
22 1 0
Oliver
23 1 1
Jhanvi Kavin
24 0 1
Catherine
25 2 1
Hector Arun Lavanya

Explanation:
Here N = 7.
Age 22: 1 male 0 females (Oliver).
Age 23: 1 male 1 female (Jhanvi, Kavin).
Age 24: 0 males 1 female (Catherine).
Age 25: 2 males 1 female (Hector, Arun, Lavanya).

Example Input/Output 2:
Input:
13
Arun M 45
Babloo M 37
Rachel F 45
John M 45
Deepa F 37
Gavin M 25
Nancy F 45
Pavithra F 45
Mambo M 45
Anitha F 50
Helen F 37
Pravin M 45
Bhuvana F 45

Output:
25 1 0
Gavin
37 1 2
Babloo Deepa Helen
45 4 4
Arun Rachel John Nancy Pavithra Mambo Pravin Bhuvana
50 0 1
Anitha
*/
import java.util.*;
class Details {
    int m=0,f=0;
    ArrayList<String> names=new ArrayList<String>();
    public Details(char gender, String name) {
        if (gender=='M')
            m+=1;
        else
            f+=1;
        names.add(name);
    }
    public void update(char gender,String name) {
        if (gender=='M')
            m+=1;
        else
            f+=1;
        names.add(name);
    }
}
class Palace {
    SortedMap<Integer, Details> tm = new TreeMap<>();
    public void visit(String name, char gender, int age) {
        if (tm.containsKey(age))
            tm.get(age).update(gender,name);
        else
            tm.put(age,new Details(gender,name));
    }
    public void printVisitStatus() {
        for(Map.Entry<Integer,Details> entry: tm.entrySet()) {
            Details obj=entry.getValue();
            System.out.println(entry.getKey()+" "+obj.m+" "+obj.f);
            for(String name:obj.names) {
                System.out.print(name+" ");
            }
            System.out.println();
        }
    }
}
public class Hello {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine().trim());
        Palace palace = new Palace();
        for (int ctr = 1; ctr <= N; ctr++) {
            String currPerson[] = sc.nextLine().trim().split("\\s+");
            palace.visit(currPerson[0], currPerson[1].charAt(0), Integer.parseInt(currPerson[2]));
        }
        palace.printVisitStatus();
    }
}
