# ASCII FTW

---


AUTHOR: ABHISHEK AGARWAL

Description
This program has constructed the flag using hex ascii values. Identify the flag text by disassembling the program.
You can download the file from here.

---

basic file check:

```bash
❯ file asciiftw
asciiftw: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e1c32dace8ac1516160b771e493f5ebffcac9855, for GNU/Linux 3.2.0, not stripped
❯ checksec --file=asciiftw
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH	Symbols		FORTIFY	Fortified	Fortifiable	FILE
Full RELRO      Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH   66 Symbols	  No	0		1		asciiftw
╭─ ~/picoctf/ascii-ftw
╰─❯
```
---

let's objdump .........

```bash
╰─❯ objdump -D -M intel asciiftw | less
```

Now in the main function there's a lot of hex data.........save it in a file......

<img width="1440" alt="d-1" src="https://github.com/Lynk4/PicoCTF/assets/44930131/c2b56fd6-73f3-4349-9cb4-4cd5e290efe3">

---

we only need hex characters... let's sort it out using some regx

```bash
❯ awk -F, '{print $2}' data.txt
0x70
0x69
0x63
0x6f
0x43
0x54
0x46
0x7b
0x41
0x53
0x43
0x49
0x49
0x5f
0x49
0x53
0x5f
0x45
0x41
0x53
0x59
0x5f
0x38
0x39
0x36
0x30
0x46
0x30
0x41
0x46
0x7d
╭─ ~/picoctf/ascii-ftw
╰─❯ awk -F, '{print $2}' data.txt > ascii.txt

╭─ ~/picoctf/ascii-ftw
╰─❯ tr -d "\n" < ascii.txt > a.txt
```

---

let's write a python script to conver hex to strings......

```python
# Hex string
hex_string = "0x700x690x630x6f0x430x540x460x7b0x410x530x430x490x490x5f0x490x530x5f0x450x410x530x590x5f0x380x390x360x300x460x300x410x460x7d"

# Remove the "0x" prefix and concatenate the string
cleaned_hex_string = hex_string.replace("0x", "")

# Convert hex string to bytes
byte_array = bytes.fromhex(cleaned_hex_string)

# Decode bytes to a string
decoded_string = byte_array.decode('utf-8')

print(decoded_string)
```

---
```bash
❯ python3 converter.py
picoCTF{ASCII_IS_EASY_8960F0AF}
```

flag:```picoCTF{ASCII_IS_EASY_8960F0AF}```

---

