/*
Please fill in the missing lines of code to define the classes Animal, Dog and Duck so that the program prints the output as given below.

Program's Output:
Dog
Bark
Duck
Quack
*/
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
