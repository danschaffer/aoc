package main

import "testing"

func TestPart1Sample(t *testing.T) {
	lines, err := parse("sample.txt")
	if err != nil {
		t.Skip("sample.txt not present")
	}
	got := part1(lines)
	want := 2
	if want != 0 && got != want {
		t.Errorf("part1(sample) = %d, want %d", got, want)
	}
}

func TestPart2Sample(t *testing.T) {
	lines, err := parse("sample.txt")
	if err != nil {
		t.Skip("sample.txt not present")
	}
	got := part2(lines)
	want := 4
	if want != 0 && got != want {
		t.Errorf("part2(sample) = %d, want %d", got, want)
	}
}
