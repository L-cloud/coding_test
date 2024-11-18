package main

import (
	"fmt"
	"strconv"
)

func main() {
	var input1, input2, input3 string

	fmt.Scan(&input1)
	fmt.Scan(&input2)
	fmt.Scan(&input3)

	// 숫자로 변환 시도
	if check(input1) {
		print_(input1, 3)
		return
	}
	if check(input2) {
		print_(input2, 2)
		return
	}
	if check(input3) {
		print_(input3, 1)
		return
	}
}

func check(input string) bool {
	_, err := strconv.Atoi(input)
	if err == nil {
		return true
	}
	return false
}

func print_(input string, n int) {
	num, _ := strconv.Atoi(input)
	num += n
	if num%3 == 0 && num%5 == 0 {
		fmt.Println("FizzBuzz")
	} else if num%3 == 0 {
		fmt.Println("Fizz")
	} else if num%5 == 0 {
		fmt.Println("Buzz")
	} else {
		fmt.Println(num)
	}
}

