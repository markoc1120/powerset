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
    return []  # FIXME: you need to add some code here.
