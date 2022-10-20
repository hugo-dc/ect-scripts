import sys

USAGE = sys.argv[0] + " <total_push>"

def main():
    if len(sys.argv) != 2:
        print(USAGE)
        exit(1)

    print("6000" * int(sys.argv[1]))

if __name__ == '__main__':
    main()
