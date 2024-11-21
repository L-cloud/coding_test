package main

import (
	"fmt"
	"math"
)

var (
	min_value = 1000000000.0
)

func main() {
	yumi := [2]int{}
	x := [2]int{}
	y := [2]int{}
	z := [2]int{}
	fmt.Scanf("%d %d", &yumi[0], &yumi[1])
	fmt.Scanf("%d %d", &x[0], &x[1])
	fmt.Scanf("%d %d", &y[0], &y[1])
	fmt.Scanf("%d %d", &z[0], &z[1])
	m := make(map[[2]int]int)
	v := make(map[[2]int]int)
	m[yumi], v[yumi] = 1, 1
	m[x], v[x] = 1, 1
	m[y], v[y] = 1, 1
	m[z], v[z] = 1, 1

	find(m, v, yumi, 0)
	fmt.Println(int(min_value))

}

func distance(x [2]int, y [2]int) float64 {
	return math.Sqrt(float64(x[0]-y[0])*float64(x[0]-y[0]) + float64(x[1]-y[1])*float64(x[1]-y[1]))
}

func check(v map[[2]int]int) bool {
	for _, v := range v {
		if v != 0 {
			return false
		}
	}
	return true
}

func find(m map[[2]int]int, v map[[2]int]int, c [2]int, d float64) {
	if check(v) {
		min_value = min(min_value, d)
		return
	}
	for k, _ := range m {
		if v[k] > 0 {
			v[k] -= 1
			find(m, v, k, d+distance(c, k))
			v[k] += 1
		}

	}
}

