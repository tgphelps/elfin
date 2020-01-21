#!/usr/bin/env python

"""
elfin.py: Intel x64 ELF file investigator

Usage:
    elfin.py [-l] ELF

Options:
    -h --help           Show this screen, and exit.
    -l --log            Create debugging log file
"""

from typing import Dict, Any

import docopt  # type: ignore

import log
import util
import Elf


# Constants
VERSION = '0.01'
LOG_FILE = 'LOG.txt'


# Global variables

class Globals:
    log:  bool
    file: str


g = Globals()
g.log = False
g.file = ''


def main() -> None:
    args = docopt.docopt(__doc__, version=VERSION)
    # print(args)
    save_cmd_line(args)
    if g.log:
        log.log_open(LOG_FILE)
    ok, err = Elf.is_elf64_file(g.file)
    if not ok:
        util.fatal(f"cannot open or init ELF. Error: {err}")
    if g.log:
        log.log_close()


def save_cmd_line(args: Dict[str, Any]) -> None:
    if args['--log']:
        g.log = True
    g.file = args['ELF']


if __name__ == '__main__':
    main()
