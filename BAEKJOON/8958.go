package main

import (
	"fmt"
)

func main() {
	var n int
	var str string
	fmt.Scanf("%d", &n)
	for n > 0 {
		n--
		fmt.Scan(&str)
		cnt := 0
		prev := 0
		for _, c := range str {
			if c == 'O' {
				prev++
			} else {
				prev = 0
			}
			cnt += prev
		}
		fmt.Println(cnt)
	}
}

