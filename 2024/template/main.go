package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	lines, err := readLines("input.txt")
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	fmt.Println("Part 1:", part1(lines))
	fmt.Println("Part 2:", part2(lines))
}

func part1(lines []string) int {
	// TODO
	return 0
}

func part2(lines []string) int {
	// TODO
	return 0
}

func readLines(path string) ([]string, error) {
	f, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer f.Close()

	var lines []string
	s := bufio.NewScanner(f)
	s.Buffer(make([]byte, 0, 1024*1024), 1024*1024)
	for s.Scan() {
		lines = append(lines, s.Text())
	}
	return lines, s.Err()
}
