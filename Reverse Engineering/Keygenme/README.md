---
# Keygenme

---
AUTHOR: LT 'SYREAL' JONES

Description
Can you get the flag?
Reverse engineer this binary.

---

Basic file check:

```bash
❯ file keygenme
keygenme: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=054f04db5ac2714c025f015397bec4f65af8e688, for GNU/Linux 3.2.0, stripped
❯ checksec --file=keygenme
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH	Symbols		FORTIFY	Fortified	Fortifiable	FILE
Full RELRO      Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH   No Symbols	No	0		3		keygenme
╭─ ~/picoctf/keygenme
╰─❯
❯ ./keygenme
Enter your license key: 111111111
That key is invalid.
╭─ ~/picoctf/keygenme                                                                                                                                   5s
╰─❯
```
---

So it's asking for a license.......


strings on the binary

```bash
❯ strings keygenme
/lib64/ld-linux-x86-64.so.2
mgUa
libcrypto.so.1.1
__gmon_start__
_ITM_deregisterTMCloneTable
_ITM_registerTMCloneTable
libc.so.6
sprintf
puts
__stack_chk_fail
stdin
fgets
strlen
__cxa_finalize
__libc_start_main
OPENSSL_1_1_0
GLIBC_2.4
GLIBC_2.2.5
u+UH
picoCTF{H
br1ng_y0H
ur_0wn_kH
dH34%(
[]A\A]A^A_
%02x
Enter your license key:
That key is valid.
That key is invalid.
:*3$"
GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0
.shstrtab
.interp
.note.gnu.property
.note.gnu.build-id
.note.ABI-tag
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.plt.sec
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.data
.bss
.comment
```
---

We can see some parts of flag but it's useless...

---

Let's use radare2


---

```bash
❯ r2 -AA ./keygenme
WARN: Relocs has not been applied. Please use `-e bin.relocs.apply=true` or `-e bin.cache=true` next time
INFO: Analyze all flags starting with sym. and entry0 (aa)
INFO: Analyze imports (af@@@i)
INFO: Analyze entrypoint (af@ entry0)
INFO: Analyze symbols (af@@@s)
INFO: Recovering variables
INFO: Analyze all functions arguments/locals (afva@@@F)
INFO: Analyze function calls (aac)
INFO: Analyze len bytes of instructions for references (aar)
INFO: Finding and parsing C++ vtables (avrr)
INFO: Analyzing methods
INFO: Recovering local variables (afva)
INFO: Type matching analysis for all functions (aaft)
INFO: Propagate noreturn information (aanr)
INFO: Scanning for strings constructed in code (/azs)
INFO: Finding function preludes (aap)
INFO: Enable anal.types.constraint for experimental type propagation
[0x00001120]> do?
Usage: do   # Debug (re)open commands
| do            open process (reload, alias for 'oo')
| dor [rarun2]  comma separated list of k=v rarun2 profile options (e dbg.profile)
| doe           show rarun2 startup profile
| doe!          edit rarun2 startup profile with $EDITOR
| doo [args]    Reopen in debug mode with args (alias for 'ood')
| doof [args]   Reopen in debug mode from file (alias for 'oodf')
| doc           close debug session
[0x00001120]> dor stdin=flag.txt
[0x00001120]> doo
INFO: File dbg:///home/lynk/picoctf/keygenme/keygenme reopened in read-write mode
WARN: Relocs has not been applied. Please use `-e bin.relocs.apply=true` or `-e bin.cache=true` next time
7677
[0x00001120]> db main
[0x00001120]> dc
INFO: hit breakpoint at: 0x5bb6440d748b
[0x5bb6440d748b]> pdf
            ;-- rax:
            ;-- rip:
            ; DATA XREF from entry0 @ 0x5bb6440d7141(r)
/ 144: int main (int argc, char **argv, char **envp);
|           ; arg int argc @ rdi
|           ; arg char **argv @ rsi
|           ; var int64_t canary @ rbp-0x8
|           ; var char *s @ rbp-0x30
|           ; var int64_t var_34h @ rbp-0x34
|           ; var char **var_40h @ rbp-0x40
|           0x5bb6440d748b b    f30f1efa       endbr64
|           0x5bb6440d748f      55             push rbp
|           0x5bb6440d7490      4889e5         mov rbp, rsp
|           0x5bb6440d7493      4883ec40       sub rsp, 0x40
|           0x5bb6440d7497      897dcc         mov dword [var_34h], edi ; argc
|           0x5bb6440d749a      488975c0       mov qword [var_40h], rsi ; argv
|           0x5bb6440d749e      64488b0425..   mov rax, qword fs:[0x28]
|           0x5bb6440d74a7      488945f8       mov qword [canary], rax
|           0x5bb6440d74ab      31c0           xor eax, eax
|           0x5bb6440d74ad      488d3d550b..   lea rdi, str.Enter_your_license_key: ; 0x5bb6440d8009 ; "Enter your license key: " ; const char *format
|           0x5bb6440d74b4      b800000000     mov eax, 0
|           0x5bb6440d74b9      e8f2fbffff     call sym.imp.printf     ; int printf(const char *format)
|           0x5bb6440d74be      488b154b2b..   mov rdx, qword [reloc.stdin] ; [0x5bb6440da010:8]=0x7ac7fe5f68e0 ; FILE *stream
|           0x5bb6440d74c5      488d45d0       lea rax, [s]
|           0x5bb6440d74c9      be25000000     mov esi, 0x25           ; '%' ; 37 ; int size
|           0x5bb6440d74ce      4889c7         mov rdi, rax            ; char *s
|           0x5bb6440d74d1      e8fafbffff     call sym.imp.fgets      ; char *fgets(char *s, int size, FILE *stream)
|           0x5bb6440d74d6      488d45d0       lea rax, [s]
|           0x5bb6440d74da      4889c7         mov rdi, rax            ; char *arg1
|           0x5bb6440d74dd      e827fdffff     call fcn.00001209
|           0x5bb6440d74e2      84c0           test al, al
|       ,=< 0x5bb6440d74e4      740e           je 0x5bb6440d74f4
|       |   0x5bb6440d74e6      488d3d350b..   lea rdi, str.That_key_is_valid. ; 0x5bb6440d8022 ; "That key is valid." ; const char *s
|       |   0x5bb6440d74ed      e8cefbffff     call sym.imp.puts       ; int puts(const char *s)
|      ,==< 0x5bb6440d74f2      eb0c           jmp 0x5bb6440d7500
|      ||   ; CODE XREF from main @ 0x5bb6440d74e4(x)
|      |`-> 0x5bb6440d74f4      488d3d3a0b..   lea rdi, str.That_key_is_invalid. ; 0x5bb6440d8035 ; "That key is invalid." ; const char *s
|      |    0x5bb6440d74fb      e8c0fbffff     call sym.imp.puts       ; int puts(const char *s)
|      |    ; CODE XREF from main @ 0x5bb6440d74f2(x)
|      `--> 0x5bb6440d7500      b800000000     mov eax, 0
|           0x5bb6440d7505      488b4df8       mov rcx, qword [canary]
|           0x5bb6440d7509      6448330c25..   xor rcx, qword fs:[0x28]
|       ,=< 0x5bb6440d7512      7405           je 0x5bb6440d7519
|       |   0x5bb6440d7514      e8f7fbffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
|       |   ; CODE XREF from main @ 0x5bb6440d7512(x)
|       `-> 0x5bb6440d7519      c9             leave
\           0x5bb6440d751a      c3             ret
[0x5bb6440d748b]> pdf @fcn.00001209
            ; CALL XREF from main @ 0x5bb6440d74dd(x)
