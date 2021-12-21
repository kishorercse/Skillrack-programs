/*
Please fill in the missing lines of code to define the classes Fruit and Mango so that the program prints the output as given below.

Program's Output:
Fruit
Mango
Mango
*/
#include <iostream>
using namespace std;

class Fruit
{
    public:
    virtual void printName()
    {
        cout << "Fruit" << endl;
    }
};

class Mango:public Fruit
{
    public:
    void printName()
    {
        cout << "Mango" << endl;
    }
};
int main()
{
    Fruit *fruit1 = new Fruit();
    Fruit *fruit2 = new Mango();
    Mango *mango = new Mango();
    fruit1->printName();
    fruit2->printName();
    mango->printName();
    return 0;
}
