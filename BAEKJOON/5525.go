package main

import (
    "bufio"
    "fmt"
    "os"
)

func main() {
    var n, m int
    fmt.Scanf("%d", &n)
    fmt.Scanf("%d", &m)

    reader := bufio.NewReader(os.Stdin)
    s, _ := reader.ReadString('\n')
    s = s[:len(s)-1] // 개행 문자 제거

    cnt := 0
    result := 0
    i := 1

    for i < m-1 {
        if s[i-1] == 'I' && s[i] == 'O' && s[i+1] == 'I' {
            cnt++
            if cnt == n {
                result++
                cnt--
            }
            i += 2
        } else {
            cnt = 0
            i++
        }
    }
    fmt.Println(result)
}
