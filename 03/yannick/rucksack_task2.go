package main

import (
    "fmt"
    "bufio"
    "strings"
    "os"
    "log"
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

    var groups []string
    
    for scanner.Scan() {
        groups = append(groups, scanner.Text())
        if len(groups) == 3 {
            for i := 0; i < len(groups[0]); i++ {
                if strings.Contains(groups[1], string(groups[0][i])) && strings.Contains(groups[2], string(groups[0][i])) {
                    score += strings.Index(letters, string(groups[0][i])) + 1
                    break
                }
            }
            groups = nil
        }
    }
    fmt.Println(score)

}


