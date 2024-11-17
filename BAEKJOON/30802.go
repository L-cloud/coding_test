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

	scanner.Scan()
	nums := make([]int, 6)
	shirt := 0
	for i, num := range strings.Fields(scanner.Text()) {
		nums[i], _ = strconv.Atoi(num)
	}

	scanner.Scan()
	input := strings.Fields(scanner.Text())
	t, _ := strconv.Atoi(input[0])
	p, _ := strconv.Atoi(input[1])

	for _, num := range nums {
		shirt += num / t
		if num%t != 0 {
			shirt++
		}
	}
	fmt.Println(shirt)
	fmt.Println(n/p, n%p)

}

