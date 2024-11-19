package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)

	arr := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &arr[i])
	}

	maxLen := 0
	left := 0
	count := make(map[int]int)

	for right := 0; right < n; right++ {
		count[arr[right]]++

		for len(count) > 2 {
			count[arr[left]]--
			if count[arr[left]] == 0 {
				delete(count, arr[left])
			}
			left++
		}

		if right-left+1 > maxLen {
			maxLen = right - left + 1
		}
	}

	fmt.Println(maxLen)
}

