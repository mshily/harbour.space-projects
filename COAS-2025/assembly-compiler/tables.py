# REGISTER AND OPCODE MAPS
REG_MAP = {
    "reg0": "00",
    "reg1": "01",
    "reg2": "10",
    "reg3": "11",
}

OPCODE_MAP = {
    "xor": "00",
    "eq": "01",
    "add": "10",
    "mov": "11",
    "nop": "11",
}

def register_to_binary(register: str) -> str:
    register = register.lower()
    if register not in REG_MAP:
        raise ValueError(f"Invalid register: {register}")
    return REG_MAP[register]

def opcode_to_binary(opcode: str) -> str:
    opcode = opcode.lower()
    if opcode not in OPCODE_MAP:
        raise ValueError(f"Invalid opcode: {opcode}")
    return OPCODE_MAP[opcode]
