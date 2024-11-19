package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	firstLine := strings.Fields(scanner.Text())

	n, _ := strconv.Atoi(firstLine[0])
	k, _ := strconv.Atoi(firstLine[1])

	numbers := make([]int, n)
	for i := 0; i < n; i++ {
		scanner.Scan()
		numbers[i], _ = strconv.Atoi(scanner.Text())
	}
	sort.Ints(numbers)
	left := 1
	right := numbers[n-1]
	for right > left {
		if check(&numbers, left, k) {
			left = (right + left + 1) / 2
			if !check(&numbers, left, k) {
				left, right = 1, left-1
			}
		} else {
			right = (right + left) / 2
		}
	}
	fmt.Println(left)
}

func check(numbers *[]int, value int, k int) bool {
	cnt := 0
	for _, v := range *numbers {
		cnt += v / value
	}
	return cnt >= k
}

