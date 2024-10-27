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

	for scanner.Scan() {
		line := scanner.Text()
		arr := strings.Fields(line)
		a := 0
		for _, i := range arr {
			i, _ := strconv.Atoi(i)
			a += i
		}
		if a == 0{
			break
		}
		fmt.Println(a)
	}
}
