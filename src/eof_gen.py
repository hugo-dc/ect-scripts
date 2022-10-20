#!/bin/env python
import sys

MAGIC = b"\xef\x00\x01"
TERMINATOR = b"\x00"
USAGE = "Usage:\n\t" + sys.argv[0] + " <bytecode> [data]"

def clean_hex_input(i):
    result = i
    if i[0:2] == '0x':
        result = i[2:]
    return bytes.fromhex(result)

def get_eof(code, data):
    code_len = len(code)
    code_header = b"\x01" + code_len.to_bytes(2, byteorder='big')

    data_header = b""
    if data:
        data_len = len(data)
        data_header = b"\x02" + data_len.to_bytes(2, byteorder='big')

    eof_code = MAGIC + code_header + data_header + TERMINATOR + code + data
    return eof_code

def main():
    if len(sys.argv) != 3 and len(sys.argv) != 2:
        print(USAGE)
        exit(1)

    data = b""
    code = clean_hex_input(sys.argv[1])

    if len(sys.argv) > 2:
        data = clean_hex_input(sys.argv[2])

    eof = get_eof(code, data)

    print(eof.hex())
    
if __name__ == '__main__':
    main()

