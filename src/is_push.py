import sys

USAGE = sys.argv[0] +  """ <opcode_number> - Given opcode_number, returns False if it doesn't corresponds 
                                 to a PUSH opcode, otherwise it prints the number of bytes required by the 
                                 PUSH opcode."""

def main():

    if len(sys.argv) != 2:
        print(USAGE)
        exit(1)

    opcode = sys.argv[1]

    if opcode.startswith('0x'):
        opcode = int(opcode, 16)
    else:
        opcode = int(opcode)

    if opcode >= 0x60 and opcode <= 0x7f:
        print(opcode - 0x5f)
    else:
        print("False")

if __name__ == '__main__':
    main()
