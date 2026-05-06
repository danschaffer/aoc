package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
)

func main() {
	lines, err := readLines("input.txt")
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	nums1, nums2 := parse(lines)
	fmt.Println("Part 1:", part1(nums1, nums2))
	fmt.Println("Part 2:", part2(nums1, nums2))
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func parse(lines []string) ([]int, []int) {
	var nums1, nums2 []int
	for _, line := range lines {
		var a, b int
		if _, err := fmt.Sscanf(line, "%d %d", &a, &b); err != nil {
			continue
		}
		nums1 = append(nums1, a)
		nums2 = append(nums2, b)
	}
	slices.Sort(nums1)
	slices.Sort(nums2)
	return nums1, nums2
}

func part1(nums1 []int, nums2 []int) int {
	var sum int
	for i := 0; i < len(nums1); i++ {
		sum += abs(nums1[i] - nums2[i])
	}
	return sum
}

func part2(nums1 []int, nums2 []int) int {
	freq := make(map[int]int)
	for _, v := range nums2 {
		freq[v]++
	}
	var sum int
	for _, v := range nums1 {
		sum += v * freq[v]
	}
	return sum
}

func readLines(path string) ([]string, error) {
	f, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer func() { _ = f.Close() }()

	var lines []string
	s := bufio.NewScanner(f)
	s.Buffer(make([]byte, 0, 1024*1024), 1024*1024)
	for s.Scan() {
		lines = append(lines, s.Text())
	}
	return lines, s.Err()
}
