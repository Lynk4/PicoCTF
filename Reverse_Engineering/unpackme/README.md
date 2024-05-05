# unpackme

---
Description
Can you get the flag?

---

Basic file check:

---
```bash
❯ checksec --file=unpackme-upx
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH	Symbols		FORTIFY	Fortified	FortifiableFILE
Partial RELRO   Canary found      NX enabled    No PIE          No RPATH   No RUNPATH   1973 Symbols	 No	0		0	unpackme-upx
```

---

Let's run it...

```bash
❯ ./unpackme-upx
What's my favorite number? 1111
Sorry, that's not it!
```

---

The binary asking for a number...& we don't know it..........

The binary name end with upx ..by checking upx manual it used to compress executables.

upx - compress or expand executable files

---

so to extract 

```bash
╰─❯ upx -d unpackme-upx
```

after extracting the size of the binary will increase

Now let's open it in gdb

```bash
❯ sudo gdb ./unpackme-upx
GNU gdb (Debian 13.2-1) 13.2
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
pwndbg: loaded 156 pwndbg commands and 47 shell commands. Type pwndbg [--shell | --all] [filter] for a list.
pwndbg: created $rebase, $base, $ida GDB functions (can be used with print/break)
Reading symbols from ./unpackme-upx...
(No debugging symbols found in ./unpackme-upx)
------- tip of the day (disable with set show-tips off) -------
If you have debugging symbols the info args command shows current frame's function arguments (use up and down to switch between frames)
pwndbg> disass main
Dump of assembler code for function main:
   0x0000000000401e43 <+0>:	endbr64
   0x0000000000401e47 <+4>:	push   rbp
   0x0000000000401e48 <+5>:	mov    rbp,rsp
   0x0000000000401e4b <+8>:	sub    rsp,0x50
   0x0000000000401e4f <+12>:	mov    DWORD PTR [rbp-0x44],edi
   0x0000000000401e52 <+15>:	mov    QWORD PTR [rbp-0x50],rsi
   0x0000000000401e56 <+19>:	mov    rax,QWORD PTR fs:0x28
   0x0000000000401e5f <+28>:	mov    QWORD PTR [rbp-0x8],rax
   0x0000000000401e63 <+32>:	xor    eax,eax
   0x0000000000401e65 <+34>:	movabs rax,0x4c75257240343a41
   0x0000000000401e6f <+44>:	movabs rdx,0x30623e306b6d4146
   0x0000000000401e79 <+54>:	mov    QWORD PTR [rbp-0x30],rax
   0x0000000000401e7d <+58>:	mov    QWORD PTR [rbp-0x28],rdx
   0x0000000000401e81 <+62>:	movabs rax,0x5f60643630486637
   0x0000000000401e8b <+72>:	mov    QWORD PTR [rbp-0x20],rax
   0x0000000000401e8f <+76>:	mov    DWORD PTR [rbp-0x18],0x37666132
   0x0000000000401e96 <+83>:	mov    WORD PTR [rbp-0x14],0x4e
   0x0000000000401e9c <+89>:	lea    rdi,[rip+0xb1161]        # 0x4b3004
   0x0000000000401ea3 <+96>:	mov    eax,0x0
   0x0000000000401ea8 <+101>:	call   0x410ba0 <printf>
   0x0000000000401ead <+106>:	lea    rax,[rbp-0x3c]
   0x0000000000401eb1 <+110>:	mov    rsi,rax
   0x0000000000401eb4 <+113>:	lea    rdi,[rip+0xb1165]        # 0x4b3020
   0x0000000000401ebb <+120>:	mov    eax,0x0
   0x0000000000401ec0 <+125>:	call   0x410d30 <__isoc99_scanf>
   0x0000000000401ec5 <+130>:	mov    eax,DWORD PTR [rbp-0x3c]
   0x0000000000401ec8 <+133>:	cmp    eax,0xb83cb
   0x0000000000401ecd <+138>:	jne    0x401f12 <main+207>
   0x0000000000401ecf <+140>:	lea    rax,[rbp-0x30]
   0x0000000000401ed3 <+144>:	mov    rsi,rax
   0x0000000000401ed6 <+147>:	mov    edi,0x0
   0x0000000000401edb <+152>:	call   0x401d85 <rotate_encrypt>
   0x0000000000401ee0 <+157>:	mov    QWORD PTR [rbp-0x38],rax
   0x0000000000401ee4 <+161>:	mov    rdx,QWORD PTR [rip+0xdd7e5]        # 0x4df6d0 <stdout>
   0x0000000000401eeb <+168>:	mov    rax,QWORD PTR [rbp-0x38]
   0x0000000000401eef <+172>:	mov    rsi,rdx
   0x0000000000401ef2 <+175>:	mov    rdi,rax
   0x0000000000401ef5 <+178>:	call   0x420980 <fputs>
   0x0000000000401efa <+183>:	mov    edi,0xa
   0x0000000000401eff <+188>:	call   0x420e20 <putchar>
   0x0000000000401f04 <+193>:	mov    rax,QWORD PTR [rbp-0x38]
   0x0000000000401f08 <+197>:	mov    rdi,rax
   0x0000000000401f0b <+200>:	call   0x42ec70 <free>
   0x0000000000401f10 <+205>:	jmp    0x401f1e <main+219>
   0x0000000000401f12 <+207>:	lea    rdi,[rip+0xb110a]        # 0x4b3023
   0x0000000000401f19 <+214>:	call   0x420c40 <puts>
   0x0000000000401f1e <+219>:	mov    eax,0x0
   0x0000000000401f23 <+224>:	mov    rcx,QWORD PTR [rbp-0x8]
   0x0000000000401f27 <+228>:	xor    rcx,QWORD PTR fs:0x28
   0x0000000000401f30 <+237>:	je     0x401f37 <main+244>
   0x0000000000401f32 <+239>:	call   0x45cba0 <__stack_chk_fail_local>
   0x0000000000401f37 <+244>:	leave
   0x0000000000401f38 <+245>:	ret
End of assembler dump.
pwndbg> break *0x0000000000401ec8
Breakpoint 1 at 0x401ec8
pwndbg> run
Starting program: /home/lynk/picoCTF/unpackme/unpackme-upx 
What's my favorite number? 111

Breakpoint 1, 0x0000000000401ec8 in main ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
────────────────────────────────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]─────────────────────────────────────────────────
*RAX  0x6f
*RBX  0x400530 ◂— 0x0
 RCX  0x0
 RDX  0x0
*RDI  0x7fffffffdda0 ◂— 0x313131 /* '111' */
 RSI  0x0
*R8   0xa
 R9   0x0
*R10  0x4ba420 (_nl_C_LC_CTYPE_toupper+512) ◂— 0x100000000
 R11  0x0
*R12  0x402fc0 (__libc_csu_fini) ◂— endbr64 
 R13  0x0
*R14  0x4df018 (_GLOBAL_OFFSET_TABLE_+24) —▸ 0x44efd0 (__strcpy_avx2) ◂— endbr64 
 R15  0x0
*RBP  0x7fffffffe330 —▸ 0x402f20 (__libc_csu_init) ◂— endbr64 
*RSP  0x7fffffffe2e0 —▸ 0x7fffffffe468 —▸ 0x7fffffffe6c8 ◂— '/home/lynk/picoCTF/unpackme/unpackme-upx'
*RIP  0x401ec8 (main+133) ◂— cmp eax, 0xb83cb
─────────────────────────────────────────────────────────[ DISASM / x86-64 / set emulate on ]──────────────────────────────────────────────────────────
 ► 0x401ec8 <main+133>    cmp    eax, 0xb83cb
   0x401ecd <main+138>    jne    main+207                      <main+207>
    ↓
   0x401f12 <main+207>    lea    rdi, [rip + 0xb110a]
   0x401f19 <main+214>    call   puts                      <puts>
 
   0x401f1e <main+219>    mov    eax, 0
   0x401f23 <main+224>    mov    rcx, qword ptr [rbp - 8]
   0x401f27 <main+228>    xor    rcx, qword ptr fs:[0x28]
   0x401f30 <main+237>    je     main+244                      <main+244>
 
   0x401f32 <main+239>    call   __stack_chk_fail_local                      <__stack_chk_fail_local>
 
   0x401f37 <main+244>    leave  
   0x401f38 <main+245>    ret    
───────────────────────────────────────────────────────────────────────[ STACK ]───────────────────────────────────────────────────────────────────────
00:0000│ rsp 0x7fffffffe2e0 —▸ 0x7fffffffe468 —▸ 0x7fffffffe6c8 ◂— '/home/lynk/picoCTF/unpackme/unpackme-upx'
01:0008│-048 0x7fffffffe2e8 ◂— 0x100000002
02:0010│-040 0x7fffffffe2f0 ◂— 0x6f004dc0e0
03:0018│-038 0x7fffffffe2f8 —▸ 0x402f9c (__libc_csu_init+124) ◂— add rbx, 1
04:0020│-030 0x7fffffffe300 ◂— 'A:4@r%uLFAmk0>b07fH06d`_2af7N'
05:0028│-028 0x7fffffffe308 ◂— 'FAmk0>b07fH06d`_2af7N'
06:0030│-020 0x7fffffffe310 ◂— '7fH06d`_2af7N'
07:0038│-018 0x7fffffffe318 ◂— 0x4e37666132 /* '2af7N' */
─────────────────────────────────────────────────────────────────────[ BACKTRACE ]─────────────────────────────────────────────────────────────────────
 ► 0         0x401ec8 main+133
   1         0x402750 __libc_start_main+1168
   2         0x401c8e _start+46
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
pwndbg> print $eax
$1 = 111
pwndbg> print 0xb83cb
$2 = 754635
pwndbg> set $eax=754635
pwndbg> c
Continuing.
picoCTF{up><_m3_f7w_e510a27f}
[Inferior 1 (process 10708) exited normally]
pwndbg>
```

---

We change the value of eax ..........

---
