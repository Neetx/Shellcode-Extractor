ShellcodeExtractor
========

SHELLCODE-EXTRACTOR
Tool used to extract shellcode and lenght from an object/binary file.

Copyright (C) 2017  Neetx

This file is part of Shellcode-Extractor.

Shellcode-Extractor is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Shellcode-Extractor is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>

### CONTACTS:
[Neetx](mailto:neetx@protonmail.com)

---
Tool developed for study and research reasons, I hope it will be useful.

### Usage

Write assembly code, product an object file and the use this script in pipeline to objdump.

Example:

Let's write spwaning shell assembly code in spawnshell.asm ( NASM )

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

Lenght: 1822
```
---
### Testing:

Insert our shellcode into the empty string in shellcode_tester.c, compile it with gcc and run.