/ 642: fcn.00001209 (char *arg1);
|           ; arg char *arg1 @ rdi
|           ; var int64_t canary @ rbp-0x8
|           ; var int64_t var_dh @ rbp-0xd
|           ; var int64_t var_eh @ rbp-0xe
|           ; var int64_t var_fh @ rbp-0xf
|           ; var int64_t var_10h @ rbp-0x10
|           ; var int64_t var_11h @ rbp-0x11
|           ; var int64_t var_12h @ rbp-0x12
|           ; var int64_t var_13h @ rbp-0x13
|           ; var int64_t var_14h @ rbp-0x14
|           ; var int64_t var_15h @ rbp-0x15
|           ; var int64_t var_30h @ rbp-0x30
|           ; var int64_t var_3bh @ rbp-0x3b
|           ; var char *var_50h @ rbp-0x50
|           ; var int64_t var_53h @ rbp-0x53
|           ; var int64_t var_58h @ rbp-0x58
|           ; var int64_t var_5ah @ rbp-0x5a
|           ; var int64_t var_62h @ rbp-0x62
|           ; var char *var_70h @ rbp-0x70
|           ; var int64_t var_78h @ rbp-0x78
|           ; var int64_t var_80h @ rbp-0x80
|           ; var int64_t var_88h @ rbp-0x88
|           ; var char *s @ rbp-0x90
|           ; var int64_t var_a0h @ rbp-0xa0
|           ; var int64_t var_b0h @ rbp-0xb0
|           ; var char *var_b2h @ rbp-0xb2
|           ; var signed int64_t var_b8h @ rbp-0xb8
|           ; var char *var_bch @ rbp-0xbc
|           ; var signed int64_t var_c0h @ rbp-0xc0
|           ; var signed int64_t var_c4h @ rbp-0xc4
|           ; var int64_t var_c8h @ rbp-0xc8
|           ; var char *var_d8h @ rbp-0xd8
|           0x5bb6440d7209      f30f1efa       endbr64
|           0x5bb6440d720d      55             push rbp
|           0x5bb6440d720e      4889e5         mov rbp, rsp
|           0x5bb6440d7211      4881ece000..   sub rsp, 0xe0
|           0x5bb6440d7218      4889bd28ff..   mov qword [var_d8h], rdi ; arg1
|           0x5bb6440d721f      64488b0425..   mov rax, qword fs:[0x28]
|           0x5bb6440d7228      488945f8       mov qword [canary], rax
|           0x5bb6440d722c      31c0           xor eax, eax
|           0x5bb6440d722e      48b8706963..   movabs rax, 0x7b4654436f636970 ; 'picoCTF{'
|           0x5bb6440d7238      48ba627231..   movabs rdx, 0x30795f676e317262 ; 'br1ng_y0'
|           0x5bb6440d7242      48898570ff..   mov qword [s], rax
|           0x5bb6440d7249      48899578ff..   mov qword [var_88h], rdx
|           0x5bb6440d7250      48b875725f..   movabs rax, 0x6b5f6e77305f7275 ; 'ur_0wn_k'
|           0x5bb6440d725a      48894580       mov qword [var_80h], rax
|           0x5bb6440d725e      c745883379..   mov dword [var_78h], 0x5f7933 ; '3y_'
|           0x5bb6440d7265      66c7854eff..   mov word [var_b2h], 0x7d ; '}' ; 125
|           0x5bb6440d726e      488d8570ff..   lea rax, [s]
|           0x5bb6440d7275      4889c7         mov rdi, rax            ; const char *s
|           0x5bb6440d7278      e863feffff     call sym.imp.strlen     ; size_t strlen(const char *s)
|           0x5bb6440d727d      4889c1         mov rcx, rax
|           0x5bb6440d7280      488d9550ff..   lea rdx, [var_b0h]
|           0x5bb6440d7287      488d8570ff..   lea rax, [s]
|           0x5bb6440d728e      4889ce         mov rsi, rcx
|           0x5bb6440d7291      4889c7         mov rdi, rax
|           0x5bb6440d7294      e857feffff     call sym.imp.MD5
|           0x5bb6440d7299      488d854eff..   lea rax, [var_b2h]
|           0x5bb6440d72a0      4889c7         mov rdi, rax            ; const char *s
|           0x5bb6440d72a3      e838feffff     call sym.imp.strlen     ; size_t strlen(const char *s)
|           0x5bb6440d72a8      4889c1         mov rcx, rax
|           0x5bb6440d72ab      488d9560ff..   lea rdx, [var_a0h]
|           0x5bb6440d72b2      488d854eff..   lea rax, [var_b2h]
|           0x5bb6440d72b9      4889ce         mov rsi, rcx
|           0x5bb6440d72bc      4889c7         mov rdi, rax
|           0x5bb6440d72bf      e82cfeffff     call sym.imp.MD5
|           0x5bb6440d72c4      c78538ffff..   mov dword [var_c8h], 0
|           0x5bb6440d72ce      c7853cffff..   mov dword [var_c4h], 0
|       ,=< 0x5bb6440d72d8      eb47           jmp 0x5bb6440d7321
|       |   ; CODE XREF from fcn.00001209 @ 0x5bb6440d7328(x)
|      .--> 0x5bb6440d72da      8b853cffffff   mov eax, dword [var_c4h]
|      :|   0x5bb6440d72e0      4898           cdqe
|      :|   0x5bb6440d72e2      0fb6840550..   movzx eax, byte [rbp + rax - 0xb0]
|      :|   0x5bb6440d72ea      0fb6c0         movzx eax, al
|      :|   0x5bb6440d72ed      488d4d90       lea rcx, [var_70h]
|      :|   0x5bb6440d72f1      8b9538ffffff   mov edx, dword [var_c8h]
|      :|   0x5bb6440d72f7      4863d2         movsxd rdx, edx
|      :|   0x5bb6440d72fa      4801d1         add rcx, rdx
|      :|   0x5bb6440d72fd      89c2           mov edx, eax
|      :|   0x5bb6440d72ff      488d35fe0c..   lea rsi, str._02x       ; 0x5bb6440d8004 ; "%02x" ; const char *format
|      :|   0x5bb6440d7306      4889cf         mov rdi, rcx            ; char *s
|      :|   0x5bb6440d7309      b800000000     mov eax, 0
|      :|   0x5bb6440d730e      e8edfdffff     call sym.imp.sprintf    ; int sprintf(char *s, const char *format, ...)
|      :|   0x5bb6440d7313      83853cffff..   add dword [var_c4h], 1
|      :|   0x5bb6440d731a      838538ffff..   add dword [var_c8h], 2
|      :|   ; CODE XREF from fcn.00001209 @ 0x5bb6440d72d8(x)
|      :`-> 0x5bb6440d7321      83bd3cffff..   cmp dword [var_c4h], 0xf
|      `==< 0x5bb6440d7328      7eb0           jle 0x5bb6440d72da
|           0x5bb6440d732a      c78538ffff..   mov dword [var_c8h], 0
|           0x5bb6440d7334      c78540ffff..   mov dword [var_c0h], 0
|       ,=< 0x5bb6440d733e      eb47           jmp 0x5bb6440d7387
|       |   ; CODE XREF from fcn.00001209 @ 0x5bb6440d738e(x)
|      .--> 0x5bb6440d7340      8b8540ffffff   mov eax, dword [var_c0h]
|      :|   0x5bb6440d7346      4898           cdqe
|      :|   0x5bb6440d7348      0fb6840560..   movzx eax, byte [rbp + rax - 0xa0]
|      :|   0x5bb6440d7350      0fb6c0         movzx eax, al
|      :|   0x5bb6440d7353      488d4db0       lea rcx, [var_50h]
|      :|   0x5bb6440d7357      8b9538ffffff   mov edx, dword [var_c8h]
|      :|   0x5bb6440d735d      4863d2         movsxd rdx, edx
|      :|   0x5bb6440d7360      4801d1         add rcx, rdx
|      :|   0x5bb6440d7363      89c2           mov edx, eax
|      :|   0x5bb6440d7365      488d35980c..   lea rsi, str._02x       ; 0x5bb6440d8004 ; "%02x" ; const char *format
|      :|   0x5bb6440d736c      4889cf         mov rdi, rcx            ; char *s
|      :|   0x5bb6440d736f      b800000000     mov eax, 0
|      :|   0x5bb6440d7374      e887fdffff     call sym.imp.sprintf    ; int sprintf(char *s, const char *format, ...)
|      :|   0x5bb6440d7379      838540ffff..   add dword [var_c0h], 1
|      :|   0x5bb6440d7380      838538ffff..   add dword [var_c8h], 2
|      :|   ; CODE XREF from fcn.00001209 @ 0x5bb6440d733e(x)
|      :`-> 0x5bb6440d7387      83bd40ffff..   cmp dword [var_c0h], 0xf
|      `==< 0x5bb6440d738e      7eb0           jle 0x5bb6440d7340
|           0x5bb6440d7390      c78544ffff..   mov dword [var_bch], 0
|       ,=< 0x5bb6440d739a      eb23           jmp 0x5bb6440d73bf
|       |   ; CODE XREF from fcn.00001209 @ 0x5bb6440d73c6(x)
|      .--> 0x5bb6440d739c      8b8544ffffff   mov eax, dword [var_bch]
|      :|   0x5bb6440d73a2      4898           cdqe
|      :|   0x5bb6440d73a4      0fb6940570..   movzx edx, byte [rbp + rax - 0x90]
|      :|   0x5bb6440d73ac      8b8544ffffff   mov eax, dword [var_bch]
|      :|   0x5bb6440d73b2      4898           cdqe
|      :|   0x5bb6440d73b4      885405d0       mov byte [rbp + rax - 0x30], dl
|      :|   0x5bb6440d73b8      838544ffff..   add dword [var_bch], 1
|      :|   ; CODE XREF from fcn.00001209 @ 0x5bb6440d739a(x)
|      :`-> 0x5bb6440d73bf      83bd44ffff..   cmp dword [var_bch], 0x1a
|      `==< 0x5bb6440d73c6      7ed4           jle 0x5bb6440d739c
|           0x5bb6440d73c8      0fb645c5       movzx eax, byte [var_3bh]
|           0x5bb6440d73cc      8845eb         mov byte [var_15h], al
|           0x5bb6440d73cf      0fb645a6       movzx eax, byte [var_5ah]
|           0x5bb6440d73d3      8845ec         mov byte [var_14h], al
|           0x5bb6440d73d6      0fb645a6       movzx eax, byte [var_5ah]
|           0x5bb6440d73da      8845ed         mov byte [var_13h], al
|           0x5bb6440d73dd      0fb64590       movzx eax, byte [var_70h]
|           0x5bb6440d73e1      8845ee         mov byte [var_12h], al
|           0x5bb6440d73e4      0fb645ad       movzx eax, byte [var_53h]
|           0x5bb6440d73e8      8845ef         mov byte [var_11h], al
|           0x5bb6440d73eb      0fb645c5       movzx eax, byte [var_3bh]
|           0x5bb6440d73ef      8845f0         mov byte [var_10h], al
|           0x5bb6440d73f2      0fb6459e       movzx eax, byte [var_62h]
|           0x5bb6440d73f6      8845f1         mov byte [var_fh], al
|           0x5bb6440d73f9      0fb645a8       movzx eax, byte [var_58h]
|           0x5bb6440d73fd      8845f2         mov byte [var_eh], al
|           0x5bb6440d7400      0fb6854eff..   movzx eax, byte [var_b2h]
|           0x5bb6440d7407      8845f3         mov byte [var_dh], al
|           0x5bb6440d740a      488b8528ff..   mov rax, qword [var_d8h]
|           0x5bb6440d7411      4889c7         mov rdi, rax            ; const char *s
|           0x5bb6440d7414      e8c7fcffff     call sym.imp.strlen     ; size_t strlen(const char *s)
|           0x5bb6440d7419      4883f824       cmp rax, 0x24           ; '$' ; 36
|       ,=< 0x5bb6440d741d      7407           je 0x5bb6440d7426
|       |   0x5bb6440d741f      b800000000     mov eax, 0
|      ,==< 0x5bb6440d7424      eb4f           jmp 0x5bb6440d7475
|      ||   ; CODE XREF from fcn.00001209 @ 0x5bb6440d741d(x)
|      |`-> 0x5bb6440d7426      c78548ffff..   mov dword [var_b8h], 0
|      |,=< 0x5bb6440d7430      eb35           jmp 0x5bb6440d7467
|      ||   ; CODE XREF from fcn.00001209 @ 0x5bb6440d746e(x)
|     .---> 0x5bb6440d7432      8b8548ffffff   mov eax, dword [var_b8h]
|     :||   0x5bb6440d7438      4863d0         movsxd rdx, eax
|     :||   0x5bb6440d743b      488b8528ff..   mov rax, qword [var_d8h]
|     :||   0x5bb6440d7442      4801d0         add rax, rdx
|     :||   0x5bb6440d7445      0fb610         movzx edx, byte [rax]
|     :||   0x5bb6440d7448      8b8548ffffff   mov eax, dword [var_b8h]
|     :||   0x5bb6440d744e      4898           cdqe
|     :||   0x5bb6440d7450      0fb64405d0     movzx eax, byte [rbp + rax - 0x30]
|     :||   0x5bb6440d7455      38c2           cmp dl, al
|    ,====< 0x5bb6440d7457      7407           je 0x5bb6440d7460
|    |:||   0x5bb6440d7459      b800000000     mov eax, 0
|   ,=====< 0x5bb6440d745e      eb15           jmp 0x5bb6440d7475
|   ||:||   ; CODE XREF from fcn.00001209 @ 0x5bb6440d7457(x)
|   |`----> 0x5bb6440d7460      838548ffff..   add dword [var_b8h], 1
|   | :||   ; CODE XREF from fcn.00001209 @ 0x5bb6440d7430(x)
|   | :|`-> 0x5bb6440d7467      83bd48ffff..   cmp dword [var_b8h], 0x23 ; '#'
|   | `===< 0x5bb6440d746e      7ec2           jle 0x5bb6440d7432
|   |  |    0x5bb6440d7470      b801000000     mov eax, 1
|   |  |    ; CODE XREFS from fcn.00001209 @ 0x5bb6440d7424(x), 0x5bb6440d745e(x)
|   `--`--> 0x5bb6440d7475      488b75f8       mov rsi, qword [canary]
|           0x5bb6440d7479      6448333425..   xor rsi, qword fs:[0x28]
|       ,=< 0x5bb6440d7482      7405           je 0x5bb6440d7489
|       |   0x5bb6440d7484      e887fcffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
|       |   ; CODE XREF from fcn.00001209 @ 0x5bb6440d7482(x)
|       `-> 0x5bb6440d7489      c9             leave
\           0x5bb6440d748a      c3             ret
[0x5bb6440d748b]> db 0x5bb6440d740a
[0x5bb6440d748b]> dc
[+] SIGNAL 28 errno=0 addr=0x00000000 code=128 si_pid=0 ret=0
INFO: hit breakpoint at: 0x5bb6440d748b
[+] signal 28 aka SIGWINCH received 0 (Window Changed Size)
[0x5bb6440d748b]> pdf
            ;-- rax:
            ;-- rip:
            ; DATA XREF from entry0 @ 0x5bb6440d7141(r)
/ 144: int main (int argc, char **argv, char **envp);
|           ; arg int argc @ rdi
|           ; arg char **argv @ rsi
|           ; var int64_t canary @ rbp-0x8
|           ; var char *s @ rbp-0x30
|           ; var int64_t var_34h @ rbp-0x34
|           ; var char **var_40h @ rbp-0x40
|           0x5bb6440d748b b    f30f1efa       endbr64
|           0x5bb6440d748f      55             push rbp
|           0x5bb6440d7490      4889e5         mov rbp, rsp
|           0x5bb6440d7493      4883ec40       sub rsp, 0x40
|           0x5bb6440d7497      897dcc         mov dword [var_34h], edi ; argc
|           0x5bb6440d749a      488975c0       mov qword [var_40h], rsi ; argv
|           0x5bb6440d749e      64488b0425..   mov rax, qword fs:[0x28]
|           0x5bb6440d74a7      488945f8       mov qword [canary], rax
|           0x5bb6440d74ab      31c0           xor eax, eax
|           0x5bb6440d74ad      488d3d550b..   lea rdi, str.Enter_your_license_key: ; 0x5bb6440d8009 ; "Enter your license key: " ; const char *format
|           0x5bb6440d74b4      b800000000     mov eax, 0
|           0x5bb6440d74b9      e8f2fbffff     call sym.imp.printf     ; int printf(const char *format)
|           0x5bb6440d74be      488b154b2b..   mov rdx, qword [reloc.stdin] ; [0x5bb6440da010:8]=0x7ac7fe5f68e0 ; FILE *stream
|           0x5bb6440d74c5      488d45d0       lea rax, [s]
|           0x5bb6440d74c9      be25000000     mov esi, 0x25           ; '%' ; 37 ; int size
|           0x5bb6440d74ce      4889c7         mov rdi, rax            ; char *s
|           0x5bb6440d74d1      e8fafbffff     call sym.imp.fgets      ; char *fgets(char *s, int size, FILE *stream)
|           0x5bb6440d74d6      488d45d0       lea rax, [s]
|           0x5bb6440d74da      4889c7         mov rdi, rax            ; char *arg1
|           0x5bb6440d74dd      e827fdffff     call fcn.00001209
|           0x5bb6440d74e2      84c0           test al, al
|       ,=< 0x5bb6440d74e4      740e           je 0x5bb6440d74f4
|       |   0x5bb6440d74e6      488d3d350b..   lea rdi, str.That_key_is_valid. ; 0x5bb6440d8022 ; "That key is valid." ; const char *s
|       |   0x5bb6440d74ed      e8cefbffff     call sym.imp.puts       ; int puts(const char *s)
|      ,==< 0x5bb6440d74f2      eb0c           jmp 0x5bb6440d7500
|      ||   ; CODE XREF from main @ 0x5bb6440d74e4(x)
|      |`-> 0x5bb6440d74f4      488d3d3a0b..   lea rdi, str.That_key_is_invalid. ; 0x5bb6440d8035 ; "That key is invalid." ; const char *s
|      |    0x5bb6440d74fb      e8c0fbffff     call sym.imp.puts       ; int puts(const char *s)
|      |    ; CODE XREF from main @ 0x5bb6440d74f2(x)
|      `--> 0x5bb6440d7500      b800000000     mov eax, 0
|           0x5bb6440d7505      488b4df8       mov rcx, qword [canary]
|           0x5bb6440d7509      6448330c25..   xor rcx, qword fs:[0x28]
|       ,=< 0x5bb6440d7512      7405           je 0x5bb6440d7519
|       |   0x5bb6440d7514      e8f7fbffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
|       |   ; CODE XREF from main @ 0x5bb6440d7512(x)
|       `-> 0x5bb6440d7519      c9             leave
\           0x5bb6440d751a      c3             ret
[0x5bb6440d748b]> dc
INFO: hit breakpoint at: 0x5bb6440d740a
[0x5bb6440d740a]> pdf
            ; CALL XREF from main @ 0x5bb6440d74dd(x)
