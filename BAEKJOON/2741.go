package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var n int
	_, err := fmt.Scan(&n)
	if err != nil {
		return
	}

	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	for i := 1; i <= n; i++ {
		w.WriteString(strconv.Itoa(i) + "\n")
	}
}

