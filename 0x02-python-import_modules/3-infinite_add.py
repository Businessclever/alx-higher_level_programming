#!/usr/bin/python3

import sys

if __name__ == "__main__":
    """Print the addition of all arguments."""
    total = sum(map(int, sys.argv[1:]))
    print("{}".format(total))

