// Euler's Totient Function
#include <bits/stdc++.h>
using namespace std;
#define int long long int

int ETFnumber(int n)
{
	int ans = 1;
	for (int i = 2; i < n; i++){
		if (__gcd(i, n) == 1){
			ans++;
		}
	}
	return ans;
}

int32_t main()
{
	int n;
	cin>>n;
	cout<<ETFnumber(n);
	return 0;
}