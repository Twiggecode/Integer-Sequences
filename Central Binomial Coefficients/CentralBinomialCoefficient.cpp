// C++ implementation to find the
// Nth Central Binomial Coefficient

#include<bits/stdc++.h>
using namespace std;

// Function to find the value of
// Nth Central Binomial Coefficient
int binomialCoeff(int n, int k)
{
	int C[n + 1][k + 1];
	int i, j;

	// Calculate value of Binomial
	// Coefficient in bottom up manner
	for (i = 0; i <= n; i++)
	{
		for (j = 0; j <= min(i, k); j++)
		{
			// Base Cases
			if (j == 0 || j == i)
				C[i][j] = 1;

			// Calculate value
			// using previously
			// stored values
			else
				C[i][j] = C[i - 1][j - 1] +
						C[i - 1][j];
		}
	}

	return C[n][k];
}

// Driver Code
int main()
{
	int n;
	cin >>n;
	int k = n;
	n = 2*n;
	cout << binomialCoeff(n, k);
}

