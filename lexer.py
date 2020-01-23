
# type: ignore
# flake8: noqa

from sly import Lexer


class ElfLexer(Lexer):
    tokens = {ID, PRINT, DUMP, QUIT, HELP, HDR, PHT, SHT, HEXNUM, NUMBER}

    ignore = ' \t'

    ID = r'[a-zA-Z][a-zA-z0-9]*'
    HEXNUM = r'0[0-9a-fA-F]+'
    NUMBER = r'\d+'

    ID['p'] = PRINT
    ID['d'] = DUMP
    ID['q'] = QUIT
    ID['help'] = HELP
    ID['hdr'] = HDR
    ID['pht'] = PHT
    ID['sht'] = SHT

    def error(self, t):
        print(f"Illegal character {t.value[0]}")
        self.index += 1


def main():
    data = [
        "p hdr",
        "d pht",
        "p sht",
        "q",
        "help",       
        "d 07f 012FD"
        ]
    lexer = ElfLexer()
    for s in data:
        for tok in lexer.tokenize(s):
            print('type=%r, value=%r, len=%r' %
                  (tok.type, tok.value, len(tok.value)))


if __name__ == '__main__':
    main()
