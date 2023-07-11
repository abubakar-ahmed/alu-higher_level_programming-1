#!/usr/bin/python3
import sys

# Get all command-line arguments excluding the script name
arguments = sys.argv[1:]

# Convert arguments to integers and calculate the sum
total = sum(int(arg) for arg in arguments)

# Print the sum
print(total)
