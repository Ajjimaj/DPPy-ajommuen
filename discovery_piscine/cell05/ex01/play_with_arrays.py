#!/usr/bin/env python3

a = [2, 8, 9, 48, 8, 22, -12, 2, 42, 42.42, 67]

# List comprehension
new_array = [num + 2 for num in a]

print(f"Original array: {a}")
print(f"New array: {new_array}")