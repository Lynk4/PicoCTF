---
# breadth

---

AUTHOR: ASPHYXIA

Description
Surely this is what people mean when they say "horizontal scaling," right?
TOP SECRET INFO:
Our operatives managed to exfiltrate an in-development version of this challenge, 
where the function with the real flag had a mistake in it. Can you help us get the 
flag?

---

So there's two files different versions.......

let's chek out whats the difference between these two...

```bash
❯ ls
 breadth.v1   breadth.v2
❯ cmp -bl breadth.v1 breadth.v2
    725 315 M-M  103 C
    726 120 P    122 R
    727 141 a    345 M-e
    728  57 /    327 M-W
    729  61 1    117 O
    730 350 M-h  165 u
    731 223 M-^S 237 M-^_
    732 150 h    371 M-y
    733  31 ^Y   234 M-^\
    734 163 s    127 W
    735 271 M-9    6 ^F
    736 220 M-^P  14 ^L
    737 377 M-^?  53 +
    738 313 M-K  302 M-B
    739 307 M-G  337 M-_
    740 327 M-W   47 '
    741 270 M-8  121 Q
    742 250 M-(  247 M-'
    743 361 M-q  335 M-]
    744 264 M-4  251 M-)
 610380 124 T    104 D
 610383 270 M-8  110 H
 610384  72 :     75 =
 610385 200 M-^@  76 >
 610386  67 7    307 M-G
 610387 320 M-P   33 ^[
 610388 110 H      4 ^D
 610389  71 9    164 t
 610390 302 M-B   12 ^J
 610391 164 t    303 M-C
 610392  10 ^H   146 f
 610393 303 M-C   17 ^O
 610394  17 ^O    37 ^_
 610395  37 ^_   204 M-^D
 610396 200 M-^@   0 ^@
2438996  61 1     62 2
╭─ ~/picoctf/breadth
╰─❯
```
---

So the huge difference lies in  "610380 124 T    104 D" thus line 

but 610380 is not an actual address...

converting this in hex
```
❯ python3
Python 3.12.4 (main, Jun  7 2024, 06:33:07) [GCC 14.1.1 20240522] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> hex(610380)
'0x9504c'
```
0x9504c is the actual address

***so we need to add 0x9504c and entry point address to get the actual address where the data changes in both the binaries.........***

0x9504c + entry point address


---

let's open breadth.v1 in ghidra........

Analyzing in ghidra.......

there's two entry point.....

1st entry point address:=0101091
<img width="1317" alt="e-1" src="https://github.com/Lynk4/PicoCTF/assets/44930131/c4434da6-ef27-4248-804d-bcee5e25071f">

2nd entry point address:00100018
<img width="1318" alt="e-2" src="https://github.com/Lynk4/PicoCTF/assets/44930131/619c1284-5289-4519-956d-07e9089ec811">

let's try both......

for saving your time I’ve tried both the second entry point is correct.......

---

so 

00100018 + 9504c = 195064

search for 195064 in ghidra.  shortcut key g 


<img width="1324" alt="Screenshot 2024-07-10 at 1 26 28 AM" src="https://github.com/Lynk4/PicoCTF/assets/44930131/ac543bf2-7a9f-44c9-a741-8141f8de65bc">

---

flag:```picoCTF{VnDB2LUf1VFJkdfDJtdYtFlMexPxXS6X}```

---



