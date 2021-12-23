/*
The program accepts three integers and three string values as the input. The program prints the sum of the three integers and the three integers in the first two lines. Then
the program prints the concatenation of the three string values and the three string values in the next two lines as the output. Please fill in the missing lines of code to
define the class Triplet so that the program runs successfully.

Example Input/Output 1:
Input:
10 20 30
one two three

Output:
60
10 20 30
onetwothree
one two three

Example Input/Output 2:
Input:
45 99 10
bread and jam

Output:
154
45 99 10
breadandjam
bread and jam
*/
#include <iostream>
using namespace std;

template <typename T>
class Triplet
{
    private:
        T a,b,c;
    public:
    Triplet(T a,T b,T c)
    {
        this->a=a;
        this->b=b;
        this->c=c;
    }
    T add()
    {
        return a+b+c;
    }
    void display()
    {
        cout << a << " " << b << " " << c << endl;;
    }
};

int main()
{
    int num1, num2, num3;
    cin >> num1 >> num2 >> num3;
    Triplet<int> intTriplet = Triplet<int>(num1, num2, num3);
    cout << intTriplet.add() << endl;
    intTriplet.display();

    string str1, str2, str3;
    cin >> str1 >> str2 >> str3;
    Triplet<string> stringTriplet = Triplet<string>(str1, str2, str3);
    cout << stringTriplet.add() << endl;
    stringTriplet.display();
    return 0;
}
