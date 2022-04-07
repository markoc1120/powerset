"""Module for computing power sets."""

from typing import Any


def power(x: list[Any]) -> list[list[Any]]:
    """
    Compute the power-set of x.

    Returns the power-set of x as a list of lists.

    >>> power([])
    [[]]
    >>> power([1])
    [[], [1]]
    >>> power([1, 2])
    [[], [1], [2], [1, 2]]
    """
    n = 2**len(x)
    res = []
    for i in range(n):
        bits = format(i, "b").zfill(len(x))
        elements = [i for i, b in enumerate(bits) if b == '1']
        res.append([x[j] for j in elements])
    return res
