
import struct


class Phent:
    "Program header table entry"
    def __init__(self, ent: bytes):
        a, b, c, d, e, f, g, h = \
            struct.unpack("<IIQQQQQQ", ent)
        self.data = ent
        self.p_type = a
        self.p_flags = b
        self.p_offset = c
        self.p_vaddr = d
        _ = e
        self.p_filesz = f
        self.p_memsz = g
        self.p_align = h
