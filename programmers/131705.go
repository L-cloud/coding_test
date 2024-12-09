func solution(number []int) int {
    num := 0
    n := len(number)
    for i := 0; i < n-2; i++ {
        for j := i + 1; j < n-1; j++ {
            for k := j + 1; k < n; k++ {
                if number[i]+number[j]+number[k] == 0 {
                    num++
                }
            }
        }
    }
    return num
}
