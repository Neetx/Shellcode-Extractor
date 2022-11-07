ShellcodeExtractor
========

Simple tool developed for study and research reasons, I hope it will be useful.  
The goal is to extract the shellcode and its length from an object/binary file.


### Usage

Write assembly code, product an object file and the use this script in pipeline to objdump.

Example:

The example is on Linux, but shellcode-extractor works on macos too.  
Let's write spwaning shell assembly code in spawnshell.asm (NASM)

```
	xor eax, eax,
	push eax
	push 0x68732f2f
	push 0x6e69622f
	mov ebx, esp
	push eax
	mov edx, esp
	push ebx
	mov ecx, esp
	mov al, 11
	int 0x80
```

Launch : 
```
nobody@nobody:~$ nasm -f elf spawnshell.asm -o output.o
```

Now we can use our script: 
```
nobody@nobody:~$ objdump -d output.o | python shellcode_extractor.py

\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80

Lenght: 25
```
---
### Testing:

Insert our shellcode into the empty string in shellcode_tester.c or shellcode_tester_macos.c, compile it with gcc and run (remember: on macos gcc is an alias for clang).

### CONTACTS:
[Neetx](mailto:neetx@protonmail.com)