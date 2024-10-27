package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')

	input = strings.TrimSpace(input)

	num, err := strconv.Atoi(input)
	if err == nil {
		if num%4 == 0 && (num%100 != 0 || num%400 == 0) {
			fmt.Println(1)
		} else {
			fmt.Println(0)
		}
	}

}
