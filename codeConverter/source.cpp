#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int v;

class MyClass
{
public:
    int id = 20;
    int miau;

    void printId()
    {
        cout << this->id;
    }

private:
    int x;
    float dot(int a, int b)
    {
        cout << a;
    }

protected:
    void s(int k)
    {
        cout << "FLA";
        this->dot(this->x, this->x);
    }
};

float check(int x, int y)
{
    if(x > y)
    {
        return true;
    }
return false;
}

class yourClass
{
public:
    int ba;
    float ma(int l, int p)
    {
        cout << "fiat";
    }
};

int main()
{
    cout << "Hello world!" << "this is a" << " " << endl;
    cout << "test";
    int x = 0;
    if(x == 0)
    {
        if(x == 1)
        {
            if(x == 2)
            {
                x = 3;
                x = 4;
            }
            else
            {
                x = 4;
            }

        }
        else
        {
            cout << "mate";
        }
    }
    else
    {
        cout << "1";
    }

    for(int i=0; i <10; i+=3)
    {
        long y = 0;
        cout << i << " ";
    }

    int i = 0;
    while(i < 10)
    {
        i++;
    }

    cout << check(10, 20);

    switch(x)
    {
        case 1: cout <<"1"; break;
        case 2: cout << "2"; break;
    }

    yourClass obj1();
    MyClass obj2();

}
