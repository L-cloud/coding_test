package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())
	current := -1
	stack := [10000]int{}

	for i := 0; i < n; i++ {
		scanner.Scan()
		command := strings.Split(scanner.Text(), " ")

		switch command[0] {
		case "push":
			num, _ := strconv.Atoi(command[1])
			current++
			stack[current] = num
		case "pop":
			if current > -1 {
				fmt.Println(stack[current])
				current--
			} else {
				fmt.Println(-1)
			}
		case "top":
			if current > -1 {
				fmt.Println(stack[current])
			} else {
				fmt.Println(-1)
			}
		case "size":
			fmt.Println(current + 1)
		case "empty":
			if current > -1 {
				fmt.Println(0)
			} else {
				fmt.Println(1)
			}
		}
	}
}

