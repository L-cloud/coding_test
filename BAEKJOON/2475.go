package main

import "fmt"

func main() {
	var a, b, c, d, e int
	n, err := fmt.Scan(&a, &b, &c, &d, &e)
	if err != nil {
		fmt.Println(n)
	}
	fmt.Println((a*a + b*b + c*c + d*d + e*e) % 10)
}

