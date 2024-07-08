# transposition-trial

---
AUTHOR: WILL HONG

Description
Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message.
Download the corrupted message here.


---

here's the content of message.txt

```bash
❯ cat message.txt
heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4%
```
let's write a python solver.........

---

```python
#!/usr/bin/python3

with open("message.txt") as filp:
	contents = filp.read()

for i in range(0, len(contents), 3):
	chunk = contents[i : i + 3]
	a, b, c = chunk
	print(c + a + b, end="")
```
---

running the above script........

```bash
❯ python solve.py
The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}
╭─ ~/picoctf/transposition-trial
╰─❯
```

flag:```picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}```

---
