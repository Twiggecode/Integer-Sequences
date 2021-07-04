package main

import (
	"fmt"
)

func user_input() int {
	var n int
	fmt.Print("Enter the value of n: ")
	fmt.Scanf("%d", &n)
	n = n + 1
	return n
}

func tribonacci() int {
	// Initialize the first three sequence values

	a, b, c := 0, 1, 1
	var d int

	n := user_input()

	if (n == 1){
		return 0
	}else if (n == 2 || n == 3){
		return 1
	}else{
		for i := 0; i < (n - 3); i++{
			d = a + b + c
			a = b
			b = c
			c = d
		}
		return d
	}
}

func main() {
	fmt.Println("The Nth term in the sequence is ", tribonacci())
}
