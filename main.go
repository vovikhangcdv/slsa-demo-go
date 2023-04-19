// Write a simplest game binary for go

package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	var (
		secretNumber = rand.Intn(100)
		guess        int
	)
	for {
		fmt.Println("Guess a number between 1 and 100")
		fmt.Scan(&guess)
		switch {
		case guess > secretNumber:
			fmt.Println("Too high")
		case guess < secretNumber:
			fmt.Println("Too low")
		default:
			fmt.Println("You win!")
			return
		}
	}
}