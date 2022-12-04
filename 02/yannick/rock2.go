package main


// Rock paper scissors tournament strategy guide task for advent of code
// A - Rock | B - Paper | C - Scissors ---- Enemy Input
// X - lose | Y - draw | Z - win ---- Player Response

// total score == sum of scores for each round
// score: 1 for rock, 2 for paper, 3 for scissors + the score
// for the outcome of the round: loss - 0, draw - 3, win - 6


import (
    "fmt"
    "log"
    "bufio"
    "os"
) 

func main() {
    // open the input file
    f, err := os.Open("input")

    if err != nil {
        log.Fatal(err)
    }

    defer f.Close()

    scanner := bufio.NewScanner(f)
    var total_score = 0
    // read the input file line by line
    // for each line: 
    //      - get both letters
    //      - get score for second letter
    //      - compare letters and get score for result
    //      - add score iteratively

    for scanner.Scan() {
        round := scanner.Text()
        switch {
            case round == "A X":
                total_score += (3 + 0)
            case round == "A Y":
                total_score += (1 + 3)
            case round == "A Z":
                total_score += (2 + 6)
            case round == "B X":
                total_score += (1 + 0)
            case round == "B Y":
                total_score += (2 + 3)
            case round == "B Z":
                total_score += (3 + 6)
            case round == "C X":
                total_score += (2 + 0)
            case round == "C Y":
                total_score += (3 + 3)
            case round == "C Z":
                total_score += (1 + 6)
        }
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

    fmt.Println(total_score)
}
