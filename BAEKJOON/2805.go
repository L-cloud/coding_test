package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(reader, &n)
	fmt.Fscan(reader, &k)
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &arr[i])
	}
	sort.Ints(arr)
	left, right := 0, arr[n-1]
	maxV := 0
	for left <= right {
		mid := (right-left)/2 + left
		index := sort.SearchInts(arr, mid)
		t := cal(arr, index, mid)
		if k <= t {
			maxV = mid
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	fmt.Println(maxV)

}

func cal(arr []int, index int, h int) int {
	v := 0
	for _, val := range arr[index:] {
		v += val - h
	}
	return v
}
