import "fmt"
func solution(seoul []string) string {
    for i, v := range seoul{
        if v == "Kim"{
            return fmt.Sprintf("김서방은 %d에 있다", i)
        }
    }
    return ""
}
