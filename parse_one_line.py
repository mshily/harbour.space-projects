import re
from typing import Optional
from tables import register_to_binary, opcode_to_binary

# now we need to create a function that will take a line of assembly code and convert it to binary code
TOKEN_REGEX = re.compile(r"^\s*([a-zA-Z]+)\s*(?:([^;]+))?")

def assemble_line(line: str) -> Optional[int]:
    line = line.split(";", 1)[0].strip() # we need to remove the comment from the end of the line
    if not line:
        return None

    match = TOKEN_REGEX.match(line)
    if not match:
        return None

    opcode = match.group(1)
    operands = match.group(2)

    regs = []
    if operands:
        regs = [p for p in re.split(r"[\s,]+", operands) if p]

    # validate opcode first to surface unknown instructions early
    code = opcode_to_binary(opcode)

    if opcode == "nop":
        a_name, b_name = "reg0", "reg0"
    else:
        if len(regs) != 2:
            raise ValueError(f"Invalid operands: {operands}")
        a_name, b_name = regs[0].lower(), regs[1].lower()
    
    a = register_to_binary(a_name)
    b = register_to_binary(b_name)

    bits = "00" + a + b + code
    value = int(bits, 2)
    return value

