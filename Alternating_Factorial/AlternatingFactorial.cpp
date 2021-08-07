// AlternatingFactorial.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>

using namespace std;

long long factorialOf(int);

int main()
{
    cout << "The program finds the nth element in the Alternating factorial sequence.\n\n";

    string n_s = "";
    int n = 0;

    cout << "\tEnter n (starts from 0): ";
    cin >> n_s;
    
    try {
        n = stoi(n_s);
        if (n < 0) throw 1;
    }
    catch (invalid_argument& e) {
        cerr << "\tNot an integer." << endl;
        return 1;
    }
    catch (int e) {
        cerr << "\tInvalid n, n must be greater or equal to zero." << endl;
        return 1;
    }

    int num = n;
    int turn = 0;
    long long result = factorialOf(n + 1);

    for (int i = 0; i < n; i++) {
        if (turn % 2 == 0) {
            result -= factorialOf(num);
            num--;
            turn++;
        }
        else {
            result += factorialOf(num);
            num--;
            turn++;
        }
    }

    cout << "\tElement " << n + 1 << " in the sequence is: " << result << endl;

    return 0;
}

long long factorialOf(int n) {
    long long factorial = 1;
    for (int i = 1; i <= n; ++i) {
        factorial *= i;
    }
    return factorial;
}