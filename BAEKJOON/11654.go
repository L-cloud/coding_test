package main

import ("fmt")

func main() {
	var i string
	fmt.Scan(&i)
	for _, c := range(i){
		fmt.Println(c)
	}
}
