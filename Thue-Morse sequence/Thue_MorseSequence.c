#ifndef _GNU_SOURCE
    #define _GNU_SOURCE 1
#endif

#include<stdio.h>
#include <string.h>

const char* complement(const char* term) {
    char* appendString = NULL;
    for (int i = 0; i < strlen(term); i++) { // iterate each digit of the term and compute the complement digit 
        char* appendDigit;
        
        appendDigit = term[i] == 48 ? "1" : "0"; // 48 is ascii code for "0"

        if (appendString == NULL) { // First time appendString is NULL so initialize it with the first complement digit
            appendString = appendDigit;
        } else {
            asprintf(&appendString, "%s%s",appendString, appendDigit); // concat strings
        }
    }

    return appendString;
}

const char* calculateSequence(int num) {
    if (num <= 1) {
        return "0";
    }
    char* initTerm = "0";
    for (int i = 1; i < num; i++) { // iterate through terms
        asprintf(&initTerm, "%s%s",initTerm, complement(initTerm)); // concat strings
    }
    return initTerm;
}

    
void main()  
{  
  int num;  
  printf("Enter a number: ");
  scanf("%d", &num);
  printf("%dth term of Thue Morse sequence is: \n", num);
  printf("%s\n",calculateSequence(num));
}  
