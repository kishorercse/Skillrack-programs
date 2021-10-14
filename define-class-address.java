/*
The program accepts an integer X as the input. If the value of X is a nonzero value, then the address(door number, street name, city name, state name and pincode) of person 
is passed as the input. Else the default address must be as given below.
Door Number: 100 
Street Name: ABC 
Street City Name: XYZ City 
State Name: MNO State 
Pincode: 666666 
Finally, the program prints the address(door number, street name, city name, state name and pincode) of the person. 
Your task is to define the class Address so that the program runs successfully.

Example Input/Output 1: 
Input:
1
241
Jacob Road 
Jaipur 
Rajasthan 
302001 

Output:
241
Jacob Road 
Jaipur 
Rajasthan 
302001 

Example Input/Output 2: 
Input:
0

Output: 
100 
ABC 
Street 
XYZ 
City 
MNO State 
666666

Explanation: 
Here X = 0, so the default address is printed as the output.
*/
import java.util.*;

class Address {
    private int doorNumber=100, pincode=666666;
    private String streetName="ABC Street", city="XYZ City", state="MNO State";
    public void setDoorNumber(int n){
        doorNumber=n;
    }
    public void setStreetName(String s){
        streetName=s;
    }
    public void setCity(String s){
        city=s;
    }
    public void setState(String s){
        state=s;
    }
    public void setPincode(int n){
        pincode=n;
    }
    public int getDoorNumber(){
        return doorNumber;
    }
    public String getStreetName(){
        return streetName;
    }
    public String getCity(){
        return city;
    }
    public String getState(){
        return state;
    }
    public int getPincode(){
        return pincode;
    }
}

public class Hello { 
  public static void main(String args[]) { 
    Scanner sc = new Scanner(System.in);
    Address addr = new Address();
    int X = sc.nextInt(); 
    if (X != 0) { 
      addr.setDoorNumber(sc.nextInt()); 
      sc.nextLine();
      addr.setStreetName(sc.nextLine()); 
      addr.setCity(sc.nextLine());
      addr.setState(sc.nextLine());
      addr.setPincode(sc.nextInt());
    } 
    System.out.println(addr.getDoorNumber()); 
    System.out.println(addr.getStreetName());
    System.out.println(addr.getCity()); 
    System.out.println(addr.getState());
    System.out.println(addr.getPincode());
  }
}
