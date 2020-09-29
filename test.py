from string import ascii_letters, digits

Digits = digits + ascii_letters


def c(n: str, to_base: int, from_base: int = 10) -> int:

    if isinstance(n, str):
        n = int(n, from_base)
    else:
        n = int(n)

    if n < to_base:
        return Digits[n]
    else:
        return c(n // to_base, to_base) + Digits[n % to_base]
