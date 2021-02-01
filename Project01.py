#!/usr/bin/env python3
from colorama import Fore, Back, Style
import os
def logo():
    print(Fore.RED + """
 _____           _         _       ___ ___   
|  _  |___ ___  |_|___ ___| |_ ___|   |_  |  
|   __|  _| . | | | -_|  _|  _|___| | |_| |_ 
|__|  |_| |___|_| |___|___|_|     |___|_____|
              |___|                          """)
    print(Fore.YELLOW+"""
----------------------------------------------
             EXPLAINER (JoyGhosh)
----------------------------------------------

""")
def main():
    inp=input(Fore.WHITE+"project01@root~ ")
    print(Fore.GREEN+" ")
    os.system('curl -s https://explainshell.com/explain?cmd='+inp+' | grep "help-box" |html2text')
    print(Fore.WHITE+" ")
    main()
logo()
main()