package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
)

func main() {
	nums1, nums2, err := parse("input.txt")
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	fmt.Println("Part 1:", part1(nums1, nums2))
	fmt.Println("Part 2:", part2(nums1, nums2))
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func parse(path string) ([]int, []int, error) {
	f, err := os.Open(path)
	if err != nil {
		return nil, nil, err
	}
	defer f.Close()

	var nums1, nums2 []int
	s := bufio.NewScanner(f)
	for s.Scan() {
		var a, b int
		if _, err := fmt.Sscanf(s.Text(), "%d %d", &a, &b); err == nil {
			nums1 = append(nums1, a)
			nums2 = append(nums2, b)
		}
	}
	if err := s.Err(); err != nil {
		return nil, nil, err
	}
	slices.Sort(nums1)
	slices.Sort(nums2)
	return nums1, nums2, nil
}

func part1(nums1 []int, nums2 []int) int {
	var sum int
	for i, v := range nums1 {
		sum += abs(v - nums2[i])
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
