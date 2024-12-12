import "strings"
func solution(phone_number string) string {
    return strings.Repeat("*", len(phone_number) -4 ) + phone_number[len(phone_number) -4:]
}
