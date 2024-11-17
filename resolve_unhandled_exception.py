#!/usr/bin/env python3

__author__ = "Ibor E. Offor"
__email__ = "iboroffor@gmail.com"

"""
    A simple script to resolve UnhandledExecption that pops up
    on trying to open the ECC App on a system. Thank you again!
"""

import os

if __name__ == "__main__":
    
    os.chdir('C:/Users/ECC/AppData/Local/NCC_Case_System/NCC_Case_System.exe_Url_1claezvvoktxaehwgbbu0fpstsfoljsd/1.0.0.0/')
    try:
        os.remove('user.config')
    except FileNotFoundError:
        print('The "user.config" file is already deleted.')
    os.chdir('C:/Users/ECC/Desktop')
    os.startfile('NCC_Case_System')
