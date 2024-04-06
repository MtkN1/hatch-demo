# SPDX-FileCopyrightText: 2024-present MtkN1 <51289448+MtkN1@users.noreply.github.com>
#
# SPDX-License-Identifier: MIT
import sys


def print_version():
    version_info = tuple(sys.version_info[:2])

    if version_info == (3, 8):
        print("You are running Python 3.8")
    elif version_info == (3, 9):
        print("You are running Python 3.9")
    elif version_info == (3, 10):
        print("You are running Python 3.10")
    elif version_info == (3, 11):
        print("You are running Python 3.11")
    else:
        print("You are running Python >= 3.12")
