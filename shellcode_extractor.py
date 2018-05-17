"""
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

CONTACTS:
    - neetx@protonmail.com
"""

import sys, re

if not sys.stdin.isatty():
    try:
        shellcode = ""
        lenght = 0
        while True:
            item = sys.stdin.readline()
            if item:
                if re.match("^[ ]*[0-9a-f]*:.*$",item):
                    item =item.split(":")[1].lstrip()
                    x = item.split("\t")
                    opcode = re.findall("[0-9a-f][0-9a-f]",x[0])
                    for i in opcode:
                        shellcode += "\\x" + i
                        lenght += 1
            else: 
                break
        if shellcode == "":
            print "Nothing to extract"
        else:    
            print "\n" + shellcode
            print "\nLenght: " + str(lenght) + "\n"
    except:
        print "\nError! \n Usage:  objdump -d example.o | python shellcode_extractor.py" 
        pass
else:
    print "\nError! \n Usage:  objdump -d example.o | python shellcode_extractor.py \n" 
