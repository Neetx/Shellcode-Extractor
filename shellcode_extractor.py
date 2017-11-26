"""Neetx ShellcodeExtractor"""
import sys, re

try:
    shellcode = ""
    while True:
        item = sys.stdin.readline()
        if item:
            if re.match("^[ ]*[0-9a-f]*:.*$",item):
                item =item.split(":")[1].lstrip()
                x = item.split("\t")
                opcode = re.findall("[0-9a-f][0-9a-f]",x[0])
                for i in opcode:
                    shellcode += "\\x" + i
        else: 
            break
    if shellcode == "":
        print "Nothing to extract"
    else:    
        print shellcode
except:
    print "Error! \n Usage:  objdump -d example.o | python shellcode_extractor.py" 
    pass