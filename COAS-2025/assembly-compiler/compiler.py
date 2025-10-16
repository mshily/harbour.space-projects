import argparse
from pathlib import Path
from assemble_text import assemble_text

# MAIN logic of compiler. Work with the terminal
def compiler ():
    arg_parser = argparse.ArgumentParser(description="1 byte binary format 00AABBCC")
    
    arg_parser.add_argument("-i", "--input", type=Path, required = True, help = "input .asm") # Path to our .asm file
    arg_parser.add_argument("-o", "--output", type=Path, help = "output binaty (.bin) file") # Path to our binary output file
    arg_parser.add_argument("--show", action="store_true", help="print of bytes") #Print instructions
    
    args = arg_parser.parse_args()

    text = args.input.read_text(encoding = "utf-8")
    raw, bitlines = assemble_text(text)

    if args.output:
        args.output.write_bytes(raw)
    
    if args.show or not args.output:
        for b in bitlines:
            print(b)


if __name__ == "__main__":
    compiler()