package main

import(
"bufio"
"fmt"
"os"
"strconv"
"strings"
)

func main(){
 reader := bufio.NewReader(os.Stdin)

 line1, _ := reader.ReadString('\n')
 parts := strings.Fields(line1)
 target, _ := strconv.Atoi(parts[1])

line2, _ := reader.ReadString('\n')
candi := strings.Fields(line2)

for _, v := range(candi){
    v, _ := strconv.Atoi(v)
	if v < target{
		fmt.Printf("%d ", v)
	}
}

}
