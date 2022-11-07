"""
SHELLCODE-EXTRACTOR
Tool used to extract shellcode and lenght from an object/binary file.

Copyright (C) 2022  Neetx

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

def banner():
    print(" _____ _          _ _               _        _____     _                  _         ")
    print("/  ___| |        | | |             | |      |  ___|   | |                | |            ")
    print("\\ `--.| |__   ___| | | ___ ___   __| | ___  | |____  _| |_ _ __ __ _  ___| |_ ___  _ __ ")
    print(" `--. \\ '_ \\ / _ \\ | |/ __/ _ \\ / _` |/ _ \\ |  __\\ \\/ / __| '__/ _` |/ __| __/ _ \\| '__|")
    print("/\\__/ / | | |  __/ | | (_| (_) | (_| |  __/ | |___>  <| |_| | | (_| | (__| || (_) | |   ")
    print("\\____/|_| |_|\\___|_|_|\\___\\___/ \\__,_|\\___| \\____/_/\\_\\___|_|  \\__,_|\\___|\\__\\___/|_|   ")
    print("                                                             Neext: neetx@protonmail.com")

def error():
    print("\nError! \n Usage:  objdump -d example.o | python shellcode_extractor.py \n")

def main():
    if not sys.stdin.isatty():
        try:
            shellcode = ""
            lenght = 0
            while True:
                item = sys.stdin.readline()
                if item:
                    if re.match("^[ ]*[0-9a-f]*:.*$", item):
                        item = item.split(":")[1].lstrip()
                        x = item.split("\t")
                        opcode = re.findall("[0-9a-f][0-9a-f]",x[0])
                        for i in opcode:
                            shellcode += "\\x" + i
                            lenght += 1
                else: 
                    break
            if shellcode == "":
                print("Nothing to extract")
            else:    
                print("\n" + shellcode)
                print("\nLenght: " + str(lenght) + "\n")
        except:
            error()
            pass
    else:
        error()

if __name__ == "__main__":
    banner()
    main()