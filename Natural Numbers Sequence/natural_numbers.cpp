#include <iostream>
using namespace std;
int main()
{
    int start, end;
    cout << "Enter your starting number  : " << endl;
    cin >> start;
    cout << "Enter your end number  : " << endl;
    cin >> end;
    if (start <= 0 || end <= 0)
        cout << "A Natural Number can't be negative, fractional or equal to zero.." << endl;
    else if (end < start)
        cout << "End Number should be larger than starting number" << endl;
    else
    {
        for (int i = start; i <= end; i++)
        {
            cout << i << " ";
        }
    }
}
