# Reverse

Description
Try reversing this file? Can ya?
I forgot the password to this file. Please find it for me?

---



```bash
❯ sudo gdb ./ret
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
Reading symbols from ./ret...
(No debugging symbols found in ./ret)
------- tip of the day (disable with set show-tips off) -------
Disable Pwndbg context information display with set context-sections ''
pwndbg> info functions
All defined functions:

Non-debugging symbols:
0x0000000000001000  _init
0x0000000000001080  __cxa_finalize@plt
0x0000000000001090  puts@plt
0x00000000000010a0  __stack_chk_fail@plt
0x00000000000010b0  printf@plt
0x00000000000010c0  strcmp@plt
0x00000000000010d0  __isoc99_scanf@plt
0x00000000000010e0  _start
0x0000000000001110  deregister_tm_clones
0x0000000000001140  register_tm_clones
0x0000000000001180  __do_global_dtors_aux
0x00000000000011c0  frame_dummy
0x00000000000011c9  main
0x00000000000012d0  __libc_csu_init
0x0000000000001340  __libc_csu_fini
0x0000000000001348  _fini
pwndbg> disass main
Dump of assembler code for function main:
   0x00000000000011c9 <+0>:	endbr64
   0x00000000000011cd <+4>:	push   rbp
   0x00000000000011ce <+5>:	mov    rbp,rsp
   0x00000000000011d1 <+8>:	sub    rsp,0x60
   0x00000000000011d5 <+12>:	mov    rax,QWORD PTR fs:0x28
   0x00000000000011de <+21>:	mov    QWORD PTR [rbp-0x8],rax
   0x00000000000011e2 <+25>:	xor    eax,eax
   0x00000000000011e4 <+27>:	movabs rax,0x7b4654436f636970
   0x00000000000011ee <+37>:	movabs rdx,0x337633725f666c33
   0x00000000000011f8 <+47>:	mov    QWORD PTR [rbp-0x30],rax
   0x00000000000011fc <+51>:	mov    QWORD PTR [rbp-0x28],rdx
   0x0000000000001200 <+55>:	movabs rax,0x75735f676e693572
   0x000000000000120a <+65>:	movabs rdx,0x6c75663535656363
   0x0000000000001214 <+75>:	mov    QWORD PTR [rbp-0x20],rax
   0x0000000000001218 <+79>:	mov    QWORD PTR [rbp-0x18],rdx
   0x000000000000121c <+83>:	movabs rax,0x346434316237645f
   0x0000000000001226 <+93>:	mov    QWORD PTR [rbp-0x10],rax
   0x000000000000122a <+97>:	lea    rdi,[rip+0xdd7]        # 0x2008
   0x0000000000001231 <+104>:	mov    eax,0x0
   0x0000000000001236 <+109>:	call   0x10b0 <printf@plt>
   0x000000000000123b <+114>:	lea    rax,[rbp-0x60]
   0x000000000000123f <+118>:	mov    rsi,rax
   0x0000000000001242 <+121>:	lea    rdi,[rip+0xde8]        # 0x2031
   0x0000000000001249 <+128>:	mov    eax,0x0
   0x000000000000124e <+133>:	call   0x10d0 <__isoc99_scanf@plt>
   0x0000000000001253 <+138>:	lea    rax,[rbp-0x60]
   0x0000000000001257 <+142>:	mov    rsi,rax
   0x000000000000125a <+145>:	lea    rdi,[rip+0xdd3]        # 0x2034
   0x0000000000001261 <+152>:	mov    eax,0x0
   0x0000000000001266 <+157>:	call   0x10b0 <printf@plt>
   0x000000000000126b <+162>:	lea    rdx,[rbp-0x30]
   0x000000000000126f <+166>:	lea    rax,[rbp-0x60]
   0x0000000000001273 <+170>:	mov    rsi,rdx
   0x0000000000001276 <+173>:	mov    rdi,rax
   0x0000000000001279 <+176>:	call   0x10c0 <strcmp@plt>
   0x000000000000127e <+181>:	test   eax,eax
   0x0000000000001280 <+183>:	jne    0x129c <main+211>
   0x0000000000001282 <+185>:	lea    rdi,[rip+0xdbf]        # 0x2048
   0x0000000000001289 <+192>:	call   0x1090 <puts@plt>
   0x000000000000128e <+197>:	lea    rax,[rbp-0x30]
   0x0000000000001292 <+201>:	mov    rdi,rax
   0x0000000000001295 <+204>:	call   0x1090 <puts@plt>
   0x000000000000129a <+209>:	jmp    0x12a8 <main+223>
   0x000000000000129c <+211>:	lea    rdi,[rip+0xdf3]        # 0x2096
   0x00000000000012a3 <+218>:	call   0x1090 <puts@plt>
   0x00000000000012a8 <+223>:	mov    eax,0x0
   0x00000000000012ad <+228>:	mov    rcx,QWORD PTR [rbp-0x8]
   0x00000000000012b1 <+232>:	xor    rcx,QWORD PTR fs:0x28
   0x00000000000012ba <+241>:	je     0x12c1 <main+248>
   0x00000000000012bc <+243>:	call   0x10a0 <__stack_chk_fail@plt>
   0x00000000000012c1 <+248>:	leave
   0x00000000000012c2 <+249>:	ret
End of assembler dump.
pwndbg> break *main+176
Breakpoint 1 at 0x1279
pwndbg> run
Starting program: /home/lynk/picoCTF/reverse/ret 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Enter the password to unlock this file: lynk
You entered: lynk

Breakpoint 1, 0x0000555555555279 in main ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
────────────────────────────────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]─────────────────────────────────────────────────
*RAX  0x7fffffffe320 ◂— 0x6b6e796c /* 'lynk' */
*RBX  0x7fffffffe498 —▸ 0x7fffffffe6f1 ◂— '/home/lynk/picoCTF/reverse/ret'
 RCX  0x0
*RDX  0x7fffffffe350 ◂— 'picoCTF{3lf_r3v3r5ing_succe55ful_d7b14d4'
*RDI  0x7fffffffe320 ◂— 0x6b6e796c /* 'lynk' */
*RSI  0x7fffffffe350 ◂— 'picoCTF{3lf_r3v3r5ing_succe55ful_d7b14d4'
*R8   0x73
*R9   0x1
 R10  0x0
*R11  0x202
 R12  0x0
*R13  0x7fffffffe4a8 —▸ 0x7fffffffe710 ◂— 'PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
 R14  0x0
*R15  0x7ffff7ffd000 (_rtld_global) —▸ 0x7ffff7ffe2d0 —▸ 0x555555554000 ◂— 0x10102464c457f
*RBP  0x7fffffffe380 ◂— 0x1
*RSP  0x7fffffffe320 ◂— 0x6b6e796c /* 'lynk' */
*RIP  0x555555555279 (main+176) ◂— call 0x5555555550c0
─────────────────────────────────────────────────────────[ DISASM / x86-64 / set emulate on ]──────────────────────────────────────────────────────────
 ► 0x555555555279 <main+176>    call   strcmp@plt                <strcmp@plt>
        s1: 0x7fffffffe320 ◂— 0x6b6e796c /* 'lynk' */
        s2: 0x7fffffffe350 ◂— 'picoCTF{3lf_r3v3r5ing_succe55ful_d7b14d4'
 
   0x55555555527e <main+181>    test   eax, eax
   0x555555555280 <main+183>    jne    main+211                <main+211>
 
   0x555555555282 <main+185>    lea    rdi, [rip + 0xdbf]
   0x555555555289 <main+192>    call   puts@plt                <puts@plt>
 
   0x55555555528e <main+197>    lea    rax, [rbp - 0x30]
   0x555555555292 <main+201>    mov    rdi, rax
   0x555555555295 <main+204>    call   puts@plt                <puts@plt>
 
   0x55555555529a <main+209>    jmp    main+223                <main+223>
 
   0x55555555529c <main+211>    lea    rdi, [rip + 0xdf3]
   0x5555555552a3 <main+218>    call   puts@plt                <puts@plt>
───────────────────────────────────────────────────────────────────────[ STACK ]───────────────────────────────────────────────────────────────────────
00:0000│ rax rdi rsp 0x7fffffffe320 ◂— 0x6b6e796c /* 'lynk' */
01:0008│-058         0x7fffffffe328 ◂— 0x0
... ↓                4 skipped
06:0030│ rdx rsi     0x7fffffffe350 ◂— 'picoCTF{3lf_r3v3r5ing_succe55ful_d7b14d4'
07:0038│-028         0x7fffffffe358 ◂— '3lf_r3v3r5ing_succe55ful_d7b14d4'
─────────────────────────────────────────────────────────────────────[ BACKTRACE ]─────────────────────────────────────────────────────────────────────
 ► 0   0x555555555279 main+176
   1   0x7ffff7df06ca __libc_start_call_main+122
   2   0x7ffff7df0785 __libc_start_main+133
   3   0x55555555510e _start+46
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
pwndbg> info registers
rax            0x7fffffffe320      140737488347936
rbx            0x7fffffffe498      140737488348312
rcx            0x0                 0
rdx            0x7fffffffe350      140737488347984
rsi            0x7fffffffe350      140737488347984
rdi            0x7fffffffe320      140737488347936
rbp            0x7fffffffe380      0x7fffffffe380
rsp            0x7fffffffe320      0x7fffffffe320
r8             0x73                115
r9             0x1                 1
r10            0x0                 0
r11            0x202               514
r12            0x0                 0
r13            0x7fffffffe4a8      140737488348328
r14            0x0                 0
r15            0x7ffff7ffd000      140737354125312
rip            0x555555555279      0x555555555279 <main+176>
eflags         0x206               [ PF IF ]
cs             0x33                51
ss             0x2b                43
ds             0x0                 0
es             0x0                 0
fs             0x0                 0
gs             0x0                 0
pwndbg> x/s $rsi
0x7fffffffe350:	"picoCTF{3lf_r3v3r5ing_succe55ful_d7b14d4"
pwndbg>
```

