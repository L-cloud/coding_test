package main

import (
	"fmt"
	"strconv"
)

func main() {
	var a int
	var b int
	fmt.Scan(&a, &b)

	var bStr string = strconv.Itoa(b)
	for i := len(bStr) - 1; i >= 0; i-- {
		fmt.Println(a * int(bStr[i]-'0'))
	}

	fmt.Println(a * b)

}

