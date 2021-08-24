"""
Alfredo Osuna Torres            A01339250
Fabricio Andre Fuentes Fuentes  A01338527
"""

import re


def email(str):
    regla = "^[a-z0-9._%+-]+@[a-z0-9]+\.[a-z]{2,}|[a-z0-9]+\.[a-z]{2,}\.[a-z]{2,}$"
    p = re.compile(regla)
    if p.search(str):
        return True
    return False


def phone_number(str):
    str = str.replace(" ", "")
    regla = "^(\d{10})|\+1\(52\)(\d{10})$"
    p = re.compile(regla)
    if p.search(str):
        return True
    return False


def hexadecimal(str):
    regex = r"^0x([A-Fa-f0-9]{8})$"

    if re.fullmatch(regex, str):
        return True
    else:
        return False
