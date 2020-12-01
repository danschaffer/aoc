# create list of int for all input data
frequency_changes = [int(item) for item in open('day1-input.txt').read().split('\n')]

# part 1 sums all of the values and outputs the last frequency
final_frequency = sum(frequency_changes)
print(f"the resulting frequency after all changes is {final_frequency}.")
# answer is 556

# part 2 keeps a list of all frequencies and loops through the list until a repeat is found
frequency_state = 0
frequency_states = [0]
index = 0
while True:
  frequency_state += frequency_changes[index]
  index = (index + 1) % len(frequency_changes)
  if frequency_state in frequency_states:
    break
  frequency_states += [frequency_state]
print(f"the first frequency reaching twice is {frequency_state}.")
# answer is 448 after looping through the list 144 times, takes a few minutes
