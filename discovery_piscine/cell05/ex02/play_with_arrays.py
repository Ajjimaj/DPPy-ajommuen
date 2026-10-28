#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2, 42, 42.42, 67]

# List comprehension
more_than_five = [num for num in original_array if num > 5]

print(f"Original array: {original_array}")
print(f"More than five: {more_than_five}")