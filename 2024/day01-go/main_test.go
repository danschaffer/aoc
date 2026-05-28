package main

import (
	"testing"
)

func TestPart1Sample(t *testing.T) {
	nums1, nums2, err := parse("sample.txt")
	if err != nil {
		t.Fatalf("part1(sample) = %s", err)
	}
	got := part1(nums1, nums2)
	want := 11
	if got != want {
		t.Errorf("part1(sample) = %d, want %d", got, want)
	}
}

func TestPart2Sample(t *testing.T) {
	nums1, nums2, err := parse("sample.txt")
	if err != nil {
		t.Fatalf("part2(sample) = %s", err)
	}
	got := part2(nums1, nums2)
	want := 31
	if got != want {
		t.Errorf("part2(sample) = %d, want %d", got, want)
	}
}
