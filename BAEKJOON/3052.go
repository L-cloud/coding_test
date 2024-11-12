package main

import (
	"fmt"
)

func main() {
	numSet := make(map[int]bool)
	for i := 0; i < 10; i++ {
		var n int
		fmt.Scanf("%d", &n)
		numSet[n%42] = true
	}
	fmt.Println(len(numSet))

}

