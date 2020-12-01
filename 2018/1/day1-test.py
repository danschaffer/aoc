#!/usr/bin/env python3
frequency_changes = [int(item) for item in open('input').read().split('\n')]
final_frequency = sum(frequency_changes)
print(f"the resulting frequency after all changes is {final_frequency}")
count = 0
frequency_state = 0
frequency_states = [0]
index = 0
while True:
  frequency_state += frequency_changes[index]
  index = (index + 1) % len(frequency_changes)
  if index == 0:
    print(f"rolled over list of frequencies count {count} {len(frequency_states)}")
  if frequency_state in frequency_states:
    break
  frequency_states += [frequency_state]
print(f"the first frequency reaching twice is {frequency_state}")
