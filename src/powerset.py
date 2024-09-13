"""Module for computing power sets."""

from typing import Any


def power(x: list[Any]) -> list[list[Any]]:
    """
    Compute the power-set of x.

    Returns the power-set of x as a list of lists.
    """

    def recursion(_list, res, n):
        if n == 0:
            return [res.copy()]
        res.append(_list[n - 1])
        with_element = recursion(_list, res, n - 1)
        res.pop()
        without_element = recursion(_list, res, n - 1)
        return with_element + without_element

    list_length, ans = len(x), []
    return recursion(x, ans, list_length)


print(power([1, 2]))
