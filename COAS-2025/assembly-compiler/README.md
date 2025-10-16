# Compiler  
**Author:** Ivan Zhukau
## Task
Write a **compiler in Python** that translates assembly code into binary according to the following format:
```
00AABBCC
```

Where:
- **AA** – `registerA`
- **BB** – `registerB`
- **CC** – `opcode`
- `00` – XOR  
- `01` – EQUAL (==)  
- `10` – ADDITION  
- `11` – MOVE / NO OPERATION  

Result is **always stored in `registerA`**.

Comments in assembly start with a semicolon (`;`).

---

## Example of input assembly

```asm
mov reg1, reg2
xor reg0, reg3
add reg0, reg1
; comment example
eq reg1, reg2 ; comments should work like this
add reg3, reg3
```

Expected binary output:
```
00011011
00001100
00000110
00011001
00111110
```

---
### So how to run the compiler

1. Create an .asm file

Example: program.asm
```
add reg0, reg1
mov reg2, reg3
```
2. Run the compiler from the terminal
```
python compiler.py -i program.asm --show -o program.bin
```

| Flag             | Description                          |
| ---------------- | ------------------------------------ |
| `-i`, `--input`  | Path to the input `.asm` file        |
| `-o`, `--output` | Path to the output `.bin` file       |
| `--show`         | Print resulting bytes in binary form |


## About format
| Bits | Field | Meaning                             |
| ---- | ----- | ----------------------------------- |
| 7–6  | `00`  | constant prefix                     |
| 5–4  | `AA`  | destination register (`reg0..reg3`) |
| 3–2  | `BB`  | source register (`reg0..reg3`)      |
| 1–0  | `CC`  | opcode                              |

Registers → binary codes:
| Register | Bits |
| -------- | ---- |
| `reg0`   | `00` |
| `reg1`   | `01` |
| `reg2`   | `10` |
| `reg3`   | `11` |


Opcodes → binary codes:
| Instruction | Bits | Meaning             |
| ----------- | ---- | ------------------- |
| `xor`       | `00` | bitwise XOR         |
| `eq`        | `01` | equality (==)       |
| `add`       | `10` | addition            |
| `mov`       | `11` | move / no operation |
