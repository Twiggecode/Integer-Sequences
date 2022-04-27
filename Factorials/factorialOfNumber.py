def multiplication(x, y):
     
    #auxiliary matrix for multipliccation matrix
    multiplication_matrix = [[0 for l in range(3)]
              for m in range(3)];
    for i in range(3):
        for j in range(3):
            multiplication_matrix[i][j] = 0;
            for k in range(3):
                multiplication_matrix[i][j] += x[i][k] * y[k][j];
 
    for i in range(3):
        for j in range(3):
            x[i][j] = multiplication_matrix[i][j]; # Updating our matrix
    return x;
 
def power(fact, num):
 
    m = [[1, 1, 1], [1, 0, 0], [0, 1, 0]];
    if (num == 1):
        return fact[0][0] + fact[0][1];
    power(fact, int(num / 2));
    fact = multiplication(fact, fact);
    if (num % 2 != 0):
        fact = multiplication(fact, m);
    return fact[0][0] + fact[0][1] ;

def findNthTerm(n):
    factorial = [[1, 1, 1], [1, 0, 0], [0, 1, 0]];
 
    return power(factorial, n - 2);
 
num = input("Enter your value and we will give you factorial of that number: ")
num = int(num)
 
print("factorial of",num,"is:",findNthTerm(num));
 
