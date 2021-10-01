/*Fibonacci sequence, for nth number, 0-indexed.
Optimized, implemented with dynamic programming technique of
memorization*/

function fibonacci(n,memo={}){
    if(n<=2){
        if(n==0)
            memo[n]=0;
        else
            memo[n]=1;
        return memo[n];
    }
    if(n in memo)
        return memo[n];
    var fib=fibonacci(n-1)+fibonacci(n-2);
    memo[n]=fib;
    return fib;
}

console.log(fibonacci(10));