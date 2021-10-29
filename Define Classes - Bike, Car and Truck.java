/*
Please define the classes Bike, Car and Truck so that the program prints the following as the output. 

Program's Output: 
Bike 
2 
Car 
4 
Truck 
6
*/
import java.util.*; 
interface Vehicle { 
  public String getName();
  public int getNumberOfWheels(); 
}

class Bike implements Vehicle{
    public String getName(){
        return "Bike";
    }
    public int getNumberOfWheels(){
        return 2;
    }
}
class Car implements Vehicle{
    public String getName(){
        return "Car";
    }
    public int getNumberOfWheels(){
        return 4;
    }
}
class Truck implements Vehicle{
    public String getName(){
        return "Truck";
    }
    public int getNumberOfWheels(){
        return 6;
    }
}
public class Hello { 
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    Vehicle bike = new Bike();
    Vehicle car = new Car(); 
    Vehicle truck = new Truck(); 
    System.out.println(bike.getName()); 
    System.out.println(bike.getNumberOfWheels()); 
    System.out.println(car.getName()); 
    System.out.println(car.getNumberOfWheels()); 
    System.out.println(truck.getName()); 
    System.out.println(truck.getNumberOfWheels()); 
  }
}
