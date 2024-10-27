package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
	"fmt"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')

	input = strings.TrimSpace(input)

	num, err := strconv.Atoi(input)
	if err == nil {
		switch {
		case num >= 90:
			fmt.Println("A")
		case num >= 80:
			fmt.Println("B")
		case num >= 70:
			fmt.Println("C")
		case num >= 60:
			fmt.Println("D")
		default:
			fmt.Println("F")
		}
	}

}
