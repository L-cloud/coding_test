package main

import (
	"fmt"
)

func main() {

	var n int
	fmt.Scanf("%d", &n)

	for i := 0; i < n; i++ {
		var a, b, c int
		fmt.Scanf("%d %d %d", &a, &b, &c)
		floor := 1
		lake := 1
		for c > 1 {
			if floor < a {
				floor++
			} else if floor == a {
				lake++
				floor = 1
			}
			c--
		}
		if lake < 10 {
			fmt.Printf("%d0%d\n", floor, lake)

		} else {
			fmt.Printf("%d%d\n", floor, lake)
		}
	}
}

