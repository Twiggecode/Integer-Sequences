// C++ program to check if the number
// is semi-perfect or not
#include <bits/stdc++.h>
using namespace std;

// code to find all the factors of
// the number excluding the number itself
vector<int> factors(int n)
{
	// vector to store the factors
	vector<int> v;
	v.push_back(1);

	// note that this loop runs till sqrt(n)
	for (int i = 2; i <= sqrt(n); i++) {

		// if the value of i is a factor
		if (n % i == 0) {
			v.push_back(i);

			// condition to check the
			// divisor is not the number itself
			if (n / i != i) {
				v.push_back(n / i);
			}
		}
	}
	// return the vector
	return v;
}

// Function to check if the
// number is semi-perfect or not
bool check(int n)
{
	vector<int> v;

	// find the divisors
	v = factors(n);

	// sorting the vector
	sort(v.begin(), v.end());

	int r = v.size();

	// subset to check if no is semiperfect
	bool subset[r + 1][n + 1];

	// initialising 1st column to true
	for (int i = 0; i <= r; i++)
		subset[i][0] = true;

	// initializing 1st row except zero position to 0
	for (int i = 1; i <= n; i++)
		subset[0][i] = false;

	// loop to find whether the number is semiperfect
	for (int i = 1; i <= r; i++) {
		for (int j = 1; j <= n; j++) {

			// calculation to check if the
			// number can be made by summation of divisors
			if (j < v[i - 1])
				subset[i][j] = subset[i - 1][j];
			else {
				subset[i][j] = subset[i - 1][j] ||
							subset[i - 1][j - v[i - 1]];
			}
		}
	}

	// if not possible to make the
	// number by any combination of divisors
	if ((subset[r][n]) == 0)
		return false;
	else
		return true;
}

// driver code to check if possible
int main()
{
	int n;
	cin >> n;
	for(int i =0 ; i <n ; i++){
	    if (check(i))
	        cout << i << " ";
	}
	return 0;
	
}

