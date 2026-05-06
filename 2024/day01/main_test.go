package main

import "testing"

func TestPart1Sample(t *testing.T) {
	lines, err := readLines("sample.txt")
	if err != nil {
		t.Skip("sample.txt not present")
	}
	nums1, nums2 := parse(lines)
	got := part1(nums1, nums2)
	want := 11
	if got != want {
		t.Errorf("part1(sample) = %d, want %d", got, want)
	}
}

func TestPart2Sample(t *testing.T) {
	lines, err := readLines("sample.txt")
	if err != nil {
		t.Skip("sample.txt not present")
	}
	nums1, nums2 := parse(lines)
	got := part2(nums1, nums2)
	want := 31
	if got != want {
		t.Errorf("part2(sample) = %d, want %d", got, want)
	}
}
