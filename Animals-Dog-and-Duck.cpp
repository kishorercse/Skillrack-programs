/*
Please fill in the missing lines of code to define the classes Animal, Dog and Duck so that the program prints the output as given below.

Program's Output:
Dog
Bark
Duck
Quack
*/

#include <iostream>
using namespace std;
class Animal
{
    public:
    virtual void printAnimalName()=0;
    virtual void printAnimalSound()=0;
};

class Dog:public Animal
{
    public:
    void printAnimalName()
    {
        cout << "Dog" << endl;
    }
    void printAnimalSound()
    {
        cout << "Bark" << endl;
    }
};

class Duck:public Animal
{
    public:
    void printAnimalName()
    {
        cout << "Duck" << endl;
    }
    void printAnimalSound()
    {
        cout << "Quack" << endl;
    }
};

int main()
{
    Animal *animal1 = new Dog();
    animal1->printAnimalName();
    animal1->printAnimalSound();
    Animal *animal2 = new Duck();
    animal2->printAnimalName();
    animal2->printAnimalSound();
    return 0;
} // End of main function
