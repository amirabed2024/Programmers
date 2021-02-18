#include <iostream>
using namespace std;
int main()
{
    int x,y;
    cin >> x>> y; 
    if (x>y){
        cout << x << "is larger";
    }else
    if (y>x){
        cout << y << "is larger";
    }else 
    if (x==y){
        cout << "are equal";
    } 
    return 0;
}