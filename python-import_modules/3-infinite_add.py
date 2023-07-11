#!/usr/bin/python3
def add_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:d}".format(n))
        return
    else:
        i = 1
        add = 0
        while i <= n:
            add += int(argv[i])
            i += 1
        print("{:d}".format(add))

if _name_ == "_main_":
    import sys
    result = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            result += int(arg)
    print(result)
