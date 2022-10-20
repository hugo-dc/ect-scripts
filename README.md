# Ethereum Consensus Tests Scripts

Useful scripts when writing Ethereum Consensus Tests

- `eof_gen.py` - Requires EVM code and optionally data to be stored in the EOF
    data section, will generate EOF formatted code containing the specified
    code and data.
- `gen_push.py` - In Yul each parameter required by an opcode corresponds to
    a PUSH statement in EVM, this script will generate the number of parameters
    indicated.
- `get_op_name.py` - Given an opcode number (decimal or hexadecimal) will
    return the opcode name.
- `get_opcodes.py` - Returns the requested opcodes (All/Valid, Terminating
    Opcodes, or Non-Terminating Opcodes).
- `is_push.py` - Given an opcode number it will return False if it doesn't
    correspond to a PUSH opcode, or will return the number of bytes it push to
    the stack.
- `stack_req.py` - Given an opcode number it will return the number of stack
    items required by the opcode.
