ELF INvestigator
================
A program to view and explore Intel x64 ELF files, both executable
and relocatable types. Eventually, I hope it can disassemble code.

Usage
-----
    elfin <options> <ELF-file>
    No options yet
Elfin reads commands from stdin and writes to stdout, for now.

Commands
--------
    p hdr | pht | sht
    d hdr | pht NUM | sht NUM | HEX HEX
    help
    q

tokens: print dump quit help hdr pht sht hexnum number
