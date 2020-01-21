
"""
Elf.py is a module for reading and decoding Intel x64 ELF files,
both executable and relocatable.
"""

from typing import Tuple


# Constants
HDR_SIZE = 64


def is_elf64_file(fname: str) -> Tuple[bool, int]:
    """
    Determines whether fname is an ELF file or not.

    Returns (True, 0) if it is, and (False, <err>) if not.
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


if __name__ == '__main__':
    good, reason = is_elf64_file('bad')
    print(f'status = {good}, reason = {reason}')
    good, reason = is_elf64_file('tests/hello')
    print(f'status = {good}, reason = {reason}')
