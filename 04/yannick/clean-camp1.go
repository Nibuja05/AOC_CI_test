package main

import (
    "fmt"
    "bufio"
    "os"
    "log"
    "regexp"
    "strconv"
)

func main() {
    f, err := os.Open("input_day4")
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()

    scanner := bufio.NewScanner(f)
    re := regexp.MustCompile("[0-9]+")
    score := 0
    var actual_number_list [4]int


    for scanner.Scan() {
        line := scanner.Text()
        number_list := re.FindAllString(line, -1)
        for i := 0; i < len(number_list); i++ {
            num, err := strconv.Atoi(number_list[i])
            if err != nil {
                log.Fatal(err)
            }
            actual_number_list[i] = num
        }
        if (actual_number_list[2] >= actual_number_list[0] && actual_number_list[3] <= actual_number_list[1]) {
            score += 1
            continue
        } else if actual_number_list[2] <= actual_number_list[0] && actual_number_list[3] >= actual_number_list[1] {
                score += 1
            
        }

    }
    fmt.Println(score)
}
