from string import ascii_letters, digits

Digits = digits + ascii_letters


def c(n: str, bt: int, bf: int = 10) -> int:

    if isinstance(n, str):
        n = int(n, bf)
    else:
        n = int(num)

    if n < bt:
        return Digits[n]
    else:
        return c(n // bt, bt) + Digits[n % bt]
