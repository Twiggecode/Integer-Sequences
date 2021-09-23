#include<bits/stdc++.h>

int main()
{
	int n,t;
	std::cout<<"Stella Octangula numbers\nEnter your choice:\n[1]  Print the single term of the series\n[2] Print series till term specified\n";
	std::cin>>n;
	switch(n)
	{
		case 1:	std::cout<<"[+] Enter the Index:\n";
				std::cin>>t;
				std::cout<<"Term at Index "<<t<<" "<<t*(2*(t*t)-1)<<"\n";
		case 2: std::cout<<"[+] Enter the Index:\n";
				std::cin>>t;
				for(int i=0;i<n+1;++i)
				{
					std::cout<<"Term at Index "<<i<<" "<<i*(2*(i*i)-1)<<"\n";
				}
		default:std::cout<<"Enter Valid option\n";

	}
	return 0;
}