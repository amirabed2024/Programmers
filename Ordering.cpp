#include <iostream>
using namespace std;
int main()
{   int x,y,z;
        cin >> x >> y >> z;
    if (x>y and y>z)
        cout << x <<" "<< y <<" "<< z;
    else if(x>z and z>y)
        cout << x <<" "<< z <<" "<< y;
    else if(y>x and x>z)
        cout << y <<" "<< x <<" "<< z;
    else if(y>z and z>x)
        cout << y <<" "<< z <<" "<< x;
    else if(z>x and x>y)
        cout << z <<" "<< x <<" "<< y;
    else if(z>y and y>x)
        cout << z <<" "<< y <<" "<< x;
    return 0;
}