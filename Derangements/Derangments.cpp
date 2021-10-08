#include <iostream>
#include <stdio.h>

using std::cout;
using std::endl;
using std:: cin;

int derangements(int n ){
    if (n == 0){
        return 1;
    }else if(n== 1){
        return 0;
    }else{
        return (n-1)*(derangements(n-1)+derangements(n-2));
    }
}

int main(){
    int n;
    int out; 
    cout << "input number: ";
    cin >> n;
    out=derangements(n);
    printf("the %ith number is:\n", n);
    printf("%i \n ", out);

}