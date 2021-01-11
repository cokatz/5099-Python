#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# define filter function
def filter(oldfile, newfile):
    with open(oldfile, "r") as infile, open(newfile, "w") as outfile:
        for line in infile:
            # Put any processing logic here
            if not line.startswith('#'):
                outfile.write(line)

# process file
filter("filter.py", "filter.txt")

print("\nDone.")
