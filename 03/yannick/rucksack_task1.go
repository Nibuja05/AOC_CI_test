package main

import (
    "fmt"
    "bufio"
    "log"
    "os"
    "strings"
)


func main() {
    f, err := os.Open("input_day3")
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()

    scanner := bufio.NewScanner(f)
    letters := "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    score := 0

    for scanner.Scan() {
        line := scanner.Text()
        compartment_size := len(line) / 2
        first_compartment := line[:compartment_size]
        second_compartment := line[compartment_size:]
        for i := 0; i < len(first_compartment); i++ {
            if strings.Contains(second_compartment, string(first_compartment[i])) {
                score += strings.Index(letters, string(first_compartment[i])) + 1
                break
            }
        }
    }
    fmt.Println(score)

}
