package main

import (
    "bufio"
    "fmt"
    "os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	a := scanner.Text()
	if a == "1 2 3 4 5 6 7 8"{
		fmt.Println("ascending")
	}else if a == "8 7 6 5 4 3 2 1"{
		fmt.Println("descending")
	}else{
		fmt.Println("mixed")
	}
}
