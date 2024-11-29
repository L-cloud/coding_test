package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	str1, _ := reader.ReadString('\n')
	str2, _ := reader.ReadString('\n')
	str1 = strings.TrimSuffix(str1, "\n")
	str2 = strings.TrimSuffix(str2, "\n")
	p := lps(str2)
	idx := 0
	positions := make([]int, 0)
	i := 0
	for i < len(str1) {
		if str1[i] == str2[idx] {
			if idx == len(str2)-1 {
				positions = append(positions, i-idx+1)
				idx = p[idx]
			} else {
				idx++
			}
			i++
		} else {
			if idx > 0 {
				idx = p[idx-1]
			} else {
				i++
			}

		}
	}

	fmt.Println(len(positions))
	for _, pos := range positions {
		fmt.Print(pos, " ")
	}
}

func lps(s string) []int {
	p := make([]int, len(s))
	length := 0
	i := 1
	for i < len(s) {
		if s[i] == s[length] {
			length++
			p[i] = length
			i++
		} else {
			if length > 0 {
				/* 현재 지금 length까지는 같아.
				지금까지 같은 접두사 접미사 중 하나 더 짧은 것이 혹시 있어?
				== length - 1 어짜피 지금의 앞,뒤 패턴은 같아.
				ex abaeabad 에서 aba < 전미, 접두사임. abc에 반복되는 패턴이 있는지 확인
				그런데 이것을 우리는 이미 aba를 하면서 확인을 했음! 그래서 aba에서 a는 1인거임! 그럼 뒤에 b가 나온다면 걔는 길이가 2가 됨!
				(e와 d를 비교하는 과정)
				그럼 이 패턴 중에 반복되는 부분이 있어?
				*/
				// length를 조정한 후 재검사
				length = p[length-1]
			} else {
				i++
			}

		}
	}
	return p
}

