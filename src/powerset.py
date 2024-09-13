"""Module for computing power sets."""

from typing import Any


def power(x: list[Any]) -> list[list[Any]]:
    """
    Compute the power-set of x.

    Returns the power-set of x as a list of lists.
    """

    def recursion(x, ans, n):
        if n == 0:
            return [ans.copy()]
        ans.append(x[n - 1])
        with_element = recursion(x, ans, n - 1)
        ans.pop()
        without_element = recursion(x, ans, n - 1)
        return with_element + without_element

    n, ans = len(x), []
    return recursion(x, ans, n)
