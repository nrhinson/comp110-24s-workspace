"""CQ07."""

__author__ = "730664337"


def f(n: int, k: int) -> int:
    """Recursion fucntion that is used to multipy."""
    if n == 0:
        return 0
    else:
        return k + f(n - 1, k)