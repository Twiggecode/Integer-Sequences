#include<iostream>
using namespace std;

// Define the number of digits the output factorial can contain
#define HUGE 10000 

// High school multiplication - storing output as individual digits in an array
// Multiplying each digit with individually and adjusting carry overs
int mult(int x, int answer[], int output_digits)
{
    int carry = 0;  
 
    for (int i=0; i<output_digits; i++)
    {
        int prod = answer[i] * x + carry;
        answer[i] = prod % 10; 
        carry  = prod/10;   
    }
 
    while (carry)
    {
        answer[output_digits] = carry%10;
        carry = carry/10;
        output_digits++;
    }
    return output_digits;
}
// Factorial function
void factorial(int n)
{
    int answer[HUGE];
    answer[0] = 1;
    int output_digits = 1;

    for (int x=2; x<=n; x++)
        output_digits = mult(x, answer, output_digits);
 
    cout << "Factorial of the given number is: \n";
    for (int i=output_digits-1; i>=0; i--)
        cout << answer[i];
}
// Main Driver
int main()
{
    int n;
    cout<<"Enter a number: ";
    cin>>n;
    factorial(n);
    return 0;
}