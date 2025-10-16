from parse_one_line import assemble_line
from typing import Tuple, List

# create instructions using each of lines
def assemble_text(text: str) -> Tuple[bytes, List[str]]:
    out = bytearray()
    bits = []

    for lineno, line in enumerate(text.splitlines(), 1):
        try:
            v = assemble_line(line)
        except Exception as e:
            raise ValueError(f"Line {lineno}: {e}")
            
        if v is None:
            continue
        out.append(v)
        bits.append(f"{v:08b}")

    return bytes(out), bits