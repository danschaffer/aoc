#!/usr/bin/env node
import { readFileSync } from 'fs';

class Day {
  constructor(file) {
    this.data = readFileSync(file, 'utf8')
      .trim()
      .split('\n')
      .map(line => line.trim());
  }

  part1() {
    return -1;
  }

  part2() {
    return -1;
  }
}

const file = process.argv[2] ?? './input.txt';
const day = new Day(file);
console.log(`advent of code: day`);
console.log(`part 1: ${day.part1()}`);
console.log(`part 2: ${day.part2()}`);
