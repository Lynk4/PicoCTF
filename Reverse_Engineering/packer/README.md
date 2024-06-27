# packer

---
AUTHOR: MUBARAK MIKAIL

Description
Reverse this linux executable?
binary

---


The provided binary is upx packed........

We need to unpack it using upx

```bash
❯ file out
out: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, no section header
❯ upx -d out
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2024
UPX 4.2.2       Markus Oberhumer, Laszlo Molnar & John Reiser    Jan 3rd 2024

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
[WARNING] bad b_info at 0x4b718

[WARNING] ... recovery at 0x4b714

    877724 <-    336520   38.34%   linux/amd64   out

Unpacked 1 file.
❯ file out
out: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, BuildID[sha1]=2e06e54daad34a6d4b0c7ef71b3e1ce17ffbf6db, for GNU/Linux 3.2.0, not stripped
❯
```

Using strings.

```bash
❯ strings out | grep flag
Password correct, please see flag: 7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f65313930633366337d
(mode_flags & PRINTF_FORTIFY) != 0
WARNING: Unsupported flag value(s) of 0x%x in DT_FLAGS_1.
version == NULL || !(flags & DL_LOOKUP_RETURN_NEWEST)
flag.c
_dl_x86_hwcap_flags
_dl_stack_flags
```

it's a hexadecimal flag..

decode it in cyber chef...

---

<img width="1170" alt="Screenshot 2024-06-27 at 5 08 30 PM" src="https://github.com/Lynk4/PicoCTF/assets/44930131/585dabab-068d-4d34-8610-23bac8501dc6">


---

flag:```picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_e190c3f3}```

---



