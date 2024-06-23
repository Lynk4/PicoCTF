# Bbbbloat


---


Basic file check:

```bash
❯ checksec --file=bbbbloat
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH	Symbols		FORTIFY	Fortified	Fortifiable	FILE
Full RELRO      Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH   No Symbols	 No	0		bbbbloat
❯ file bbbbloat
bbbbloat: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=db1dc86836c3e0e4140eb30914db4af5bce7cb18, for GNU/Linux 3.2.0, stripped
```

---

Running the program:
```
❯ ./bbbbloat
What's my favorite number? 18
Sorry, that's not it!
```
---
open the binary in ghidra:

<img width="1395" alt="Screenshot 2024-06-23 at 10 41 38 PM" src="https://github.com/Lynk4/PicoCTF/assets/44930131/1de6a6e1-bc6d-43ff-8c61-7d0394cdca75">

---

here we can se a number is being comapared by our input.

the number is in hexadecimal.

convert it to decimal

```python
❯ python3
>>> 0x86187
549255
```

```bash
❯ ./bbbbloat
What's my favorite number? 549255
picoCTF{cu7_7h3_bl047_695036e3}
```

flag:```picoCTF{cu7_7h3_bl047_695036e3}```


---

