#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]

remove_dup = [x + 2 for x in original_array if x > 5]

# remove duplicate
print(original_array)
print(set(remove_dup))