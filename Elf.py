
"""
Elf.py is a module for reading and decoding Intel x64 ELF files,
both executable and relocatable.
"""

from typing import Tuple

import struct
import sys

# Constants
HDR_SIZE = 64


def is_elf64_file(fname: str) -> Tuple[bool, int]:
    """
    Determines whether fname is an ELF file or not.

    Returns (True, 0) if it is, and (False, <err>) if not.
    We verify that: the file is readable, it is at least HDR_SIZE bytes in length,
    and the interesting fields in e_ident are good.
    """
    try:
        with open(fname, 'rb') as f:
            hdr = f.read(HDR_SIZE)
            if len(hdr) != HDR_SIZE:
                return False, 2  # header read was short
            else:
                magic = hdr[0:4]
                if magic != b'\x7fELF':
                    return False, 3
                if hdr[4] != 2:
                    return False, 4
                if hdr[5] != 1:
                    return False, 5
                if hdr[6] != 1:
                    return False, 6
                if hdr[7] != 0 or hdr[8] != 0:
                    return False, 7
                return True, 0
    except IOError:
        return False, 1  # failed to read file


class Elf:
    """
    Elf is an object that represents an Intel x64 ELF file. Creating one will throw
    an exception if the file passed to __init__ isn't a proper ELF.
    """
    def __init__(self, fname:str):
        self.elf = open(fname, 'rb')
        self.hdr = self.elf.read(HDR_SIZE)
        self.e_ident = self.hdr[0:16]
        assert len(self.hdr) == HDR_SIZE

        assert self.hdr[0:4] == b'\x7fELF'
        self.ei_class = self.hdr[4]
        self.ei_data = self.hdr[5]
        self.ei_version = self.hdr[6]
        self.ei_osabi = self.hdr[7]
        self.ei_abiversion = self.hdr[8]

        assert self.ei_class == 2
        assert self.ei_data == 1
        assert self.ei_version == 1
        assert self.ei_osabi == 0
        assert self.ei_abiversion == 0

        fields = self.hdr[16:]
        a,b,c,d,e,f,g,h,i,j,k,l,m = struct.unpack('<HHIQQQIHHHHHH', fields)
        self.e_type = a
        self.e_machine = b
        self.e_version = c
        self.e_entry = d
        self.e_phoff = e
        self.e_shoff = f
        self.e_flags = g
        self.e_ehsize = h
        self.e_phentsize = i
        self.e_phnum = j
        self.e_shentsize = k
        self.e_shnum = l
        self.e_shstrndx = m

    def print_elf_hdr(self, out=sys.stdout):
        print(f"{self.ei_class=}")
        print(f"{self.ei_data=}")
        print(f"{self.ei_version=}")
        print(f"{self.ei_osabi=}")
        print(f"{self.ei_abiversion=}")
        print(f"{self.e_type=}")
        print(f"{self.e_machine=}")
        print(f"{self.e_version=}")
        print(f"{self.e_entry=:#010x}")
        print(f"{self.e_phoff=:#010x}")
        print(f"{self.e_shoff=:#010x}")
        print(f"{self.e_flags=:#06x}")
        print(f"{self.e_ehsize=}")
        print(f"{self.e_phentsize=}")
        print(f"{self.e_phnum=}")
        print(f"{self.e_shentsize=}")
        print(f"{self.e_shnum=}")
        print(f"{self.e_shstrndx=}")

    def close(self) -> None:
        self.elf.close()
        self.elf = None


if __name__ == '__main__':
    good, reason = is_elf64_file('bad')
    print(f'status = {good}, reason = {reason}')
    good, reason = is_elf64_file('tests/hello')
    print(f'status = {good}, reason = {reason}')
