package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

var re = regexp.MustCompile(`mul\((\d+),(\d+)\)|do\(\)|don't\(\)`)

type Part int

const (
	Part1 Part = iota + 1
	Part2
)

func main() {
	contents := parse("input.txt")
	fmt.Println("Part 1:", solve(contents, Part1))
	fmt.Println("Part 2:", solve(contents, Part2))
}

func solve(contents string, part Part) int {
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
			if part == Part1 || enable {
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
