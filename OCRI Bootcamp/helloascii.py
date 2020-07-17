# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 18:19:48 2020

@author: Levitannin

This is homework for the OCRI 0 -- Assignment 2.5.1
"""
import pyfiglet

character = 'a'
print(ord(character))   #   prints  97

name = 'levitannin'

asciidecimalname = []
asciihexidecimal = []
asciibinary = []

for char in name:
    decimal_char = ord(char)
    hex_char = hex(ord(char))
    binary_char = bin(ord(char))
    
    asciidecimalname.append(decimal_char)
    asciihexidecimal.append(hex_char)
    asciibinary.append(binary_char)

print("Hello world, it's me " + name)
print("Hello world, it's me in decimal " + str(asciidecimalname))
print("Hello world, it's me in hexidecimal " + str(asciihexidecimal))
print("Hello world, it's me in binary " + str(asciibinary))


ascii_banner = pyfiglet.figlet_format("Hello world!!")
print(ascii_banner)

print("                _____")
print("             ,-'     '-.")
print("            / o       o \"")
print("           /   \     /   \"")
print("          /     )-'-(     \"")
print("         /     ( 6 6 )     \"")
print("        /       \ ' /       \"")
print("       /         )=(         \"")
print("      /   o   .--'-'--.   o   \"")
print("     /    I  /  -   -  \  I    \"")
print(" .--(    (_}y/\       /\y{_)    )--.")
print("(    '.___l\/__\_____/__\/l___,'    )")
print(" \                                 /")
print("  '-._      o O o O o O o      _,-'")
print("      `--Y--.___________.--Y--'")
print("         |==.___________.==| hjw")
print("         `==.___________.==' `97")