/ 642: fcn.00001209 (char *arg1);
|           ; arg char *arg1 @ rdi
|           ; var int64_t canary @ rbp-0x8
|           ; var int64_t var_dh @ rbp-0xd
|           ; var int64_t var_eh @ rbp-0xe
|           ; var int64_t var_fh @ rbp-0xf
|           ; var int64_t var_10h @ rbp-0x10
|           ; var int64_t var_11h @ rbp-0x11
|           ; var int64_t var_12h @ rbp-0x12
|           ; var int64_t var_13h @ rbp-0x13
|           ; var int64_t var_14h @ rbp-0x14
|           ; var int64_t var_15h @ rbp-0x15
|           ; var int64_t var_30h @ rbp-0x30
|           ; var int64_t var_3bh @ rbp-0x3b
|           ; var char *var_50h @ rbp-0x50
|           ; var int64_t var_53h @ rbp-0x53
|           ; var int64_t var_58h @ rbp-0x58
|           ; var int64_t var_5ah @ rbp-0x5a
|           ; var int64_t var_62h @ rbp-0x62
|           ; var char *var_70h @ rbp-0x70
|           ; var int64_t var_78h @ rbp-0x78
|           ; var int64_t var_80h @ rbp-0x80
|           ; var int64_t var_88h @ rbp-0x88
|           ; var char *s @ rbp-0x90
|           ; var int64_t var_a0h @ rbp-0xa0
|           ; var int64_t var_b0h @ rbp-0xb0
|           ; var char *var_b2h @ rbp-0xb2
|           ; var signed int64_t var_b8h @ rbp-0xb8
|           ; var char *var_bch @ rbp-0xbc
|           ; var signed int64_t var_c0h @ rbp-0xc0
|           ; var signed int64_t var_c4h @ rbp-0xc4
|           ; var int64_t var_c8h @ rbp-0xc8
|           ; var char *var_d8h @ rbp-0xd8
|           0x5bb6440d7209      f30f1efa       endbr64
|           0x5bb6440d720d      55             push rbp
|           0x5bb6440d720e      4889e5         mov rbp, rsp
|           0x5bb6440d7211      4881ece000..   sub rsp, 0xe0
|           0x5bb6440d7218      4889bd28ff..   mov qword [var_d8h], rdi ; arg1
|           0x5bb6440d721f      64488b0425..   mov rax, qword fs:[0x28]
|           0x5bb6440d7228      488945f8       mov qword [canary], rax
|           0x5bb6440d722c      31c0           xor eax, eax
|           0x5bb6440d722e      48b8706963..   movabs rax, 0x7b4654436f636970 ; 'picoCTF{'
|           0x5bb6440d7238      48ba627231..   movabs rdx, 0x30795f676e317262 ; 'br1ng_y0'
|           0x5bb6440d7242      48898570ff..   mov qword [s], rax
|           0x5bb6440d7249      48899578ff..   mov qword [var_88h], rdx
|           0x5bb6440d7250      48b875725f..   movabs rax, 0x6b5f6e77305f7275 ; 'ur_0wn_k'
|           0x5bb6440d725a      48894580       mov qword [var_80h], rax
|           0x5bb6440d725e      c745883379..   mov dword [var_78h], 0x5f7933 ; '3y_'
|           0x5bb6440d7265      66c7854eff..   mov word [var_b2h], 0x7d ; rax
|           0x5bb6440d726e      488d8570ff..   lea rax, [s]
|           0x5bb6440d7275      4889c7         mov rdi, rax            ; const char *s
|           0x5bb6440d7278      e863feffff     call sym.imp.strlen     ; size_t strlen(const char *s)
|           0x5bb6440d727d      4889c1         mov rcx, rax
|           0x5bb6440d7280      488d9550ff..   lea rdx, [var_b0h]
|           0x5bb6440d7287      488d8570ff..   lea rax, [s]
|           0x5bb6440d728e      4889ce         mov rsi, rcx
|           0x5bb6440d7291      4889c7         mov rdi, rax
|           0x5bb6440d7294      e857feffff     call sym.imp.MD5
|           0x5bb6440d7299      488d854eff..   lea rax, [var_b2h]
|           0x5bb6440d72a0      4889c7         mov rdi, rax            ; const char *s
|           0x5bb6440d72a3      e838feffff     call sym.imp.strlen     ; size_t strlen(const char *s)
|           0x5bb6440d72a8      4889c1         mov rcx, rax
|           0x5bb6440d72ab      488d9560ff..   lea rdx, [var_a0h]
|           0x5bb6440d72b2      488d854eff..   lea rax, [var_b2h]
|           0x5bb6440d72b9      4889ce         mov rsi, rcx
|           0x5bb6440d72bc      4889c7         mov rdi, rax
|           0x5bb6440d72bf      e82cfeffff     call sym.imp.MD5
|           0x5bb6440d72c4      c78538ffff..   mov dword [var_c8h], 0
|           0x5bb6440d72ce      c7853cffff..   mov dword [var_c4h], 0
|       ,=< 0x5bb6440d72d8      eb47           jmp 0x5bb6440d7321
|       |   ; CODE XREF from fcn.00001209 @ 0x5bb6440d7328(x)
|      .--> 0x5bb6440d72da      8b853cffffff   mov eax, dword [var_c4h]
|      :|   0x5bb6440d72e0      4898           cdqe
|      :|   0x5bb6440d72e2      0fb6840550..   movzx eax, byte [rbp + rax - 0xb0]
|      :|   0x5bb6440d72ea      0fb6c0         movzx eax, al
|      :|   0x5bb6440d72ed      488d4d90       lea rcx, [var_70h]
|      :|   0x5bb6440d72f1      8b9538ffffff   mov edx, dword [var_c8h]
|      :|   0x5bb6440d72f7      4863d2         movsxd rdx, edx
|      :|   0x5bb6440d72fa      4801d1         add rcx, rdx
|      :|   0x5bb6440d72fd      89c2           mov edx, eax
|      :|   0x5bb6440d72ff      488d35fe0c..   lea rsi, str._02x       ; 0x5bb6440d8004 ; "%02x" ; const char *format
|      :|   0x5bb6440d7306      4889cf         mov rdi, rcx            ; char *s
|      :|   0x5bb6440d7309      b800000000     mov eax, 0
|      :|   0x5bb6440d730e      e8edfdffff     call sym.imp.sprintf    ; int sprintf(char *s, const char *format, ...)
|      :|   0x5bb6440d7313      83853cffff..   add dword [var_c4h], 1
|      :|   0x5bb6440d731a      838538ffff..   add dword [var_c8h], 2
|      :|   ; CODE XREF from fcn.00001209 @ 0x5bb6440d72d8(x)
|      :`-> 0x5bb6440d7321      83bd3cffff..   cmp dword [var_c4h], 0xf
|      `==< 0x5bb6440d7328      7eb0           jle 0x5bb6440d72da
|           0x5bb6440d732a      c78538ffff..   mov dword [var_c8h], 0
|           0x5bb6440d7334      c78540ffff..   mov dword [var_c0h], 0
|       ,=< 0x5bb6440d733e      eb47           jmp 0x5bb6440d7387
|       |   ; CODE XREF from fcn.00001209 @ 0x5bb6440d738e(x)
|      .--> 0x5bb6440d7340      8b8540ffffff   mov eax, dword [var_c0h]
|      :|   0x5bb6440d7346      4898           cdqe
|      :|   0x5bb6440d7348      0fb6840560..   movzx eax, byte [rbp + rax - 0xa0]
|      :|   0x5bb6440d7350      0fb6c0         movzx eax, al
|      :|   0x5bb6440d7353      488d4db0       lea rcx, [var_50h]
|      :|   0x5bb6440d7357      8b9538ffffff   mov edx, dword [var_c8h]
|      :|   0x5bb6440d735d      4863d2         movsxd rdx, edx
|      :|   0x5bb6440d7360      4801d1         add rcx, rdx
|      :|   0x5bb6440d7363      89c2           mov edx, eax
|      :|   0x5bb6440d7365      488d35980c..   lea rsi, str._02x       ; 0x5bb6440d8004 ; "%02x" ; const char *format
|      :|   0x5bb6440d736c      4889cf         mov rdi, rcx            ; char *s
|      :|   0x5bb6440d736f      b800000000     mov eax, 0
|      :|   0x5bb6440d7374      e887fdffff     call sym.imp.sprintf    ; int sprintf(char *s, const char *format, ...)
|      :|   0x5bb6440d7379      838540ffff..   add dword [var_c0h], 1
|      :|   0x5bb6440d7380      838538ffff..   add dword [var_c8h], 2
|      :|   ; CODE XREF from fcn.00001209 @ 0x5bb6440d733e(x)
|      :`-> 0x5bb6440d7387      83bd40ffff..   cmp dword [var_c0h], 0xf
|      `==< 0x5bb6440d738e      7eb0           jle 0x5bb6440d7340
|           0x5bb6440d7390      c78544ffff..   mov dword [var_bch], 0
|       ,=< 0x5bb6440d739a      eb23           jmp 0x5bb6440d73bf
|       |   ; CODE XREF from fcn.00001209 @ 0x5bb6440d73c6(x)
|      .--> 0x5bb6440d739c      8b8544ffffff   mov eax, dword [var_bch]
|      :|   0x5bb6440d73a2      4898           cdqe
|      :|   0x5bb6440d73a4      0fb6940570..   movzx edx, byte [rbp + rax - 0x90]
|      :|   0x5bb6440d73ac      8b8544ffffff   mov eax, dword [var_bch]
|      :|   0x5bb6440d73b2      4898           cdqe
|      :|   0x5bb6440d73b4      885405d0       mov byte [rbp + rax - 0x30], dl
|      :|   0x5bb6440d73b8      838544ffff..   add dword [var_bch], 1
|      :|   ; CODE XREF from fcn.00001209 @ 0x5bb6440d739a(x)
|      :`-> 0x5bb6440d73bf      83bd44ffff..   cmp dword [var_bch], 0x1a
|      `==< 0x5bb6440d73c6      7ed4           jle 0x5bb6440d739c
|           0x5bb6440d73c8      0fb645c5       movzx eax, byte [var_3bh]
|           0x5bb6440d73cc      8845eb         mov byte [var_15h], al
|           0x5bb6440d73cf      0fb645a6       movzx eax, byte [var_5ah]
|           0x5bb6440d73d3      8845ec         mov byte [var_14h], al
|           0x5bb6440d73d6      0fb645a6       movzx eax, byte [var_5ah]
|           0x5bb6440d73da      8845ed         mov byte [var_13h], al
|           0x5bb6440d73dd      0fb64590       movzx eax, byte [var_70h]
|           0x5bb6440d73e1      8845ee         mov byte [var_12h], al
|           0x5bb6440d73e4      0fb645ad       movzx eax, byte [var_53h]
|           0x5bb6440d73e8      8845ef         mov byte [var_11h], al
|           0x5bb6440d73eb      0fb645c5       movzx eax, byte [var_3bh]
|           0x5bb6440d73ef      8845f0         mov byte [var_10h], al
|           0x5bb6440d73f2      0fb6459e       movzx eax, byte [var_62h]
|           0x5bb6440d73f6      8845f1         mov byte [var_fh], al
|           0x5bb6440d73f9      0fb645a8       movzx eax, byte [var_58h]
|           0x5bb6440d73fd      8845f2         mov byte [var_eh], al
|           0x5bb6440d7400      0fb6854eff..   movzx eax, byte [var_b2h]
|           0x5bb6440d7407      8845f3         mov byte [var_dh], al
|           ;-- rip:
|           0x5bb6440d740a b    488b8528ff..   mov rax, qword [var_d8h]
|           0x5bb6440d7411      4889c7         mov rdi, rax            ; const char *s
|           0x5bb6440d7414      e8c7fcffff     call sym.imp.strlen     ; size_t strlen(const char *s)
|           0x5bb6440d7419      4883f824       cmp rax, 0x24           ; '$' ; 36
|       ,=< 0x5bb6440d741d      7407           je 0x5bb6440d7426
|       |   0x5bb6440d741f      b800000000     mov eax, 0
|      ,==< 0x5bb6440d7424      eb4f           jmp 0x5bb6440d7475
|      ||   ; CODE XREF from fcn.00001209 @ 0x5bb6440d741d(x)
|      |`-> 0x5bb6440d7426      c78548ffff..   mov dword [var_b8h], 0
|      |,=< 0x5bb6440d7430      eb35           jmp 0x5bb6440d7467
|      ||   ; CODE XREF from fcn.00001209 @ 0x5bb6440d746e(x)
|     .---> 0x5bb6440d7432      8b8548ffffff   mov eax, dword [var_b8h]
|     :||   0x5bb6440d7438      4863d0         movsxd rdx, eax
|     :||   0x5bb6440d743b      488b8528ff..   mov rax, qword [var_d8h]
|     :||   0x5bb6440d7442      4801d0         add rax, rdx
|     :||   0x5bb6440d7445      0fb610         movzx edx, byte [rax]
|     :||   0x5bb6440d7448      8b8548ffffff   mov eax, dword [var_b8h]
|     :||   0x5bb6440d744e      4898           cdqe
|     :||   0x5bb6440d7450      0fb64405d0     movzx eax, byte [rbp + rax - 0x30]
|     :||   0x5bb6440d7455      38c2           cmp dl, al
|    ,====< 0x5bb6440d7457      7407           je 0x5bb6440d7460
|    |:||   0x5bb6440d7459      b800000000     mov eax, 0
|   ,=====< 0x5bb6440d745e      eb15           jmp 0x5bb6440d7475
|   ||:||   ; CODE XREF from fcn.00001209 @ 0x5bb6440d7457(x)
|   |`----> 0x5bb6440d7460      838548ffff..   add dword [var_b8h], 1
|   | :||   ; CODE XREF from fcn.00001209 @ 0x5bb6440d7430(x)
|   | :|`-> 0x5bb6440d7467      83bd48ffff..   cmp dword [var_b8h], 0x23 ; '#'
|   | `===< 0x5bb6440d746e      7ec2           jle 0x5bb6440d7432
|   |  |    0x5bb6440d7470      b801000000     mov eax, 1
|   |  |    ; CODE XREFS from fcn.00001209 @ 0x5bb6440d7424(x), 0x5bb6440d745e(x)
|   `--`--> 0x5bb6440d7475      488b75f8       mov rsi, qword [canary]
|           0x5bb6440d7479      6448333425..   xor rsi, qword fs:[0x28]
|       ,=< 0x5bb6440d7482      7405           je 0x5bb6440d7489
|       |   0x5bb6440d7484      e887fcffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
|       |   ; CODE XREF from fcn.00001209 @ 0x5bb6440d7482(x)
|       `-> 0x5bb6440d7489      c9             leave
\           0x5bb6440d748a      c3             ret
[0x5bb6440d740a]> ps @rbp-0xb2
}
[0x5bb6440d740a]> ps @rbp-0x15
abb48a6c}
[0x5bb6440d740a]>
```
---

