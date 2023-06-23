#!/bin/python3.11
import os
import sys
import shutil

MK_PATH = "/usr/share/mkmf/"

def checkIfInstalled() -> int:
    if os.path.isdir(MK_PATH): return 0

    print("Can't find any Makefiles to copy, make sure that the program is installed.")
    return 1

def langValid(lang) -> int:
    installed_langs = os.listdir(MK_PATH)
    if lang not in installed_langs:
        print(f"${lang} is not available")
        return 1
    return 0

def doCopy(lang) -> int:
    if os.path.exists("./makefile"):
        t = input("There's already a Makefile here, do you want to proceed? [Y/n] ")
        
        if not t.lower() in ["", "y"]: return 0

    shutil.copy(MK_PATH + lang, "./makefile")
    return 0

def main() -> int:
    # Creates a Makefile depending on the language given.

    # do prechecks
    if len(sys.argv) <= 1:
        print("Syntax error: mkmf <language>")
        return 1
    
    lang = sys.argv[1]
    if checkIfInstalled(): return 1
    if langValid(lang): return 1
    
    doCopy(lang)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())


