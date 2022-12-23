#include<bits/stdc++.h>
using namespace std;

// example of Fibonacci sequence ------ 0, 1, 1, 2, 3, 5, 8, 13....
// 1st and 2nd term = 0 , 1 respectively and proceeding terms are sum of previous two terms 

const int N = 1e9 + 7;

// Multiplying the parameter matrices:
vector<vector<int>> multiply (vector <vector <int>> a, vector <vector <int>> b)
{
    vector <vector <int>> r (2, vector <int> (2, 0));
    for (int i = 0; i < 2; ++i)
    {
        for (int j = 0; j < 2; ++j)
        {
            for (int k = 0; k < 2; ++k)
            {
                r[i][j] += a[i][k] * b[k][j];
                r[i][j] %= N;
            }
        }
    }
    
    return r;
}

// Finding T^n:
void matrixExponentiation (vector <vector <int>> &T, int n)
{
    // defining the identity matrix:
    vector <vector <int>> I = {{1, 0},
                               {0, 1}};
    vector <vector <int>> current = T;
    T = I;
    while (n > 0)
    {
        if (n%2 != 0)
        {
            T = multiply (T, current);
        }
        
        n = n/2;
        current = multiply (current, current);
    }
}

int Fibonacci (int n)
{
    // *** for details of matrix exponentiation method visit: ***
    // (1) https://www.youtube.com/watch?v=k43lupRL8jU
    // (2) https://www.youtube.com/watch?v=Y-slDsjyxmY
	
    if (n == 1)	return 0;
    if (n == 2) return 1;
	
    n -= 2;
	
    // computing nth Fibonacci number using matrix exponentiation algorithm:
 
    // Transition matrix:
    vector <vector <int>> T = {{0, 1},
                               {1, 1}};
	
    matrixExponentiation (T, n);
	
    return T[1][1];
}

int main()
{
    int n; // n is the expected user input
    cout << "Enter the required index of Fibonacci sequence : ";
    cin >> n;
    cout << "The Term at required index of Fibonacci sequence is : "; 
    cout << Fibonacci (n);
    return 0;
}
