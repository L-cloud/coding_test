package main

import (
"fmt"
"strconv"
)

func main() {
	var a int
	var b int
	var c int
	var arr [10]int
	fmt.Scan(&a, &b, &c)
	d := a*b*c
	s := strconv.Itoa(d)
	for _, i := range s{
		a, _ = strconv.Atoi(string(i))
		arr[a]++
	}
	for _, v := range arr{
		fmt.Println(v)
	}
}
