# Question : https://www.codingame.com/training/easy/ascii-art

import sys
import math

l = int(input())
h = int(input())
t = input()
asciiArt = []
for i in range(h):
    row = input()
    asciiArt.append(row)

def printChar(char):
    asciiVal = ord(char)
    charNum = 0
    charAsciiArt = []
    if (asciiVal >= 65 and asciiVal <= 90) or (asciiVal >= 97 and asciiVal <= 122):
        if asciiVal <= 90:
            charNum = asciiVal - 65
        else:
            charNum = asciiVal - 97
            
        for i in range(h):
            row = ""
            for j in range(l*charNum, l*charNum+l):
                row += asciiArt[i][j]
            charAsciiArt.append(row)
    else:
        for i in range(h):
            row = ""
            for j in range(l*26,  l*26+l):
                row += asciiArt[i][j]
            charAsciiArt.append(row)
    return charAsciiArt

result = []
for char in t:
    charAsciiArt = printChar(char)
    result.append(charAsciiArt)
    
for line in range(h):
    for char in result:
        print(char[line], end="")
    print()