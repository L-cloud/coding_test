package main
import "fmt"

func main() {
	var a,b int
	fmt.Scan(&a, &b)
	b -= 45
	if b < 0 { 
		a -=1 
		b += 60
		if a < 0 {a = 23}
	}
	fmt.Printf("%d %d", a, b)
	
}
