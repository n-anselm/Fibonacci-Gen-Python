#!/usr/bin/python

# Author: n-anselm
# Date created: 221105
# Date modified: 221105
# Description: Print numbers in the Fibonacci sequence
# Fibonnaci sequence: https://en.wikipedia.org/wiki/Fibonacci_number

def main():
    count = 10
    current = 1
    hist_list = [0]  # Will contain the two previous numbers

    # Number of iterations is set by "count" variable
    for i in range(0, count):
        print(current)
        hist_list.append(current)
        current = hist_list[-1] + hist_list[-2]  # Add the two previous numbers to get the new number

        # Pop out the first item in the list so that the list length stays at 2
        if len(hist_list) > 2:
            hist_list.pop(0)


if __name__ == "__main__":
    main()
