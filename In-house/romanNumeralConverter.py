# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 17:13:31 2021

@author: DeleLinus
"""
def convertRomanNumeral(romNumeral):
    """
    converts Roman numerals into ordinary numbers.
    
    Params:
        romNumeral (String) - the Roman numeral string to be converted
        
    
    Returns:
        num (int): ordinary numbers equivalant of the roman numeral.
    
    Examples:
        >>> num = convertRomanNumeral("M")
        >>>print(num)
        100
        
        >>> num = convertRomanNumeral("DX")
        >>>print(num)
        510
        
        >>> num = convertRomanNumeral("XL")
        >>>print(num)
        40
    
    """
    romNumeral = romNumeral.upper()
    rom_dict = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1,'IV':4,\
                'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    i = 0
    num = 0
    while i < len(romNumeral):
        if i+1<len(romNumeral) and romNumeral[i:i+2] in rom_dict:
            num+=rom_dict[romNumeral[i:i+2]]
            i+=2
        else:
            num+=rom_dict[romNumeral[i]]
            i+=1
    return num


rom_num = input("Enter the Roman Numeral you would like to convert: ")
num = convertRomanNumeral(rom_num)

print("The integer representation of %s is %d"%(rom_num,num))
