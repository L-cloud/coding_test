package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
	
	scanner.Scan()
	var n int
	_, _ = fmt.Sscanf(scanner.Text(), "%d", &n)

	x := make([]int, n)
	y := make([]int, n)
	
	for i := 0; i < n; i++ {
		scanner.Scan()
		_, _ = fmt.Sscanf(scanner.Text(), "%d", &x[i])
		scanner.Scan()
		_, _ = fmt.Sscanf(scanner.Text(), "%d", &y[i])
	}

	sort.Ints(x)
	sort.Ints(y)

	c := 0
	for i := 0; i < n; i++ {
		c += abs(x[i] - x[n/2])
		c += abs(y[i] - y[n/2])
	}
	fmt.Println(c)
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
