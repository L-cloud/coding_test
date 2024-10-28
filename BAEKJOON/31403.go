package main
import (
"bufio"
"fmt"
"os"
"strconv"
)

func main(){
scanner := bufio.NewScanner(os.Stdin)
scanner.Scan()
i := scanner.Text()
scanner.Scan()
j := scanner.Text()
scanner.Scan()
k := scanner.Text()
Int_i, _ := strconv.Atoi(i)
Int_j, _ := strconv.Atoi(j)
Int_k, _ := strconv.Atoi(k)
Int_ij, _ := strconv.Atoi(i+j)
fmt.Println(Int_i + Int_j - Int_k)
fmt.Println(Int_ij - Int_k)

}
