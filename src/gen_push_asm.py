import sys

USAGE = sys.argv[0] + " <items>"

def main():
    if len(sys.argv) != 2:
        print(USAGE)

    print("push1(0) " * int(sys.argv[1]))

if __name__ == '__main__':
    main()

