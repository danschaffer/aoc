package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

func main() {
	contents := parse("input.txt")
	fmt.Println("Part 1:", parts(contents, true))
	fmt.Println("Part 2:", parts(contents, false))
}

func parts(contents string, part1 bool) int {
	var re *regexp.Regexp
	if part1 {
		re = regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	} else {
		re = regexp.MustCompile(`mul\((\d+),(\d+)\)|do\(\)|don't\(\)`) 
	}
	matches := re.FindAllStringSubmatch(contents, -1)
	sum := 0
	enable := true
	for _, match := range matches {
		switch {
		case match[0] == "do()":
			enable = true
		case match[0] == "don't()":
			enable = false
		default:
			if enable {
				first, _ := strconv.Atoi(match[1])
				second, _ := strconv.Atoi(match[2])
				sum += first * second
			}
		}
	}
	return sum
}

func parse(path string) string {
	contents, err := os.ReadFile(path)
	if err != nil {
		log.Fatal(err)
	}
	return string(contents)
}
