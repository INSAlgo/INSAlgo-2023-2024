# Fonction récursive avec tail call (donc optimisée (pas en python hélas))
def atoi_calc(s: list[str], acc: int = 0) -> int :
    match s:
        case [] :
            return acc
        case [n, *_] if not n.isdigit():
            return acc
        case [n, *tail]:
            return atoi_calc(tail, acc*10+int(n))

def atoi_sign(s: list[str]) -> int :
    match s:
        case ["-", *tail]:
            return -atoi_calc(tail)
        case ["+", *tail] | tail:
            return atoi_calc(tail)

def atoi_whitespace(s: list[str]) -> int :
    match s:
        case [" ", *tail]:
            return atoi_whitespace(tail)
        case other:
            return atoi_sign(other)

def atoi(s: str) -> int:
    return max(min(atoi_whitespace(list(s)), 2**31-1), -2**31)


class Solution:
    def myAtoi(self, s: str) -> int:
        return atoi(s)
