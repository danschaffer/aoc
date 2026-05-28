package main

import "testing"

func TestPart1Sample(t *testing.T) {
	contents := parse("sample1.txt")
	got := solve(contents, Part1)
	want := 161
	if got != want {
		t.Errorf("part1(sample) = %d, want %d", got, want)
	}
}

func TestPart2Sample(t *testing.T) {
	contents := parse("sample2.txt")
	got := solve(contents, Part2)
	want := 48
	if got != want {
		t.Errorf("part2(sample) = %d, want %d", got, want)
	}
}
