ShellcodeExtractor

Python script for extracting shellcode from object file.

Write assembly code, product an object file and the use this script in pipeline to objdump.

Example:

Let's write spwaning shell assembly code in spawnshell.asm ( NASM )

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

Launch : nasm -f elf spawnshell.asm -o output.o

Now we can use our script: objdump -d output.o | python shellcode_extractor.py

The output is:	\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80


