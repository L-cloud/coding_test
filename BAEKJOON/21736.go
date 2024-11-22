package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n, m int
	fmt.Scanf("%d %d", &n, &m)

	chat := make([][]byte, n)
	scanner := bufio.NewScanner(os.Stdin)

	for i := 0; i < n; i++ {
		scanner.Scan()
		chat[i] = []byte(scanner.Text())
	}
	v := make([][]int, len(chat))
	for i := range v {
		v[i] = make([]int, len(chat[0]))
	}

	c := [2]int{0, 0}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if chat[i][j] == 'I' {
				c[0], c[1] = i, j
			}
		}
	}
	cnt := 0
	x := [4]int{1, 0, -1, 0}
	y := [4]int{0, 1, 0, -1}
	stack := [][2]int{}
	stack = append(stack, c)
	for len(stack) > 0 {
		c := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if chat[c[0]][c[1]] == 'P' {
			cnt++
		}
		for i := 0; i < 4; i++ {
			x_ := c[0] + x[i]
			y_ := c[1] + y[i]
			if x_ > -1 && y_ > -1 && x_ < n && y_ < m && chat[x_][y_] != 'X' && v[x_][y_] != 1 {
				stack = append(stack, [2]int{x_, y_})
				v[x_][y_] = 1
			}
		}
	}
	if cnt > 0 {
		fmt.Println(cnt)
	} else {
		fmt.Println("TT")
	}

}

