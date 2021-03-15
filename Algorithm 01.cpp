// Sum of two numbers
#include <iostream>
using namespace std;
int main()
{
    int A, B;
    cin >> A;
    cin >> B;
    cout << A + B;
    return 0;
}


// Average of Numbers
#include <iostream>
using namespace std;
int main()
{
    int A, B, C;
    float D;
    cin >> A;
    cin >> B;
    cin >> C;
    D = A + B + C;
    D = D / 3;
    cout << D;
    return 0;
} 


// Even, Odd
#include <iostream>
using namespace std;
int main()
{
    int A, B;
    cin >> A;
    B = A % 2;
    if (B == 0)
    {
    cout << "Zoj Ast";
    }
    else
    {
    cout << "Fard Ast";
    }
    return 0;
} 


//  Even numbers less than 20 
#include <iostream>
using namespace std;
int main()
{
    int A, B;
    for (A=1; A<20; A++)
    {
    B = A % 2;
    if (B == 0)
    {
    cout << A;
    }
    }
    return 0;
}