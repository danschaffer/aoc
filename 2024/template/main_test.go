package main

import "testing"

func TestPart1Sample(t *testing.T) {
	lines, err := readLines("sample.txt")
	if err != nil {
		t.Skip("sample.txt not present")
	}
	got := part1(lines)
	want := 0 // update once you know the expected answer
	if want != 0 && got != want {
		t.Errorf("part1(sample) = %d, want %d", got, want)
	}
}

func TestPart2Sample(t *testing.T) {
	lines, err := readLines("sample.txt")
	if err != nil {
		t.Skip("sample.txt not present")
	}
	got := part2(lines)
	want := 0
	if want != 0 && got != want {
		t.Errorf("part2(sample) = %d, want %d", got, want)
	}
}
