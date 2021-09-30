/*Tribonacci Sequence optimized with Dynamic Programming approach
and memorization
0-indexed
*/

function tribonacci(n,memo={}){
    if(n<=3){
        if(n<=1)
            memo[n]=0;
        else
            memo[n]=1;
        return memo[n];
    }
    if(n in memo)
        return memo[n];
    var trib=tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3);
    memo[n]=trib;
    return trib;
}

console.log(tribonacci(8));