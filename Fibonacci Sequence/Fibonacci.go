package main

import "fmt"

// Find the nth number of Fibonacci sequence
// Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
func findNthFibonacciNumber(n int) int64 {
	if n == 0 || n == 1 {
		return int64(n)
	}
	var firstPrv int64 = 0
	var secondPrv int64 = 1

	for i := 2; i <= n; i++ {
		var tmp int64 = firstPrv + secondPrv
		firstPrv = secondPrv
		secondPrv = tmp
	}
	return secondPrv
}

func main() {
	var idxTarget int

	fmt.Printf("Enter the required index of Fibonacci sequence: ")
	fmt.Scanf("%d", &idxTarget)

	fmt.Printf("The %dth element of Fibonacci sequence is %d\n", idxTarget, findNthFibonacciNumber(idxTarget))
}
