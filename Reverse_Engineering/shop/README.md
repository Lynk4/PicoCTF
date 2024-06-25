# shop

---

AUTHOR: THELSHELL

Description
Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: source. The shop is open 
for business at nc mercury.picoctf.net 42159.

---
basic file check:

```bash
❯ file source
source: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, Go BuildID=PjavkptB2tPNbBJewQBD/KlDP1g_fpBnKyhti11wQ/JIWBEgtPAt3YPE6g8qd7/pWlMkjZuAYGqbSv46xuR, with debug_info, not stripped

```

---

running the program:

```bash
❯ ./source
Welcome to the market!
=====================
You have 40 coins
	Item		Price	Count
(0) Quiet Quiches	10	12
(1) Average Apple	15	8
(2) Fruitful Flag	100	1
(3) Sell an Item
(4) Exit
Choose an option: 
0
How many do you want to buy?
2
You have 20 coins
	Item		Price	Count
(0) Quiet Quiches	10	10
(1) Average Apple	15	8
(2) Fruitful Flag	100	1
(3) Sell an Item
(4) Exit
Choose an option: 
4
```
---

So we can try a negative number to buy some stuffs..

---

```bash
❯ nc mercury.picoctf.net 42159
Welcome to the market!
=====================
You have 40 coins
	Item		Price	Count
(0) Quiet Quiches	10	12
(1) Average Apple	15	8
(2) Fruitful Flag	100	1
(3) Sell an Item
(4) Exit
Choose an option: 
0
How many do you want to buy?
-12
You have 160 coins
	Item		Price	Count
(0) Quiet Quiches	10	24
(1) Average Apple	15	8
(2) Fruitful Flag	100	1
(3) Sell an Item
(4) Exit
Choose an option: 
2
How many do you want to buy?
1
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 55 57 55 98 50 57 50 99 125]
```

we got the flag let's decode it in python

```python
❯ python3
Python 3.11.8 (main, Feb  7 2024, 21:52:08) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> flag = "112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 55 57 55 98 50 57 50 99 125"
>>> flag.split()
['112', '105', '99', '111', '67', '84', '70', '123', '98', '52', '100', '95', '98', '114', '111', '103', '114', '97', '109', '109', '101', '114', '95', '55', '57', '55', '98', '50', '57', '50', '99', '125']
>>> [int(c) for c in flag.split()]
[112, 105, 99, 111, 67, 84, 70, 123, 98, 52, 100, 95, 98, 114, 111, 103, 114, 97, 109, 109, 101, 114, 95, 55, 57, 55, 98, 50, 57, 50, 99, 125]
>>> [chr(int(c)) for c in flag.split()]
['p', 'i', 'c', 'o', 'C', 'T', 'F', '{', 'b', '4', 'd', '_', 'b', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'e', 'r', '_', '7', '9', '7', 'b', '2', '9', '2', 'c', '}']
>>> ''.join([chr(int(c)) for c in flag.split()])
'picoCTF{b4d_brogrammer_797b292c}'
>>> 
```

flag:```picoCTF{b4d_brogrammer_797b292c}```

---

