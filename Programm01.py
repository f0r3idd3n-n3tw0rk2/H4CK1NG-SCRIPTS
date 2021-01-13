import sys

def print5time(line_to_print):
    for count in range(0,5):
        print(line_to_print)

print5time(sys.args[1])