#!/usr/bin/env python

def split(word):
    return list(word)


userinput = input('string: ')
userinput2 = input('vm name: ')
inputlist = split(userinput)

keydict = {
    "1" : "0x02",
    "2" : "0x03",
    "3" : "0x04",
    "4" : "0x05",
    "5" : "0x06",
    "6" : "0x07",
    "7" : "0x08",
    "8" : "0x09",
    "9" : "0x0a",
    "0" : "0x0b",
    "-" : "0x0c",
    "=" : "0x0d",
    "q" : "0x10",
    "w" : "0x11",
    "e" : "0x12",
    "r" : "0x13",
    "t" : "0x14",
    "y" : "0x15",
    "u" : "0x16",
    "i" : "0x17",
    "o" : "0x18",
    "p" : "0x19",
    "[" : "0x1a",
    "]" : "0x1b",
    "a" : "0x1e",
    "s" : "0x1f",
    "d" : "0x20",
    "f" : "0x21",
    "g" : "0x22",
    "h" : "0x23",
    "j" : "0x24",
    "k" : "0x25",
    "l" : "0x26",
    ";" : "0x27",
    "'" : "0x28",
    "`" : "0x29",
    chr(92) : "0x2b",
    "z" : "0x2c",
    "x" : "0x2d",
    "c" : "0x2e",
    "v" : "0x2f",
    "b" : "0x30",
    "n" : "0x31",
    "m" : "0x32",
    "," : "0x33",
    "." : "0x34",
    "/" : "0x35",
    "*" : "0x37",
     "!" : "0x2a 0x02",
    "@" : "0x2a 0x03",
    "#" : "0x2a 0x04",
    "$" : "0x2a 0x05",
    "%" : "0x2a 0x06",
    "^" : "0x2a 0x07",
    "&" : "0x2a 0x08",
    "(" : "0x2a 0x0a",
    ")" : "0x2a 0x0b",
    "_" : "0x2a 0x0c",
    "+" : "0x2a 0x0d",
    "Q" : "0x2a 0x10",
    "W" : "0x2a 0x11",
    "E" : "0x2a 0x12",
    "R" : "0x2a 0x13",
    "T" : "0x2a 0x14",
    "Y" : "0x2a 0x15",
    "U" : "0x2a 0x16",
    "I" : "0x2a 0x17",
    "O" : "0x2a 0x18",
    "P" : "0x2a 0x19",
    "{" : "0x2a 0x1a",
    "}" : "0x2a 0x1b",
    "A" : "0x2a 0x1e",
    "S" : "0x2a 0x1f",
    "D" : "0x2a 0x20",
    "F" : "0x2a 0x21",
    "G" : "0x2a 0x22",
    "H" : "0x2a 0x23",
    "J" : "0x2a 0x24",
    "K" : "0x2a 0x25",
    "L" : "0x2a 0x26",
    ":" : "0x2a 0x27",
    '"' : "0x2a 0x28",
    "~" : "0x2a 0x29",
    "|": "0x2a 0x2b",
    "Z" : "0x2a 0x2c",
    "X" : "0x2a 0x2d",
    "C" : "0x2a 0x2e",
    "V" : "0x2a 0x2f",
    "B" : "0x2a 0x30",
    "N" : "0x2a 0x31",
    "M" : "0x2a 0x32",
    "<" : "0x2a 0x33",
    ">" : "0x2a 0x34",
    "?" : "0x2a 0x35",
    " " : "0x39"
}

f = open("copypasta.sh", "w")
f.write("#!/bin/bash\n")
for i in range(len(inputlist)):
   if inputlist[i] in keydict:
      f.write(f"sudo virsh send-key {userinput2} --codeset xt {keydict.get(inputlist[i])}\n")
f.close()

