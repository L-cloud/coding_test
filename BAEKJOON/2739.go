package main

import (
	"fmt"
)

func main() {
	var n int
	_, err := fmt.Scan(&n)
	if err != nil {
		return
	}

	for i := 1; i <= 9; i++ {
		fmt.Printf("%d * %d = %d\n", n, i, n*i)
	}
}

