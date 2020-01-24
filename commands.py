
from typing import Tuple, Any

import Elf
import lexer
import parser


class Globals:
    elf: Elf.Elf


g = Globals()


def run(elf: Elf.Elf) -> None:
    g.elf = elf
    lex = lexer.ElfLexer()  # type: ignore
    par = parser.ElfParser()  # type: ignore
    while True:
        try:
            text = input('cmd > ')
            result: Tuple[Any, ...] = par.parse(lex.tokenize(text))
            if not result:
                continue
            if result[0] == 'quit':
                break
            else:
                print(result)
                handler = result[0]
                args = result[1]
                func[handler](args)
        except EOFError:
            break


def cmd_help(_) -> None:
    print("help command")


def cmd_print(obj: str) -> None:
    print(f"print command: {obj}")
    if obj == 'hdr':
        g.elf.print_elf_hdr()
    else:
        assert False


def cmd_dump(obj: Any) -> None:
    # obj can be a string or a tuple
    print(f"dump command: {obj}")


func = {
        'help': cmd_help,
        'print': cmd_print,
        'dump': cmd_dump
        }
