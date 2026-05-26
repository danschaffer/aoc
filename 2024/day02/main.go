package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	levels, err := parse("input.txt")
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	fmt.Println("Part 1:", part1(levels))
	fmt.Println("Part 2:", part2(levels))
}

func removeAt(nums []int, i int) []int {
	result := make([]int, 0, len(nums)-1)
	result = append(result, nums[:i]...)
	result = append(result, nums[i+1:]...)
	return result
}

func isSafe(level []int) bool {
	unsafe := false
	increase := false
	for i := range level {
		if i == 0 {
			if level[0] < level[1] {
				increase = true
			}
			if level[0] == level[1] {
				unsafe = true
				break
			}
		} else {
			if increase && (level[i]-level[i-1] > 3 || level[i]-level[i-1] < 1) {
				unsafe = true
				break
			} else if !increase && (level[i-1]-level[i] > 3 || level[i-1]-level[i] < 1) {
				unsafe = true
				break
			}
		}
	}
	return !unsafe
}

func part1(lines [][]int) int {
	safe := 0
	for _, level := range lines {
		if isSafe(level) {
			safe += 1
		}
	}
	return safe
}

func part2(lines [][]int) int {
	safe := 0
	for _, level := range lines {
		if isSafe(level) {
			safe += 1
			continue
		}
		for i := range len(level) {
			level0 := removeAt(level, i)
			if isSafe(level0) {
				safe += 1
				break
			}
		}
	}
	return safe
}

func parse(path string) ([][]int, error) {
	f, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer f.Close()

	var result [][]int
	s := bufio.NewScanner(f)
	for s.Scan() {
		fields := strings.Fields(s.Text())
		nums := make([]int, len(fields))
		for i, f := range fields {
			nums[i], _ = strconv.Atoi(f)
		}
		result = append(result, nums)
	}
	return result, nil
}
