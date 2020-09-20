from string import ascii_uppercase, digits


def translate(num: int, base_to: int, base_from: int = 10) -> int:

    if isinstance(num, str):
        num_tlt = int(num, base_from)
    else:
        num_tlt = int(num)

    numl = digits + ascii_uppercase
    if num_tlt < base_to:
        return numl[num_tlt]
    else:
        return translate(num_tlt // base_to, base_to) + numl[num_tlt % base_to]


def count_chars(seq: str, character: str) -> int:

    count = 0
    for sym in seq:
        if sym == character:
            count += 1

    return count
