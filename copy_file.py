from sys import argv
from os.path import exists

program_name, from_copy, to_copy = argv

file1 = open(from_copy, 'r')
file1_read = file1.read()

print "Press Enter to copy a file", "press CTRL + Z to discard copying"

raw_input()

file2 = open(to_copy, "w")
file2.write(file1_read)

file1.close
file2.close
