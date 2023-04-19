package main

import (
	"fmt"
	"math/rand"
	"time"

	"github.com/schollz/progressbar/v3"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	var (
		secretNumber = rand.Intn(100) + 1
		guess        int
		maxGuesses   = 10
		guessCount   = 0
	)

	bar := progressbar.Default(int64(maxGuesses), "Guesses remaining")

	for {
		fmt.Println("Guess a number between 1 and 100")
		fmt.Scan(&guess)
		guessCount++
		_ = bar.Add(1)

		if guessCount == maxGuesses {
			fmt.Printf("You've reached the maximum number of guesses. The secret number was %d. Better luck next time!\n", secretNumber)
			break
		}

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
